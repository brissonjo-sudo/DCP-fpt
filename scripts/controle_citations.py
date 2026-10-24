"""Signale chaque chemin de skill pour Jo, sans modifier jugement ou score.

Alignement : collectivite-territoriale#23, scripts/skill_citation.py,
commit 94de5ee4bea2b28d47d07e344c2ee6f83fb36ccd. Les cibles de ressources
restent signalées quel que soit leur hôte ; les URL officielles ordinaires
restent permises. Ajout : inventaire des occurrences et chemins locaux absolus.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

import eval_suite

RESOURCE = re.compile(r"(?:\bSKILL\.md\b|(?:references|objets)/|\.agents/skills/)", re.I)
HTTP_URL = re.compile(r"https?://[^\s<>`\)]+", re.I)
LINK = re.compile(r"\[[^\]\n]*\]\(\s*(<?[^)\n]+>?)\)")
LOCAL = re.compile(
    r"(?<![\w/])(?:file:/+|[A-Z]:/|//[^\s/]+/|/(?!/)[\w.~-])[^\s`<>\)\]]*",
    re.I,
)
RELATIVE = re.compile(
    r"(?<![\w-])(?:[\w./~-]+/)?(?:SKILL\.md\b|(?:references|objets)/[^\s`<>\)\]]*|"
    r"\.agents/skills/[^\s`<>\)\]]*)", re.I,
)


def occurrences(text: str) -> list[dict]:
    """Inventorie sans exposer les chemins ; positions dans chaque ligne décodée.

    Décodage URL et séparateurs identiques au contrôle amont. Un lien compte
    une fois, même si plusieurs motifs recouvrent sa cible. Deux occurrences
    distinctes sur la même ligne restent distinctes. Aucune liste blanche d'hôte
    ne peut dissimuler une ressource de skill.
    """
    results = []
    for line_number, raw in enumerate(text.splitlines(), 1):
        line = unquote(raw).replace("\\", "/")
        spans: list[tuple[int, int, str]] = []

        def add(start: int, end: int, kind: str) -> None:
            if not any(start < old_end and end > old_start for old_start, old_end, _ in spans):
                spans.append((start, end, kind))

        for match in LINK.finditer(line):
            target = match[1].strip("<> ")
            if RESOURCE.search(target) or LOCAL.match(target):
                add(match.start(1), match.end(1), "lien_skill_ou_local")
        masked = list(line)
        for match in HTTP_URL.finditer(line):
            if RESOURCE.search(match[0]):
                add(match.start(), match.end(), "url_ressource_skill")
            masked[match.start():match.end()] = " " * len(match[0])
        without_urls = "".join(masked)
        for pattern, kind in ((LOCAL, "chemin_absolu_local"), (RELATIVE, "chemin_skill")):
            for match in pattern.finditer(without_urls):
                add(match.start(), match.end(), kind)
        results.extend({"line": line_number, "column_normalized": start + 1,
                        "end_column_normalized": end + 1, "kind": kind}
                       for start, end, kind in sorted(spans))
    return results


def check_response(case_id: str, raw: bytes) -> dict:
    """Lie les alertes aux octets de la réponse, sans recopier une donnée privée."""
    found = occurrences(raw.decode("utf-8"))
    return {"case_id": case_id, "response_sha256": hashlib.sha256(raw).hexdigest(),
            "occurrence_count": len(found), "occurrences": found,
            "review_required": bool(found), "verdict_modified": False}


def audit_run(run_dir: Path, case_ids: list[str] | None = None) -> dict:
    """Vérifie les entrées figées et tous les prompts avant audit en lecture seule."""
    manifest = json.loads((run_dir / "manifest.json").read_bytes())
    suite, rubric = run_dir / "suite.json", run_dir / "bareme.md"
    if (eval_suite.suite_digest(suite) != manifest["suite_sha256"]
            or eval_suite.suite_digest(rubric) != manifest["rubric_sha256"]):
        raise ValueError("Suite ou barème figé altéré")
    cases = eval_suite.load_cases(suite)
    if manifest["case_count"] != len(cases):
        raise ValueError("Nombre de cas incohérent")
    if case_ids and not set(case_ids) <= {case["id"] for case in cases}:
        raise ValueError("Cas inconnu")
    checks = []
    for case in cases:
        if case_ids and case["id"] not in case_ids:
            continue
        folder = run_dir / eval_suite.case_dir_name(case)
        if (folder / "prompt.md").read_text(encoding="utf-8") != case["prompt"] + "\n":
            raise ValueError(f"{case['id']} : prompt altéré")
        checks.append(check_response(case["id"], (folder / "response.md").read_bytes()))
    return {"contract": "citation-skill-informative-v1", "checks": checks,
            "occurrence_count": sum(check["occurrence_count"] for check in checks),
            "responses_with_occurrences": sum(check["review_required"] for check in checks),
            "suite_sha256": manifest["suite_sha256"], "rubric_sha256": manifest["rubric_sha256"],
            "scope": "information pour Jo ; aucun verdict ni score modifié"}


def main() -> int:
    """Code 0 même avec alertes ; code 2 si les preuves sont inexploitables."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--cases", nargs="+")
    args = parser.parse_args()
    try:
        result = audit_run(args.run_dir.resolve(), args.cases)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=True))
        return 2
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
