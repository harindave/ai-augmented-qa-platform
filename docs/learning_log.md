# Learning log

This log records the project owner's learning and implementation work. Codex can maintain the document, but understanding and completed exercises should be recorded only when confirmed by the owner or demonstrated in reviewed work.

## 14 October 2026 — Preparing for JSON

### Current starting point

The repository contains a basic requirement analyzer, a Streamlit interface, domain enums, Pydantic analysis models, and 26 passing tests. These are project milestones; this entry does not attribute their authorship or imply mastery of each topic.

### Agreed learning approach

The owner writes the application code and learning exercises. Codex explains concepts, suggests small steps, and reviews the work. Code edits by Codex require an explicit request; documentation maintenance is authorized.

### Next learning objective

Understand how a JSON response represents data and how the existing Pydantic schema checks its structure and allowed values.

### Planned exercise

1. Write a small JSON object containing `summary` and `requirement_types`.
2. Add the remaining required fields, including nested assessment objects and lists of scenarios.
3. Validate the response against `RequirementAnalysis`.
4. Read validation errors and correct the response.

### Progress to confirm

- JSON syntax and the relationship between JSON and Pydantic have not yet been reviewed together.
- The owner's JSON exercise has not yet been completed or reviewed.
- The existing password-reset JSON was authored by Codex as a reference.
- Ollama integration comes after the JSON exercise.

### Questions for the exercise

- When should a field contain an object rather than a list?
- Why must enum values match the schema exactly?
- What does schema validation check, and what still needs human review?
- How should missing business rules be reflected in assumptions and clarification questions?

## Template for future entries

### Date and topic

### What I implemented

### What I can explain in my own words

### Evidence or reviewed exercise

### Questions still open

### Next small step
