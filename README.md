# ai-model-specs

An open, community-editable database of the real limits and capabilities of AI image and video generation models.

For each model it records, when known: duration, resolutions, aspect ratios, maximum reference inputs (images / videos / audio), first and last frame support, native audio, and maximum prompt length.

## Why

Model limits are scattered across API schemas, docs and dashboards, and they change often. Most of them (especially maximum prompt length) are rarely stated anywhere. This repo keeps them in one machine-readable place, and every value says where it came from.

## How to read a value

Every field is an object with four keys:

```json
"duration_seconds": {
  "value": {"min": 4, "max": 12},
  "status": "official",
  "source": "https://replicate.com/bytedance/seedance-1-lite/api/schema",
  "date": "2026-11-15"
}
```

| status | meaning |
|---|---|
| `official` | declared by the provider's API, schema or documentation (link in `source`) |
| `tested` | measured by running the model (describe the test in the pull request) |
| `community` | reported by a contributor, with a link |
| `estimated` | a guess, shown so nobody mistakes it for a fact |

A missing field means **not declared**. It does not mean "unlimited". Only add a limit if you can point to a source or a test.

## Use the data

- `models.json`: every record in one file, easy to download.
- `models/<type>/<platform>__<model>.json`: one file per model and platform.
- `schema/model.schema.json`: JSON Schema of a record.

The same model can appear on several platforms (for example a vendor API and a reseller) with different limits, so each record belongs to one `platform`.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: edit or add a file in `models/`, run the two scripts, open a pull request with a source link.

```bash
pip install jsonschema
python scripts/validate.py
python scripts/build_index.py
```

## Seed data

The first records (2026-11-15) come from public model catalogs and schemas: OpenRouter, Replicate and Higgsfield. Only facts (numbers and capabilities) with their source are included, not documentation text. Model and provider names belong to their owners.

## License

- Data (`models/`, `models.json`): [CC BY 4.0](LICENSE-DATA.md). Please credit "ai-model-specs contributors" and link to this repository.
- Code (`scripts/`, workflows): [MIT](LICENSE).
