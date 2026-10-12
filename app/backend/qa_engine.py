def analyze_requirement(requirement: str) -> dict:
    """Validate a requirement and return a basic analysis."""
    cleaned_requirement = requirement.strip()

    if not cleaned_requirement:
        return {"status": "error", "message": "Requirement cannot be empty."}
    return {
        "status": "success",
        "requirement": cleaned_requirement,
        "character_count": len(cleaned_requirement),
    }
