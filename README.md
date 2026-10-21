# AI-Augmented QA Workforce Platform

A project I am building to help QA professionals analyze requirements, plan tests, and improve their technical skills.

## What works today

- A Streamlit form for entering a software requirement.
- Basic validation that rejects empty input and returns the cleaned text and character count.
- A Pydantic schema for checking structured requirement analysis.
- A sample JSON response with three test scenarios.
- A validation script that accepts a JSON file path and handles missing files and validation errors.
- A separate Ollama script that generates analysis and validates its structure.
- Automated tests for the analyzer, enums, and schema.

Local generation works in a standalone script. It is not connected to the Streamlit app yet. Model response quality and full-analysis timeouts are still under investigation.

## First-time setup

I use Python 3.13 (currently tested with 3.13.15). With Python 3.13 installed, run these commands from the project folder in PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

No environment activation is needed for the commands below because they use the virtual environment's Python directly. Ollama is installed separately for the local model prototype.

## Run the app

```powershell
.\.venv\Scripts\python.exe -m streamlit run app/main.py
```

## Check the sample JSON

```powershell
.\.venv\Scripts\python.exe -m scripts.validate_analysis docs/examples/my_requirement_analysis.json
```

A valid sample prints its summary and the number of test scenarios. Invalid data prints validation details.

## Try the local model

With Ollama installed and running, download the model once:

```powershell
ollama pull qwen2.5:1.5b
```

Then run the prototype:

```powershell
.\.venv\Scripts\python.exe -m scripts.try_ollama
```

The script currently analyzes a fixed password-reset requirement. It waits for the complete response before printing it. On my laptop, Ollama uses the CPU; full analysis has exceeded the earlier 180-second read timeout. The current settings allow 10 seconds to connect and 300 seconds to wait for response data, but a successful run with those settings has not yet been confirmed.

Generated analysis is a draft for review. Passing validation does not mean its reasoning is correct.

## Run the tests

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Where the project is going

1. **QA AI Playbook:** analyze requirements and suggest tests, risks, and clarification questions.
2. **QA Skills Lab:** practical exercises in API testing, SQL, Python, and automation.
3. **QA Evaluation Dashboard:** show test coverage, defect trends, and review results.

I am currently building the Requirement Analyzer. Next, I will investigate generation timeouts and assess output quality before connecting the model to the interface.

## How I work

I develop and test the project, using AI to help explain concepts, troubleshoot issues, and review changes. I make the implementation decisions and check the results.

The current stack is Python, Streamlit, Pydantic, requests, Ollama, and pytest. AI-generated testing suggestions require human review.

## Project notes

- [Progress and next steps](docs/project_progress.md)
- [JSON format and validation](docs/analysis_json.md)
- [Design decisions](docs/design_decisions.md)
- [Learning log](docs/learning_log.md)

This is an educational and portfolio project using synthetic examples. Do not add confidential company or client data.
