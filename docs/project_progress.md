# Project progress

Updated: 21 October 2026.

## Completed

- Basic requirement analyzer and Streamlit interface.
- Enums and Pydantic models for structured analysis.
- Sample JSON response with three scenarios.
- Validation script with a required file-path argument, missing-file handling, and handled Pydantic errors.
- Local Ollama connection and schema-validated generation in a separate script.
- Saved first model output for comparison.
- Tests for the analyzer, enums, and schema.

The app currently checks requirement text. It does not call a model or display structured analysis.

## Checks completed

- The test run on 14 October passed all 26 tests, with a pytest cache permission warning.
- The sample JSON passed schema validation and printed the summary and `3`.
- I tested an invalid risk level, checked the handled error, and restored the valid value.
- I tested a missing file and restored the correct path.
- The configurable validator successfully checked both manual samples: three and five scenarios.
- Python successfully requested model listings, text, JSON, and full structured analysis from Ollama.

## Next tasks

- Investigate the full-analysis timeout and check runtime behavior.
- Compare model outputs for unsupported assumptions, contradictions, and instruction following.
- Add model calls and structured results to the interface after the prototype is ready.
- Add human review controls before treating generated results as approved.

The Skills Lab, dashboard, and data storage are later work.

## Known limitations

The validator accepts a file path and handles missing files, but not every file-reading error. Handled failures still return exit status zero, so it is not ready as an automated pass/fail gate. Run it from the project root for application imports; relative input paths are resolved from the working directory.

The model script uses `qwen2.5:1.5b`, temperature zero, a JSON schema, and a non-streaming response. It still uses a fixed requirement and does not catch request or validation errors. Schema-valid outputs have contained invented behavior, contradictory assessments, and more scenarios than requested. Temperature zero did not resolve these issues.

Ollama reported 100% CPU use on my laptop. A full request exceeded the 180-second read timeout. The script now uses `timeout=(10, 300)`; successful completion with that setting is not yet confirmed. An intermediate zero-second connection timeout was invalid and has been corrected.

## Key files

| File | Purpose |
|---|---|
| `app/main.py` | Streamlit interface |
| `app/backend/qa_engine.py` | Basic requirement checks |
| `app/backend/models.py` | Allowed classifications |
| `app/backend/schemas.py` | Analysis structure |
| `scripts/validate_analysis.py` | Sample validation |
| `scripts/try_ollama.py` | Local generation prototype |
| `docs/examples/first_model_analysis.json` | First generated baseline, retained with its quality issues |
| `docs/examples/my_requirement_analysis.json` | Three-scenario sample |

See the [README](../README.md) for run commands.
