# AI-Augmented QA Workforce Platform

An AI-assisted quality engineering platform designed to help QA professionals improve testing efficiency, develop technical skills, and demonstrate measurable software quality.

## Vision

Build a practical platform that combines AI-assisted testing, human review, guided learning, and quality analytics.

The goal is to augment QA engineers, not replace them.

## Core Modules

### 1. QA AI Playbook
- Analyze software requirements and acceptance criteria.
- Generate draft test scenarios and test cases.
- Identify potential edge cases and risks.
- Support human review and approval of AI-generated outputs.

### 2. QA Skills Lab
- Provide practical exercises in API testing, SQL, Python, automation, and AI-assisted testing.
- Track learning progress and demonstrated skills.
- Encourage continuous professional development.

### 3. QA Evaluation Dashboard
- Visualize test coverage, defect trends, and testing outcomes.
- Track AI-assisted testing quality and review results.
- Support team-level learning and continuous improvement.

## Technology Stack

- Python
- Streamlit
- Ollama for local AI inference
- SQLite
- Pandas and SQL
- pytest
- Postman
- Selenium
- GitHub Actions

Python, Streamlit, Pydantic, and pytest are used in the current prototype. Ollama integration, persistence, learning modules, dashboards, and continuous integration are planned work. The remaining tools will be introduced incrementally.

## Development Principles

- Human review for AI-generated testing outputs.
- Privacy-conscious development using synthetic sample data.
- Automated testing and measurable quality checks.
- Small, understandable changes with version control.
- Clear documentation of limitations and design decisions.

## Project Status

**Phase 1 — Requirement Analyzer prototype (in progress)**

Completed:
- Repository foundation and local Python environment.
- Streamlit requirement input interface.
- Basic requirement validation: reject empty input, trim whitespace, and return a character count.
- Domain enums for analysis classifications and separate human/system workflow statuses.
- Pydantic models defining a structured requirement analysis response.
- Automated tests for the basic analyzer, enums, and schema.

The current app performs basic text validation only. It does not yet generate AI analysis. The schema defines the intended output structure; it is not connected to the analyzer or a model.

Next: learn and review JSON, write a sample response, and validate it against the schema. Connect Ollama after that exercise is understood and reviewed. The existing [sample JSON guide](docs/analysis_json.md) is an optional reference authored by Codex, not a completed learner exercise.

## Working Approach

The project owner writes the application code. Codex guides the work by explaining concepts, suggesting small steps, and reviewing the owner's implementation. Codex edits code only when explicitly asked. Documentation updates can be requested separately.

## Run Locally

From the project root in PowerShell, with the virtual environment and dependencies installed:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app/main.py
```

Run the tests:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

`.env.example` records planned model configuration. The current app does not load it or call Ollama.

See [project progress and next steps](docs/project_progress.md) for the current handoff.

The [learning log](docs/learning_log.md) tracks exercises and understanding, and [design decisions](docs/design_decisions.md) records implemented choices and open questions.

## Roadmap

1. Establish the project foundation — completed.
2. Build the first working QA AI Playbook prototype — basic interface and analysis schema completed; JSON learning and model integration next.
3. Add human review and strengthen output validation — schema validation exists; review workflow and model-response handling remain planned.
4. Build the QA Skills Lab.
5. Develop the QA Evaluation Dashboard.
6. Connect the modules through a controlled AI workflow.
7. Expand automated tests and add continuous integration — initial tests already exist.
8. Publish a documented, reproducible demonstration.

## Disclaimer

This is an educational and portfolio project. Initial examples will use synthetic data and will not contain confidential company or client information.
