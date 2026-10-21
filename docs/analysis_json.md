# Requirement analysis JSON

Updated: 21 October 2026.

JSON is the format for the analysis response. The Pydantic model in `app/backend/schemas.py` defines the fields and values the project expects.

## Examples

- [Working sample](examples/my_requirement_analysis.json): password reset requirement with three scenarios.
- [Additional reference](examples/password_reset_analysis.json): email-based password reset with five scenarios.

Both are manually prepared examples, not model output or approved specifications.

- [First model analysis](examples/first_model_analysis.json): saved generated output with known reasoning problems. This is a comparison baseline, not an approved answer.

## Main fields

| Field | What it contains |
|---|---|
| `summary` | Short description of the requirement |
| `requirement_types` | Classifications such as Functional and Security |
| `testability` | Whether it can be tested, with a reason |
| `overall_risk` | Overall risk level and reason |
| `risks` | Individual risks |
| `quality_flags` | Problems such as missing information |
| `edge_cases` | Unusual situations to consider |
| `dependencies` | Capabilities the feature needs |
| `assumptions` | Unconfirmed information used in the analysis |
| `clarification_questions` | Questions about missing details |
| `test_scenarios` | Candidate tests and expected outcomes |
| `confidence` | Qualitative confidence level and reason |

Each scenario needs `title`, `scenario_type`, `category`, `description`, `priority`, and `expected_outcome`. Its optional `quality_flags` defaults to an empty list.

Field names are case-sensitive. Enum values must match the allowed values in `app/backend/models.py`.

## Validate the working sample

Run from the project root:

```powershell
.\.venv\Scripts\python.exe -m json.tool docs/examples/my_requirement_analysis.json
.\.venv\Scripts\python.exe -m scripts.validate_analysis docs/examples/my_requirement_analysis.json
```

The first command checks JSON syntax. The second checks the project schema. A successful script run prints the summary and `3`.

Use the module command above rather than the editor's Run Python File button, which can fail to find the `app` package.

## What I checked

I tested an invalid risk level by changing `High` to `Extreme`. Pydantic identified the field and listed the allowed values. The script handled the error without an unhandled traceback. I then restored `High`.

The script accepts a required file path using `argparse`. It reads and validates inside one `try` block, handles missing files with `except FileNotFoundError`, handles schema errors with `except ValidationError`, and prints results only in `else`. I checked both manual samples and the missing-file path.

To validate the additional reference, change the argument:

```powershell
.\.venv\Scripts\python.exe -m scripts.validate_analysis docs/examples/password_reset_analysis.json
```

## Generated JSON

`scripts/try_ollama.py` sends `RequirementAnalysis.model_json_schema()` to Ollama and checks the returned text with `RequirementAnalysis.model_validate_json()`.

The model has produced schema-valid answers with unsupported rules, conflicting assessments, and incorrect scenario counts. Those need content review; structural validation alone will not catch them. Full generation currently also has unresolved timeout issues.

## What validation does not prove

Passing validation does not mean the analysis is accurate, complete, or approved. Missing business rules still need clarification. The current schema also permits extra fields, empty strings, and empty lists.

Approval and actual test results belong in the application workflow, not in the analysis response.
