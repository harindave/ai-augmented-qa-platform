from pathlib import Path
from app.backend.schemas import RequirementAnalysis
from pydantic import ValidationError
import argparse

parser = argparse.ArgumentParser(
    description="Validate a requirement analysis JSON file."
)
parser.add_argument("file_path", help="Path to the JSON file to validate")
args = parser.parse_args()

try:
    json_text = Path(args.file_path).read_text(encoding="utf-8")
    analysis = RequirementAnalysis.model_validate_json(json_text)

except FileNotFoundError:
    print("Analysis file not found. Check the file path.")
except ValidationError as error:
    print("Analysis validation failed:")
    print(error)
else:
    print(analysis.summary)
    print(len(analysis.test_scenarios))
