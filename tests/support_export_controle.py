"""Diagnostic synthétique complet d'export : aucun modèle ni avis réel de Jo."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import json
import shutil
import subprocess
import uuid

import controle_stop
import eval_suite
import export_mesure_controlee as export
import mesure_locale


def save(path: Path, value: dict) -> None:
    """Écrit les seuls octets synthétiques du diagnostic."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(export.encoded(value))


def diagnostic(root: Path, verdicts: dict[str, str] | None = None,
               reserves: dict[str, str] | None = None) -> dict:
    """Construit 56 traces factices vérifiables par les contrôles réels d'export."""
    commit = subprocess.check_output(
        ["git", "-c", "safe.directory=" + str(export.ROOT), "-C", str(export.ROOT), "rev-parse", "HEAD"]
    ).decode().strip()
    plan_dir = root / "mesure"
    attempt = plan_dir / "diagnostic-dcp-015"
    prepared, kit = attempt / "prepare", attempt / "kit"
    eval_suite.prepare_run(prepared, "SIMULATION répondant", "SIMULATION juge")
    mesure_locale.export_kit(kit, prepared)
    cases = mesure_locale.verify_kit(kit)
    result = kit / "resultats"
    settings = {"engine": "codex", "cli_version": "codex-cli 0.163.0-alpha.10.2",
                "responder_model": "gpt-6.1-sol", "judge_model": "gpt-6.1-sol", "web": True}
    roles, checks = [], []
    for case in cases:
        folder = result / case["id"]
        header = controle_stop.expected_header(case)
        response = ((header + "\n") if header else "") + "SIMULATION LOGICIELLE : aucune réponse réelle, aucun avis de Jo.\n"
        (folder / "response.md").write_text(response, encoding="utf-8", newline="\n")
        selected = (verdicts or {}).get(case["id"], "RÉUSSITE")
        save(folder / "judgment.json", {"verdict": selected, "notes": "SIMULATION, aucune mesure du skill.",
                                       "response_sha256": export.digest((folder / "response.md").read_bytes())})
        for role, output in (("respondant", "response.md"), ("juge", "judgment.json")):
            thread = str(uuid.uuid4())
            usage = {"input_tokens": 10, "cached_input_tokens": 3, "output_tokens": 2}
            events = [{"type": "thread.started", "thread_id": thread},
                      {"type": "turn.completed", "usage": usage}]
            stdout = "".join(json.dumps(event) + "\n" for event in events).encode()
            (folder / (role + "-stdout.txt")).write_bytes(stdout)
            (folder / (role + "-stderr.txt")).write_bytes(b"")
            payload = mesure_locale.input_for(kit, case, role, "codex")
            save(folder / (role + "-execution.json"), {
                "engine": "codex", "cli_version": settings["cli_version"], "role": role,
                "requested_model": "gpt-6.1-sol", "web_requested": role == "respondant",
                "fresh_process": True, "fresh_workspace": True,
                "skill_entry_supplied": role == "respondant", "native_skill_present": role == "respondant",
                "input_sha256": export.digest(payload.encode()), "output_sha256": export.digest((folder / output).read_bytes()),
                "raw_stdout_sha256": export.digest(stdout), "raw_stderr_sha256": export.digest(b""), "tokens": usage,
            })
            roles.append({"case_id": case["id"], "role": role, "thread_id": thread, "usage": usage,
                          "status": "completed", "process_exit": 0, "usage_complete": True})
        if header:
            check = controle_stop.audit_run(result, [case["id"]])
            save(folder / "controle-stop.json", check)
            checks.append({"case_id": case["id"], "passed": True,
                           "path": "kit/resultats/" + case["id"] + "/controle-stop.json",
                           "sha256": export.digest((folder / "controle-stop.json").read_bytes())})
    totals = eval_suite.validate_run(result)
    summary_path = eval_suite.write_summary(result, totals)
    (root / "PLAN-MESURE-D0.md").write_text("SIMULATION LOCALE, aucun modèle ni avis humain réel.\n", encoding="utf-8")
    save(root / "preuves/SCELLEMENT-D0.json", {"simulation": True, "files": {}})
    plan_sha = export.digest((root / "PLAN-MESURE-D0.md").read_bytes())
    seal_sha = export.digest((root / "preuves/SCELLEMENT-D0.json").read_bytes())
    manifest = export.load(result / "manifest.json")
    plan = {"simulation": True, "candidate_commit": commit, "attempt_id": attempt.name,
            "plan_d0_sha256": plan_sha, "seal_d0_sha256": seal_sha,
            "models": {"respondant": "gpt-6.1-sol", "juge": "gpt-6.1-sol"},
            "requested_cli": {"path": "CLI_NON_EXECUTEE", "version": settings["cli_version"]},
            "runtime_sha256": manifest["runtime_sha256"]}
    auth = {"simulation": True, "candidate_commit": commit, "attempt_id": attempt.name,
            "plan_d0_sha256": plan_sha, "seal_d0_sha256": seal_sha,
            "measurement_authorized": True, "budget_policy": "between_roles", "max_input_tokens": 10_000_000,
            "max_sessions": 56}
    save(plan_dir / "PLAN-D1.json", plan)
    save(plan_dir / "autorisation-jo.json", auth)
    launcher = {"files": {name: {"sha256": export.digest((plan_dir / name).read_bytes()),
                                "octets": (plan_dir / name).stat().st_size}
                          for name in ("PLAN-D1.json", "autorisation-jo.json")}}
    save(plan_dir / "MANIFESTE-LANCEUR-D1.json", launcher)
    controller = {"simulation": True, "head": commit, "attempt_id": attempt.name,
                  "plan_d0_sha256": plan_sha, "seal_d0_sha256": seal_sha,
                  "launcher_manifest_sha256": export.digest((plan_dir / "MANIFESTE-LANCEUR-D1.json").read_bytes()),
                  "status": "completed", "failure": None, "input_tokens_complete": True,
                  "sessions_started": 56, "input_tokens_limit": 10_000_000, "input_tokens_total_known": 560,
                  "roles": roles, "stop_header_checks": checks,
                  "upstream_summary": {"path": "kit/resultats/summary.json", "sha256": export.digest(summary_path.read_bytes()),
                                       "value": export.load(summary_path)}}
    save(attempt / "resume-final.json", controller)
    sheet = root / "fiche-simulee.md"
    sheet.write_text("SIMULATION : aucune relecture réelle de Jo.\n", encoding="utf-8")
    review = {"simulation": True, "decideur": "Jo", "date_utc": "2026-10-23T12:00:00+00:00",
              "source": "SIMULATION LOGICIELLE, aucun avis réel de Jo.", "tete": commit, "tentative": attempt.name,
              "resume_final_sha256": export.digest((attempt / "resume-final.json").read_bytes()),
              "fiche_relecture_sha256": export.digest(sheet.read_bytes()),
              "verdicts": {case["id"]: "en réserve" if case["id"] in (reserves or {}) else "conforme" for case in cases},
              "reserves": deepcopy(reserves or {})}
    review_path = root / "avis-simule.json"
    save(review_path, review)
    return {"attempt": attempt, "review_path": review_path, "review_sheet": sheet,
            "output": root / "public", "commit": commit, "review_date": "2026-10-23"}
