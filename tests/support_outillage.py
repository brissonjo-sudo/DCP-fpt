"""Fixtures temporaires de scripts ; aucun cas métier ni mesure du skill."""

import json
from pathlib import Path


def fixture_cases(directory: Path) -> Path:
    """Produit des entrées sans droit, exclusivement dans un dossier de test."""
    cases = [{"id": f"cas-{n:02d}", "branche": "fixture-logicielle",
              "type": "critique" if n >= 21 else "standard",
              "prompt": f"Entrée factice de test logiciel {n}. Aucun cas métier.",
              "attendus": ["Sortie factice de test logiciel uniquement."]}
             for n in range(1, 29)]
    path = directory / "suite-factice.json"
    path.write_text(json.dumps(cases, ensure_ascii=False), encoding="utf-8", newline="\n")
    return path
