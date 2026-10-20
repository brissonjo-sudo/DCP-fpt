"""Exporte les preuves d'un contrôleur DCP sans modifier ses originaux privés."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import types
import uuid

import eval_suite
import export_preuves

ROOT = Path(__file__).resolve().parents[1]
POLICY = "mesure-controlee-publique-v1"


def digest(raw: bytes) -> str:
    """Empreinte exacte."""
    return hashlib.sha256(raw).hexdigest()


def encoded(value: dict) -> bytes:
    """JSON public UTF-8/LF."""
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def load(path: Path) -> dict:
    """Lit un JSON sans charger de code ou de cache."""
    return json.loads(path.read_bytes())


def scan_public(data: bytes) -> list[str]:
    """Signale les motifs privés sans afficher ni recopier leurs valeurs."""
    text = data.decode("utf-8")
    patterns = {
        "chemin_personnel": r"(?i)(?:[A-Z]:[/\\](?:Users|Claude code)[/\\]|/(?:home|Users)/)",
        "courriel": r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        "telephone": r"(?<!\w)(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}(?!\w)",
        "iban": r"\bFR\d{2}(?:[ -]?[0-9A-Z]){23}\b",
        "nir": r"(?<!\w)[12][ -]?\d{2}[ -]?(?:0[1-9]|1[0-2])[ -]?(?:2[AB]|\d{2})[ -]?\d{3}[ -]?\d{3}[ -]?\d{2}(?!\w)",
        "adresse_ip": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        "jeton": r"\b(?:sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9_]{16,}|github_pat_[A-Za-z0-9_]{16,})",
        "bearer": r"\bBearer\s+[^\s'\";,)}]+",
        "secret_nomme": r'''\b(?:API[_-]?KEY|ACCESS[_-]?TOKEN|REFRESH[_-]?TOKEN|CLIENT[_-]?SECRET|PASSWORD)\b["']?\s*[:=]\s*\S+''',
        "cle_privee": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        "jwt": r"\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b",
        "credentials_url": r"https?://[^/\s'\"@]+:[^@\s'\"]+@",
        "parametre_secret_url": r"[?&](?:access_token|refresh_token|token|password|secret|code|state)=",
    }
    return [name for name, pattern in patterns.items() if re.search(pattern, text, re.IGNORECASE)]


def safe_relative(root: Path, name: str) -> Path:
    """Refuse chemins redirigés, absolus ou traversants."""
    if not name or "\\" in name or ":" in name or name.startswith("/") or ".." in Path(name).parts:
        raise ValueError("Chemin de preuve invalide")
    path = root / name
    for item in (path, *path.parents):
        if item.exists() and (item.is_symlink() or getattr(item.lstat(), "st_file_attributes", 0) & 1024):
            raise ValueError("Chemin de preuve redirigé")
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("Chemin hors racine de preuve")
    return path


def protocol_from_sources(kit: Path):
    """Charge seulement les trois sources du kit vérifiées, sans cache Python."""
    sys.dont_write_bytecode = True
    expected = load(kit / "kit.json")["scripts_sha256"]
    modules = []
    for name in ("eval_suite", "mesure_locale", "controle_stop"):
        path = safe_relative(kit / "scripts", name + ".py")
        raw = path.read_bytes()
        if digest(raw) != expected[name + ".py"]:
            raise ValueError("Script figé altéré")
        module = types.ModuleType(name)
        module.__file__ = str(path)
        module.__package__ = ""
        sys.modules[name] = module
        exec(compile(raw, str(path), "exec"), module.__dict__)
        modules.append(module)
    return tuple(modules)


def export(attempt: Path, review_path: Path, review_sheet: Path, output: Path, commit: str) -> dict:
    """Vérifie le contrôleur, chaque rôle, le budget et l'avis avant tout export."""
    output = output.resolve()
    if not output.is_relative_to(ROOT / "tests/runs") or output.exists() or not re.fullmatch(r"[a-f0-9]{40}", commit):
        raise ValueError("Destination neuve sous tests/runs et commit source complet requis")
    plan_dir = attempt.parent
    summary_path = attempt / "resume-final.json"
    controller = load(summary_path)
    launcher_path = plan_dir / "MANIFESTE-LANCEUR-D1.json"
    if digest(launcher_path.read_bytes()) != controller["launcher_manifest_sha256"]:
        raise ValueError("Manifeste du contrôleur non rattaché")
    for name, record in load(launcher_path)["files"].items():
        raw = safe_relative(plan_dir, name).read_bytes()
        if digest(raw) != record["sha256"] or len(raw) != record["octets"]:
            raise ValueError("Source du contrôleur altérée")
    plan = load(plan_dir / "PLAN-D1.json")
    auth_path = plan_dir / "autorisation-jo.json"
    auth = load(auth_path)
    review = load(review_path)
    if (controller["head"] != commit or plan["candidate_commit"] != commit or auth["candidate_commit"] != commit
            or controller["attempt_id"] != attempt.name or auth["attempt_id"] != attempt.name
            or review["tentative"] != attempt.name or review["tete"] != commit
            or review["resume_final_sha256"] != digest(summary_path.read_bytes())
            or review["fiche_relecture_sha256"] != digest(review_sheet.read_bytes())):
        raise ValueError("Rattachement mesure/autorisation/avis incohérent")
    for key, path in (("plan_d0_sha256", plan_dir.parent / "PLAN-MESURE-D0.md"),
                      ("seal_d0_sha256", plan_dir.parent / "preuves/SCELLEMENT-D0.json")):
        if not (digest(path.read_bytes()) == plan[key] == auth[key] == controller[key]):
            raise ValueError("Provenance D0 altérée")
    if (auth["measurement_authorized"] is not True or auth["budget_policy"] != "between_roles"
            or controller["status"] != "completed" or controller["failure"] is not None
            or controller["input_tokens_complete"] is not True
            or controller["sessions_started"] != 56 or controller["input_tokens_limit"] != 10_000_000):
        raise ValueError("Mesure contrôlée non complète ou hors autorisation")
    kit = attempt / "kit"
    evaluation, protocol, control = protocol_from_sources(kit)
    cases = protocol.verify_kit(kit)
    ids = [case["id"] for case in cases]
    if (review["decideur"] != "Jo" or set(review["verdicts"]) != set(ids)
            or any(value != "conforme" for value in review["verdicts"].values()) or review["reserves"]):
        raise ValueError("Avis de Jo incomplet ou avec réserve")
    settings = {"engine": "codex", "cli_version": plan["requested_cli"]["version"],
                "responder_model": plan["models"]["respondant"], "judge_model": plan["models"]["juge"], "web": True}
    manifest = load(kit / "resultats/manifest.json")
    for name, expected in manifest["runtime_sha256"].items():
        blob = subprocess.run(["git", "--no-optional-locks", "-c", "safe.directory=" + str(ROOT), "show", f"{commit}:{name}"],
                              cwd=ROOT, capture_output=True, check=True).stdout
        if digest(blob) != expected:
            raise ValueError("Runtime mesuré différent du commit source")
    roles = controller["roles"]
    expected_roles = [(case["id"], role) for case in cases for role in ("respondant", "juge")]
    if [(item["case_id"], item["role"]) for item in roles] != expected_roles:
        raise ValueError("Ordre ou unicité des rôles invalide")
    if len({item["thread_id"] for item in roles}) != 56:
        raise ValueError("Session réutilisée")
    total, threads, files, progression = 0, set(), {}, []
    stop_ids = [case["id"] for case in cases if control.expected_header(case)]
    source_checks = {item["case_id"]: item for item in controller["stop_header_checks"]}
    if set(source_checks) != set(stop_ids):
        raise ValueError("Inventaire des contrôles STOP incohérent")
    for index, (case_id, role) in enumerate(expected_roles):
        if total >= auth["max_input_tokens"] or index >= auth["max_sessions"]:
            raise ValueError("Un rôle a démarré hors plafond autorisé")
        case = cases[index // 2]
        folder = kit / "resultats" / case_id
        protocol.verify_evidence(kit, case, role, settings)
        record = load(folder / (role + "-execution.json"))
        events = [json.loads(line) for line in (folder / (role + "-stdout.txt")).read_text(encoding="utf-8").splitlines() if line.strip()]
        usage_events = [event for event in events if event.get("type") == "turn.completed"]
        thread_events = [event for event in events if event.get("type") == "thread.started"]
        if (len(usage_events) != 1 or len(thread_events) != 1
                or any(event.get("type") in ("turn.failed", "error") for event in events)):
            raise ValueError("Bilan de rôle ambigu ou erreur d'exécution")
        thread = thread_events[0]["thread_id"]
        if not uuid.UUID(thread).int or thread in threads or thread != roles[index]["thread_id"]:
            raise ValueError("Thread non unique ou non rattaché")
        threads.add(thread)
        usage = usage_events[0]["usage"]
        for key in ("input_tokens", "output_tokens"):
            if type(usage.get(key)) is not int or usage[key] < 0:
                raise ValueError("Usage non attesté")
        if record["tokens"] != roles[index]["usage"] or any(record["tokens"][key] != usage[key] for key in record["tokens"]):
            raise ValueError("Usage divergent")
        if roles[index]["status"] != "completed" or roles[index]["process_exit"] != 0 or roles[index]["usage_complete"] is not True:
            raise ValueError("Rôle non achevé")
        total += usage["input_tokens"]
        files[f"{case_id}/{role}-execution.json"] = (folder / (role + "-execution.json")).read_bytes()
        if role == "respondant":
            files[f"{case_id}/prompt.md"] = (folder / "prompt.md").read_bytes()
            public, redaction = eval_suite.redact_response((folder / "response.md").read_bytes())
            files[f"{case_id}/response.md"] = public
            if redaction:
                files[f"{case_id}/redaction.json"] = encoded(redaction)
            trace = {"case_id": case_id, "audit_version": 3, "roles": {}, "review_status": "relu par Jo, non praticien"}
        trace["roles"][role] = export_preuves.role_trace(events)
        if role == "juge":
            files[f"{case_id}/judgment.json"] = (folder / "judgment.json").read_bytes()
            text = (folder / "response.md").read_text(encoding="utf-8")
            cited = {export_preuves.clean_url(url.rstrip(".,;")) for url in re.findall(r"https?://[^\s)\]>]+", text) if export_preuves.official(url)}
            opened = {entry["url"] for entry in trace["roles"]["respondant"]["official_open_results"]}
            trace["official_citations_without_matching_open_url"] = sorted(cited - opened)
            trace["source_audit_note"] = "Correspondance d'URL seulement ; ni certification juridique ni qualification du plugin."
            files[f"{case_id}/trace-assainie.json"] = encoded(trace)
            progression.append({"case_id": case_id, "verdict": load(folder / "judgment.json")["verdict"],
                                "response_sha256": digest((folder / "response.md").read_bytes()), "citation_alerts": len(cited - opened)})
            if case_id in stop_ids:
                result = control.audit_run(kit / "resultats", [case_id])
                original = folder / "controle-stop.json"
                if result != load(original) or not result["passed"] or digest(original.read_bytes()) != source_checks[case_id]["sha256"]:
                    raise ValueError("Contrôle STOP non conforme ou altéré")
                files[f"{case_id}/controle-stop.json"] = original.read_bytes()
    if total != controller["input_tokens_total_known"] or total > auth["max_input_tokens"]:
        raise ValueError("Cumul de consommation incohérent")
    totals = evaluation.validate_run(kit / "resultats")
    summary = load(kit / "resultats/summary.json")
    if totals != summary["totals"] or totals["RÉUSSITE"] != len(cases) or not summary["threshold_passed"] or summary["critical_failures"]:
        raise ValueError("Synthèse de mesure incohérente")
    public_manifest = {**manifest, "source_runtime_commit": commit, "execution_settings": settings,
        "measurement_status": "mesuré en autonome Codex ; relu par Jo non praticien",
        "public_trace_policy": POLICY}
    files.update({"suite.json": (kit / "resultats/suite.json").read_bytes(),
                  "bareme.md": (kit / "resultats/bareme.md").read_bytes(),
                  "summary.json": (kit / "resultats/summary.json").read_bytes(),
                  "manifest.json": encoded(public_manifest),
                  "progression.json": encoded({"case_count": 28, "completed_count": 28, "cases": progression,
                      "publication_ready": False, "human_legal_validation": False})})
    public_controller = copy.deepcopy(controller)
    for role in public_controller["roles"]:
        role.pop("thread_id")
    for check in public_controller["stop_header_checks"]:
        check["path"] = check["case_id"] + "/controle-stop.json"
    public_controller["upstream_summary"]["path"] = "summary.json"
    public_controller["public_projection"] = "Identifiants de thread retirés ; chemins de résultats relatifs ; état de revue initial conservé, avis ultérieur séparé."
    files["resume-final.json"] = encoded(public_controller)
    public_plan = copy.deepcopy(plan)
    public_plan["requested_cli"].pop("path")
    public_plan.pop("preserved_nonruntime_sha256", None)
    public_plan["public_projection"] = "Chemin personnel CLI et inventaire de cache privé omis ; profil et empreintes conservés."
    files["plan-mesure.json"] = encoded(public_plan)
    files["autorisation-jo.json"] = auth_path.read_bytes()
    files["avis-humain-jo-20261020.json"] = review_path.read_bytes()
    files["fiche-relecture.md"] = review_sheet.read_bytes()
    files["provenance.json"] = encoded({"policy": POLICY, "source_runtime_commit": commit,
        "private_sources_sha256": {"resume-final.json": digest(summary_path.read_bytes()), "PLAN-D1.json": digest((plan_dir / "PLAN-D1.json").read_bytes()),
            "autorisation-jo.json": digest(auth_path.read_bytes()), "avis-humain-jo-20261020.json": digest(review_path.read_bytes()),
            "fiche-relecture.md": digest(review_sheet.read_bytes()), "manifest.json": digest((kit / "resultats/manifest.json").read_bytes())},
        "source_launcher_manifest_sha256": controller["launcher_manifest_sha256"],
        "excluded": ["homes", "credentials", "flux bruts", "pensées", "signatures", "identifiants de thread", "chemins personnels"],
        "human_review": {"reviewer": "Jo", "practitioner": False, "case_count": 28, "reserves": {}},
        "publication_ready": False, "plugin_qualified": False})
    for name, raw in files.items():
        findings = scan_public(raw)
        if findings:
            raise ValueError("Export refusé : motifs privés dans " + name + " : " + ",".join(findings))
    # Aucune écriture avant vérification de l'ensemble du lot public.
    output.mkdir(parents=True, exist_ok=False)
    for name, raw in files.items():
        target = safe_relative(output, name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    inventory = {"policy": POLICY, "files": {name: digest(raw) for name, raw in sorted(files.items())}}
    (output / "empreintes.json").write_bytes(encoded(inventory))
    return {"case_count": len(cases), "sessions": len(roles), "input_tokens": total,
            "stop_checks": len(stop_ids), "public_files": len(files) + 1,
            "citation_alerts": sum(item["citation_alerts"] for item in progression)}


def verify_public_run(folder: Path) -> dict:
    """Contrôle CI des octets publics et de leurs liens, sans accès au kit privé."""
    import controle_stop
    inventory = load(folder / "empreintes.json")
    actual = {path.relative_to(folder).as_posix(): digest(path.read_bytes())
              for path in folder.rglob("*") if path.is_file() and path.name != "empreintes.json"}
    if actual != inventory["files"] or inventory["policy"] != POLICY:
        raise ValueError("Inventaire public altéré")
    for name in actual:
        if scan_public(safe_relative(folder, name).read_bytes()):
            raise ValueError("Motif privé dans la preuve publique")
        if name.endswith(("-stdout.txt", "-stderr.txt", ".pyc")) or Path(name).name in ("auth.json", "credentials.json"):
            raise ValueError("Artefact privé dans le run public")
    manifest, summary = load(folder / "manifest.json"), load(folder / "summary.json")
    cases = eval_suite.load_cases(folder / "suite.json")
    totals = eval_suite.validate_run(folder)
    if totals != summary["totals"] or summary["publication_ready"] is not False:
        raise ValueError("Synthèse publique incohérente")
    for name, expected in manifest["runtime_sha256"].items():
        blob = subprocess.run(["git", "--no-optional-locks", "-c", "safe.directory=" + str(ROOT),
                              "show", f"{manifest['source_runtime_commit']}:{name}"], cwd=ROOT,
                              check=True, capture_output=True).stdout
        if digest(blob) != expected:
            raise ValueError("Runtime public non rattaché à son commit")
    total, role_count = 0, 0
    for case in cases:
        path = folder / case["id"]
        for role, output in (("respondant", "response.md"), ("juge", "judgment.json")):
            record = load(path / (role + "-execution.json"))
            expected = eval_suite.canonical_response_digest(path / output) if role == "respondant" else digest((path / output).read_bytes())
            if (record["output_sha256"] != expected or record["fresh_process"] is not True
                    or record["fresh_workspace"] is not True or record["web_requested"] != (role == "respondant")
                    or record["native_skill_present"] != (role == "respondant")):
                raise ValueError("Rôle public incohérent")
            total += record["tokens"]["input_tokens"]
            role_count += 1
    controller = load(folder / "resume-final.json")
    if (total != controller["input_tokens_total_known"] or role_count != controller["sessions_started"]
            or any("thread_id" in record for record in controller["roles"])):
        raise ValueError("Consommation publique ou projection incohérente")
    expected_stops = [case["id"] for case in cases if controle_stop.expected_header(case)]
    if [item["case_id"] for item in controller["stop_header_checks"]] != expected_stops:
        raise ValueError("Liste STOP publique incohérente")
    for case_id in expected_stops:
        result = controle_stop.audit_run(folder, [case_id])
        if not result["passed"] or result != load(folder / case_id / "controle-stop.json"):
            raise ValueError("STOP public non conforme")
    provenance = load(folder / "provenance.json")
    review_path = folder / "avis-humain-jo-20261020.json"
    review = load(review_path)
    if (digest(review_path.read_bytes()) != provenance["private_sources_sha256"][review_path.name]
            or review["resume_final_sha256"] != provenance["private_sources_sha256"]["resume-final.json"]
            or review["fiche_relecture_sha256"] != digest((folder / "fiche-relecture.md").read_bytes())
            or set(review["verdicts"]) != {case["id"] for case in cases}
            or any(value != "conforme" for value in review["verdicts"].values()) or review["reserves"]
            or provenance["human_review"]["practitioner"] is not False or provenance["plugin_qualified"] is not False):
        raise ValueError("Relecture publique incohérente")
    return {"totals": totals, "sessions": role_count, "input_tokens": total, "stop_checks": len(expected_stops)}


def main() -> int:
    """Interface d'export local ; aucun accès modèle ou réseau."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempt", type=Path, required=True)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--review-sheet", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    args = parser.parse_args()
    try:
        result = export(args.attempt.resolve(), args.review.resolve(), args.review_sheet.resolve(), args.output, args.source_commit)
        print(json.dumps(result, ensure_ascii=True))
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as error:
        print(json.dumps({"status": "refus", "error": str(error)}, ensure_ascii=True))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
