"""Build models.json (one file with every record) so apps can download a single URL."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
models = [json.loads(f.read_text(encoding="utf-8")) for f in sorted((root / "models").rglob("*.json"))]
(root / "models.json").write_text(json.dumps({"schema": 1, "count": len(models), "models": models}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(models), "models written to models.json")
