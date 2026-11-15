"""Validate every file in models/ against schema/model.schema.json (needs: pip install jsonschema)."""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

root = Path(__file__).resolve().parent.parent
validator = Draft202012Validator(json.loads((root / "schema" / "model.schema.json").read_text(encoding="utf-8")))
errors = 0
ids = set()
for f in sorted((root / "models").rglob("*.json")):
    data = json.loads(f.read_text(encoding="utf-8"))
    for e in validator.iter_errors(data):
        print(f"{f.relative_to(root)}: {'/'.join(map(str, e.path))}: {e.message}")
        errors += 1
    if data.get("id") in ids:
        print(f"{f.relative_to(root)}: duplicate id {data['id']}")
        errors += 1
    ids.add(data.get("id"))
    if f.name != f"{data['id'].replace('/', '__')}.json" and not f.name.startswith(data.get("platform", "") + "__"):
        print(f"{f.relative_to(root)}: file name must start with '<platform>__'")
        errors += 1
print(f"{len(ids)} models checked, {errors} problems")
sys.exit(1 if errors else 0)
