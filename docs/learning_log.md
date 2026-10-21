# Learning log

I use this log to record development work, concepts practiced, and questions to revisit. AI supports explanations, troubleshooting, and review.

## 14 October 2026 - Starting the JSON work

The basic analyzer, interface, enums, schema, and initial tests were in place.

My next task was to prepare a sample analysis response and understand how JSON data maps to the Pydantic schema.

## 19 October 2026 - JSON and validation completed

### Work completed

- Built the three-scenario sample response.
- Corrected field names, commas, nested objects, and lists.
- Reviewed assumptions and outcomes that depended on missing business rules.
- Checked JSON syntax and validated the sample against `RequirementAnalysis`.
- Moved the validation code into a reusable script.
- Fixed the import issue by running the script as a module.
- Added `try` / `except` / `else` to handle validation errors.
- Corrected indentation so success output only runs after valid input.

### Key takeaways

- Valid JSON can still fail the project schema.
- Field names and enum values must match exactly.
- Imports bring the required classes into the script.
- Failed validation does not create the `analysis` object.
- Schema checks cannot confirm business rules or approve results.

### Checks completed

The valid sample printed its summary and `3`. I also tested `Extreme` as an invalid risk level, checked that the error was handled, and restored `High`.

### Next steps

I continued with missing-file handling, command-line input, and local model experiments, recorded below.

## 20-21 October 2026 - Local model prototype

### Work completed

- Added missing-file handling and kept file reading and validation inside one `try` block.
- Added a required file-path argument with `argparse` and checked both manual JSON samples.
- Installed Ollama and downloaded `qwen2.5:1.5b`.
- Connected Python to Ollama using `requests`.
- Progressed from model listing to text, JSON, and schema-validated analysis.
- Saved the first generated analysis as a baseline.
- Compared fresh conversations, system instructions, and temperature zero.

### What I found

The model can return valid structured data while inventing business rules or contradicting its own assessments. Clearer instructions helped in some runs but did not make the output reliable. Human review remains necessary.

Ollama reported 100% CPU execution. Full analysis exceeded a 180-second read timeout. I increased it to `timeout=(10, 300)` for diagnosis and corrected an accidental zero connection timeout. A completed run with the corrected setting is still unconfirmed.

### Next steps

Investigate generation time and output quality before connecting the prototype to Streamlit. The model script still needs handled connection, timeout, and invalid-response errors. The validator still needs failure exit codes before automated pipeline use.

## Future entry format

- Date and task
- What I changed
- What I checked
- What I learned
- Questions and next steps
