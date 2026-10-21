import requests
from app.backend.schemas import RequirementAnalysis

print("Waiting for Ollama to generate the analysis...", flush=True)
response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "qwen2.5:1.5b",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a QA analyst. Analyze only the supplied requirement. "
                    "Separate stated facts from assumptions. "
                    "Assess testability based on whether expected behavior is clear "
                    "enough to verify; requirements can be assessed for testability. "
                    "Explain risks using potential failures and their consequences. "
                    "Do not invent steps, policies, or dependencies. "
                    "Never require or retrieve the old password for forgotten-password recovery. "
                    "Use each quality flag only once. "
                    "Make test scenarios concrete and identify outcomes that require clarification. "
                    "Base confidence on the available evidence and unresolved questions."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Analyze this requirement: Users can reset their password. "
                    "Return a complete JSON analysis matching the supplied schema. "
                    "Include one test scenario. "
                    "Do not invent a recovery method or password policy. "
                    "Record missing details as clarification questions and mark "
                    "outcomes that depend on them as requiring clarification. "
                    "Do not require or retrieve the old password."
                ),
            },
        ],
        "stream": False,
        "options": {
            "temperature": 0,
        },
        "format": RequirementAnalysis.model_json_schema(),
    },
    timeout=(10, 300),
)
response.raise_for_status()
content = response.json()["message"]["content"]
analysis = RequirementAnalysis.model_validate_json(content)

print(analysis.summary)
print(analysis.model_dump_json(indent=2))
