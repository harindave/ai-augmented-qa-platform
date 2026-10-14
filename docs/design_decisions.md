# Design decisions

Updated: 14 October 2026.

This document distinguishes implemented choices from questions still open for review. Rationales below explain how the current structure supports the project; they are not a claim that every choice has been formally approved.

## 1. Define the analysis contract with Pydantic

**Status:** Implemented in `app/backend/schemas.py`.

`RequirementAnalysis` defines the expected fields, nested objects, and allowed classifications for a structured analysis response. A single contract can be used to check manually written JSON now and model responses later.

**Limit:** Passing validation proves structural compatibility, not factual correctness, useful coverage, or approval.

## 2. Use enums for classifications

**Status:** Implemented in `app/backend/models.py`.

Requirement types, risk levels, priorities, scenario types, and other classifications use fixed values. This keeps names consistent across responses and gives validation a way to reject unsupported labels.

**Tradeoff:** A fixed vocabulary may need revision when a real use case does not fit. New labels should be reviewed and added to the contract deliberately.

## 3. Keep analysis separate from workflow status

**Status:** Represented in the current models and schema; application enforcement remains future work.

Human review, requirement lifecycle, and test execution statuses have separate enums and are absent from `RequirementAnalysis`. Analysis output describes suggested findings and scenarios. Human approval and actual test results must be recorded by the appropriate workflow.

**Limit:** The current Pydantic models allow extra fields by default, so the schema does not yet reject unsolicited workflow fields.

## 4. Pair assessments with reasons

**Status:** Implemented.

Testability, overall risk, and confidence each include a classification and a reason. The explanation helps a reviewer assess the classification and challenge unsupported conclusions.

**Limit:** Confidence is qualitative; it is not a calibrated probability. The schema does not check whether a reason supports its classification.

## 5. Make uncertainty visible

**Status:** Fields implemented; reference example illustrates their use.

The contract includes quality flags, assumptions, and clarification questions. These provide places to identify missing information instead of silently treating inferred rules as confirmed requirements.

Candidate scenarios whose outcomes depend on missing rules should state what needs clarification. This convention is illustrated in the reference JSON but is not enforced by the current schema.

## 6. Learn and review JSON before model integration

**Status:** Agreed next step.

The owner will write and validate a sample response before connecting Ollama. This makes the response contract and validation errors understandable before generation adds another source of complexity.

Codex provides guidance and review; the owner implements model integration. Ollama has not been connected.

## Open decisions

- Should unknown fields be rejected at every level of the response?
- Should text fields reject blank or whitespace-only values?
- Which lists, if any, must contain at least one item?
- Should scenario `quality_flags` remain optional with an empty-list default?
- How should the application display clarification-dependent scenarios and prevent premature approval?
- Which model and response-failure handling should be used when integration begins?

Resolve these through small examples and reviewed requirements rather than treating them as already agreed changes.

## Recording a future decision

Record the date, concrete problem, chosen approach, reason, tradeoffs, implementation status, and evidence. Update an existing entry when a decision changes so the document describes the current design.
