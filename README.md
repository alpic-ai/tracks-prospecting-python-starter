# Python prospecting automation starter

A small Python 3.11+ CLI for building a B2B prospect list and exporting contact data.

The CLI, request validation and CSV writer are implemented. The live provider adapter in `prospecting/provider.py` is intentionally unfinished: an agent must implement it using the provider selected in the task.

## Run

```sh
python -m prospecting --help
python -m unittest discover -s tests -v
python -m prospecting --countries France Germany --industry "Software Development" --min-employees 51 --max-employees 500 --roles "Head of Sales" "VP of Sales" --limit 12 --output results/prospects.csv
```

Until the adapter is implemented, the last command exits with an explicit error and produces no CSV. This is expected starter behavior.

## Implementation boundaries

- Keep credentials in environment variables; never commit or print them.
- Use live provider data for the task. Test fixtures are synthetic and must never be presented as real contacts.
- Preserve provider-reported uncertainty and unsuccessful lookups.
- The task's user instructions control the preview, spending approval and requested output.
- Keep the existing CSV columns and add tests for the integration you implement.
- Local unit tests exercise the scaffold only; passing them is not evidence of a successful live integration.

No provider-specific package or integration instructions are preinstalled.
