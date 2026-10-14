# Requirement analysis JSON example

## Learning status

JSON learning and the owner's own sample response are the next tasks. Codex authored this reference example before the working roles were clarified. Its successful validation demonstrates that the example fits the existing schema; it does not mean the owner has completed the JSON exercise.

The owner will write the code and sample JSON, with Codex providing explanations and review. Model integration follows the JSON exercise and will be implemented by the owner.

## Reference example

Source requirement: **Users can reset their password using their registered email.**

See [the example response](examples/password_reset_analysis.json). This is a manually authored draft for reviewing the output contract, not a model-generated analysis or an approved specification.

The JSON matches `RequirementAnalysis` in `app/backend/schemas.py`. Field names and enum values must match the schema exactly. All top-level fields are required; lists can be empty. Scenario `quality_flags` defaults to an empty list when omitted, but is included explicitly in this example.

## Reading the output

- `summary` and `requirement_types` describe the requirement.
- `testability`, `overall_risk`, and `confidence` each pair a classification with its reason.
- `risks` list individual risks with a category, severity, and description.
- `quality_flags` identify problems in the source requirement.
- `edge_cases`, `dependencies`, `assumptions`, and `clarification_questions` make gaps and inferred context visible.
- `test_scenarios` describe candidate tests, their priority, and expected outcomes. Outcomes that depend on missing rules explicitly require clarification.

Human approval, requirement lifecycle, and test execution statuses belong to the application workflow and are not part of this analysis JSON.

Schema validation checks structure and allowed values. It does not establish factual accuracy, test completeness, or human approval. The current schema also allows extra fields by default and accepts empty strings; stricter validation can be considered when reviewing this contract.

## Validate the example

Run from the project root:

```powershell
.\.venv\Scripts\python.exe -c "from pathlib import Path; from app.backend.schemas import RequirementAnalysis; result = RequirementAnalysis.model_validate_json(Path('docs/examples/password_reset_analysis.json').read_text(encoding='utf-8')); print('Valid analysis:', len(result.test_scenarios), 'scenarios')"
```
