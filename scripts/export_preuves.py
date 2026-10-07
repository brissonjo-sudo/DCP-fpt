"""Exporte un kit Codex vérifié sans flux bruts, pensées ni signatures."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ("legifrance.gouv.fr", "eur-lex.europa.eu", "curia.europa.eu",
           "economie.gouv.fr", "cnil.fr", "conseil-etat.fr", "courdecassation.fr")


def official(url: str) -> bool:
    """Vérifie la frontière du nom de domaine, pas une simple sous-chaîne."""
    host = (urlsplit(url).hostname or "").lower()
    return any(host == domain or host.endswith("." + domain) for domain in DOMAINS)


def clean_url(url: str) -> str:
    """Garde les sélecteurs documentaires publics et élimine credentials et jetons."""
    parts = urlsplit(url)
    query = urlencode(sorted((k, v) for k, v in parse_qsl(parts.query)
                             if k.lower() in {"uri", "celex", "id", "date", "lang"}))
    return urlunsplit((parts.scheme, parts.hostname or "", parts.path, query, ""))


def role_trace(events: list[dict]) -> dict:
    """Sépare recherche, ouverture explicite et action ambiguë sans les confondre."""
    result = {"read_commands": [], "search_calls": 0, "official_search_results": [],
              "official_results_action_unknown": [], "official_open_results": [], "mcp_calls": [], "usage": None}
    for event in events:
        if event.get("type") == "turn.completed":
            result["usage"] = event.get("usage")
        if event.get("type") != "item.completed":
            continue
        item = event.get("item") or {}
        if item.get("type") == "command_execution":
            result["read_commands"].append({"exit_code": item.get("exit_code"), "status": item.get("status"),
                "runtime_paths": sorted(set(re.findall(r"\.agents/skills/dcp-fpt/[\w./-]+", item.get("command", "").replace("\\", "/"))))})
        if item.get("type") == "mcp_tool_call":
            response = item.get("result") or {}
            success = item.get("status") == "completed" and bool(response) and not response.get("isError", False) and not item.get("error")
            structured = response.get("structuredContent")
            if not isinstance(structured, dict):
                structured = None
                for block in response.get("content", []):
                    if block.get("type") == "text":
                        try:
                            candidate = json.loads(block.get("text", ""))
                        except (ValueError, TypeError):
                            continue
                        if isinstance(candidate, dict):
                            structured = candidate
                            break
            sources = []
            if success and item.get("server") == "droit-francais" and item.get("tool") in ("get_article", "fetch", "get_section", "get_decision") and structured:
                for node in [structured, *structured.get("articles", [])]:
                    metadata = node.get("metadata") or {}
                    url = node.get("url", "")
                    if url and official(url) and node.get("text") and metadata.get("verified"):
                        sources.append({"url": clean_url(url), "title": node.get("title"), "id": node.get("id"),
                            "metadata": {key: metadata.get(key) for key in ("source", "verified", "as_of_date", "requested_date", "legal_status", "version_start_date", "version_end_date", "applicable_at_as_of_date", "content_complete")},
                            "text_sha256": hashlib.sha256(node["text"].encode()).hexdigest()})
            result["mcp_calls"].append({"server": item.get("server"), "tool": item.get("tool"),
                "succeeded": success, "sources": sources,
                "result_sha256": hashlib.sha256(json.dumps(response, sort_keys=True, ensure_ascii=False).encode()).hexdigest()})
        if item.get("type") != "web_search":
            continue
        action = (item.get("action") or {}).get("type")
        if action == "search":
            result["search_calls"] += 1
            destination = "official_search_results"
        elif action in ("open_page", "find_in_page"):
            destination = "official_open_results"
        else:
            destination = "official_results_action_unknown"
        for source in item.get("results", []):
            url = source.get("url", "")
            if not url or not official(url):
                continue
            entry = {"url": clean_url(url), "title": source.get("title")}
            if destination == "official_open_results":
                entry.update(action=action, retrieval_marker=source.get("snippet", "")[:80])
            result[destination].append(entry)
    return result


def copy_checked(source: Path, destination: Path) -> None:
    """Une preuve différente ne peut jamais écraser une preuve publiée."""
    data = source.read_bytes()
    if destination.exists() and destination.read_bytes() != data:
        raise ValueError(f"Preuve existante différente : {destination.name}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)


def save(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def frozen_module(kit: Path):
    """Contrôle les scripts avant de charger le vérificateur propre au kit."""
    frozen = json.loads((kit / "kit.json").read_text(encoding="utf-8"))
    for name in ("eval_suite.py", "mesure_locale.py"):
        if hashlib.sha256((kit / "scripts" / name).read_bytes()).hexdigest() != frozen["scripts_sha256"][name]:
            raise ValueError("Script figé altéré : " + name)
    modules = {}
    for name in ("eval_suite", "mesure_locale"):
        spec = importlib.util.spec_from_file_location(name, kit / "scripts" / (name + ".py"))
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        modules[name] = module
    return modules["mesure_locale"]


def export(kit: Path, output: Path, commit: str) -> dict:
    """Vérifie entrées/sorties de chaque rôle avant export assaini."""
    output = output.resolve()
    if not output.is_relative_to(ROOT / "tests/runs") or output.is_symlink():
        raise ValueError("La destination doit rester sous tests/runs")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("Commit source attendu sur 40 caractères")
    mesure = frozen_module(kit)
    cases = mesure.verify_kit(kit)
    settings = mesure.load(kit / "resultats/execution.json")
    if settings["engine"] != "codex":
        raise ValueError("Cet exporteur attend des traces Codex")
    manifest = mesure.load(kit / "resultats/manifest.json")
    # Rattacher chaque octet runtime à la source annoncée, pas à HEAD.
    for name, digest in manifest["runtime_sha256"].items():
        content = subprocess.run(["git", "show", f"{commit}:{name}"], cwd=ROOT,
                                 check=True, capture_output=True).stdout
        if hashlib.sha256(content).hexdigest() != digest:
            raise ValueError("Runtime différent du commit source : " + name)
    complete = []
    for case in cases:
        folder = kit / "resultats" / case["id"]
        if not (folder / "judgment.json").is_file():
            continue
        for role in ("respondant", "juge"):
            mesure.verify_evidence(kit, case, role, settings)
        complete.append((case, folder))
    # Aucun artefact n'est publié avant vérification de l'ensemble sélectionné.
    for name in ("suite.json", "bareme.md"):
        copy_checked(kit / "resultats" / name, output / name)
    progress = []
    for case, folder in complete:
        target = output / case["id"]
        for name in ("prompt.md", "response.md", "judgment.json", "respondant-execution.json", "juge-execution.json"):
            copy_checked(folder / name, target / name)
        trace = {"case_id": case["id"], "audit_version": 3, "roles": {},
                 "exporter_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                 "review_status": "à relire, pas une validation praticien"}
        for role in ("respondant", "juge"):
            events = [json.loads(line) for line in (folder / f"{role}-stdout.txt").read_text(encoding="utf-8").splitlines() if line.strip()]
            trace["roles"][role] = role_trace(events)
        text = (folder / "response.md").read_text(encoding="utf-8")
        cited = {clean_url(url.rstrip(".,;")) for url in re.findall(r"https?://[^\s)\]>]+", text) if official(url)}
        opened = {s["url"] for s in trace["roles"]["respondant"]["official_open_results"]}
        fetched = {s["url"] for call in trace["roles"]["respondant"]["mcp_calls"] for s in call["sources"]}
        trace["official_citations_without_matching_open_url"] = sorted(cited - opened)
        trace["official_citations_without_matching_retrieval"] = sorted(cited - opened - fetched)
        trace["source_audit_note"] = "Correspondance d'URL et récupération MCP explicite seulement ; application au dossier et portée restent à contrôler."
        save(target / "trace-assainie.json", trace)
        progress.append({"case_id": case["id"], "verdict": mesure.load(folder / "judgment.json")["verdict"],
                         "response_sha256": hashlib.sha256((folder / "response.md").read_bytes()).hexdigest(),
                         "citation_alerts": len(cited - opened - fetched)})
    manifest["source_runtime_commit"] = commit
    manifest["public_trace_policy"] = "Flux bruts hors dépôt ; réponses, jugements, empreintes et traces assainies exportés."
    save(output / "manifest.json", manifest)
    result = {"case_count": len(cases), "completed_count": len(progress), "cases": progress,
              "publication_ready": False, "human_legal_validation": False}
    save(output / "progression.json", result)
    if (kit / "resultats/summary.json").is_file():
        copy_checked(kit / "resultats/summary.json", output / "summary.json")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    args = parser.parse_args()
    try:
        result = export(args.kit.resolve(), args.output, args.source_commit)
        print(json.dumps({"completed": result["completed_count"], "publication_ready": False}))
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"[ÉCHEC] {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
