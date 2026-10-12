from app.backend.qa_engine import analyze_requirement


def test_analyze_requirement_returns_character_count():
    result = analyze_requirement("User can log in.")

    assert result["status"] == "success"
    assert result["requirement"] == "User can log in."
    assert result["character_count"] == 16


def test_analyze_requirement_rejects_empty_requirement():
    result = analyze_requirement("   ")

    assert result["status"] == "error"


def test_analyze_requirement_rejects_empty_input():
    result = analyze_requirement("")

    assert result["status"] == "error"


def test_analyze_requirement_trims_whitespace():
    result = analyze_requirement("  Ignore whitespace       ")
    character_count = result["character_count"]
    assert character_count == 17

    assert result["status"] == "success"


def test_analyze_requirement_handles_special_characters():
    result = analyze_requirement("Requirement with special characters: !@#$%^&*()")
    character_count = result["character_count"]
    assert character_count == 47

    assert result["status"] == "success"


def test_analyze_requirement_handles_multiline_input():
    result = analyze_requirement("This is a requirement\nthat spans multiple lines.")
    character_count = result["character_count"]
    assert character_count == 48

    assert result["status"] == "success"


def test_analyze_requirement_handles_long_input():
    long_input = "A" * 1000  # 1000 characters of 'A'
    result = analyze_requirement(long_input)
    character_count = result["character_count"]
    assert character_count == 1000

    assert result["status"] == "success"
