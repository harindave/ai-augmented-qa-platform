# Design decisions

Updated: 21 October 2026.

These notes explain the current design and the choices still open.

## Use Pydantic to check analysis responses

`RequirementAnalysis` defines the expected structure. I use it to validate both sample files and generated model responses.

Validation checks structure and allowed values. It does not judge whether the analysis is correct.

## Use fixed classifications

Enums keep labels consistent. For example, a risk level must be `Low`, `Medium`, `High`, or `Critical`.

If a new label is needed, I will update the contract deliberately rather than accept inconsistent responses.

## Keep analysis separate from approval

The analysis schema contains suggested findings and tests. Approval, requirement status, and test execution results have separate workflow enums.

The app still needs to enforce this separation. The current schema ignores extra fields rather than rejecting them.

## Explain assessments and missing information

Risk, testability, and confidence include reasons. Assumptions and clarification questions make missing information visible.

Scenario outcomes should flag unconfirmed rules instead of inventing required behavior. This is a review convention; the schema does not enforce it.

## Validate a sample before connecting a model

I completed the sample JSON and validation checks before starting model integration. This established the expected response format and exposed common errors.

Ollama is connected in `scripts/try_ollama.py`; application integration is still pending.

## Keep validation reusable

The validation code is in `scripts/validate_analysis.py`. I run it as a module from the project root so it can import the application schema.

It accepts a file path through `argparse`, catches `FileNotFoundError` and `ValidationError`, and prints results only on success. Broader file-error handling and failure exit codes are still needed for an automated pipeline.

## Start with a small local model

The prototype uses `qwen2.5:1.5b` on a laptop with about 7 GB usable RAM. Ollama reported CPU execution. This is an initial hardware-conscious choice, not a final quality decision.

The request supplies the Pydantic JSON schema and validates the returned content. System instructions and temperature zero are being evaluated, but they have not prevented reasoning errors. The first output is saved as a baseline rather than treated as approved analysis.

## Keep timeout troubleshooting separate from quality review

The prototype waits for the complete response with streaming disabled. After a 180-second read timeout, I changed the request to a 10-second connection timeout and a 300-second read timeout. Completion with these settings is not yet confirmed. A longer wait does not make generation faster or improve the answer.

## Decisions still open

- Reject unknown fields?
- Reject blank descriptions?
- Require at least one item in selected lists?
- Keep scenario quality flags optional?
- How should the interface show unresolved questions and approval?
- Is the current model adequate after evaluation, and what model-error handling is needed?

I will update these notes as those decisions are made.
