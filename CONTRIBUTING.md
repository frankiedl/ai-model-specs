# Contributing

1. Edit or add one file in `models/<type>/`, named `<platform>__<model>.json`.
2. For every value set `source` (exact URL, or the test you ran), today's `date`, and an honest `status`.
3. Never invent values. If a limit is not declared, leave the field out.
4. Run `python scripts/validate.py` and `python scripts/build_index.py`.
5. Open a pull request using the template.

`prompt_max` is written as `{"value": 4000, "unit": "characters"}` (`characters`, `words` or `tokens`).

Add facts only: do not copy documentation text or code from other projects.

By contributing you agree that your data is released under CC BY 4.0 and your code under MIT.
