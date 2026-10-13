from app.backend.models import (
    RequirementType,
    RiskLevel,
    RiskCategory,
    PriorityLevel,
    TestabilityStatus,
    ConfidenceLevel,
    QualityFlag,
    ScenarioType,
    TestLevel,
    TestCategory,
    TestApproach,
    TestDesignTechnique,
    TestPurpose,
)


def test_requirement_types():
    assert RequirementType.FUNCTIONAL.value == "Functional"
    assert RequirementType.SECURITY.value == "Security"
    assert RequirementType.PERFORMANCE.value == "Performance"
    assert RequirementType.USABILITY.value == "Usability"
    assert RequirementType.ACCESSIBILITY.value == "Accessibility"
    assert RequirementType.COMPATIBILITY.value == "Compatibility"
    assert RequirementType.RELIABILITY.value == "Reliability"
    assert RequirementType.COMPLIANCE.value == "Compliance"
    assert RequirementType.UI_UX.value == "UI/UX"
    assert RequirementType.INTEGRATION.value == "Integration"
    assert RequirementType.DATA.value == "Data"
    assert RequirementType.BUSINESS_RULE.value == "Business Rule"
    assert RequirementType.REPORTING.value == "Reporting"
    assert RequirementType.NON_FUNCTIONAL_OTHER.value == "Non-Functional (Other)"


def test_risk_levels():
    assert RiskLevel.LOW.value == "Low"
    assert RiskLevel.MEDIUM.value == "Medium"
    assert RiskLevel.HIGH.value == "High"
    assert RiskLevel.CRITICAL.value == "Critical"


def test_risk_categories():
    assert RiskCategory.SECURITY.value == "Security"
    assert RiskCategory.DATA_LOSS.value == "Data Loss"
    assert RiskCategory.FINANCIAL.value == "Financial"
    assert RiskCategory.COMPLIANCE.value == "Compliance"
    assert RiskCategory.PERFORMANCE.value == "Performance"
    assert RiskCategory.USER_EXPERIENCE.value == "User Experience"
    assert RiskCategory.INTEGRATION.value == "Integration"
    assert RiskCategory.RELIABILITY.value == "Reliability"


def test_priority_levels():
    assert PriorityLevel.LOW.value == "Low"
    assert PriorityLevel.MEDIUM.value == "Medium"
    assert PriorityLevel.HIGH.value == "High"
    assert PriorityLevel.CRITICAL.value == "Critical"


def test_testability_status():
    assert TestabilityStatus.TESTABLE.value == "Testable"
    assert TestabilityStatus.PARTIALLY_TESTABLE.value == "Partially Testable"
    assert TestabilityStatus.NOT_TESTABLE.value == "Not Testable"


def test_confidence_levels():
    assert ConfidenceLevel.LOW.value == "Low"
    assert ConfidenceLevel.MEDIUM.value == "Medium"
    assert ConfidenceLevel.HIGH.value == "High"


def test_quality_flags():
    assert QualityFlag.AMBIGUOUS.value == "Ambiguous"
    assert QualityFlag.INCOMPLETE.value == "Incomplete"
    assert QualityFlag.CONFLICTING.value == "Conflicting"
    assert QualityFlag.UNTESTABLE.value == "Untestable"
    assert QualityFlag.DUPLICATE.value == "Duplicate"


def test_scenario_types():
    assert ScenarioType.POSITIVE.value == "Positive"
    assert ScenarioType.NEGATIVE.value == "Negative"
    assert ScenarioType.BOUNDARY.value == "Boundary"
    assert ScenarioType.EDGE_CASE.value == "Edge Case"
    assert ScenarioType.RECOVERY.value == "Recovery"


def test_test_levels():
    assert TestLevel.UNIT.value == "Unit"
    assert TestLevel.INTEGRATION.value == "Integration"
    assert TestLevel.SYSTEM.value == "System"


def test_test_categories():
    assert TestCategory.FUNCTIONAL.value == "Functional"
    assert TestCategory.PERFORMANCE.value == "Performance"
    assert TestCategory.SECURITY.value == "Security"
    assert TestCategory.USABILITY.value == "Usability"
    assert TestCategory.ACCESSIBILITY.value == "Accessibility"
    assert TestCategory.COMPATIBILITY.value == "Compatibility"
    assert TestCategory.DATA_VALIDATION.value == "Data Validation"
    assert TestCategory.API.value == "API"


def test_test_approaches():
    assert TestApproach.BLACK_BOX.value == "Black Box"
    assert TestApproach.WHITE_BOX.value == "White Box"
    assert TestApproach.GREY_BOX.value == "Grey Box"


def test_test_design_techniques():
    assert (
        TestDesignTechnique.EQUIVALENCE_PARTITIONING.value == "Equivalence Partitioning"
    )
    assert (
        TestDesignTechnique.BOUNDARY_VALUE_ANALYSIS.value == "Boundary Value Analysis"
    )
    assert TestDesignTechnique.DECISION_TABLE.value == "Decision Table"
    assert TestDesignTechnique.STATE_TRANSITION.value == "State Transition"
    assert TestDesignTechnique.ERROR_GUESSING.value == "Error Guessing"
    assert TestDesignTechnique.USE_CASE.value == "Use Case"


def test_test_purposes():
    assert TestPurpose.SMOKE.value == "Smoke"
    assert TestPurpose.SANITY.value == "Sanity"
    assert TestPurpose.REGRESSION.value == "Regression"
    assert TestPurpose.EXPLORATORY.value == "Exploratory"
    assert TestPurpose.RETEST.value == "Retest"


def test_enum_str_conversion():
    assert str(RequirementType.FUNCTIONAL) == "Functional"
    assert str(RiskLevel.HIGH) == "High"
    assert str(TestCategory.SECURITY) == "Security"
    assert str(PriorityLevel.CRITICAL) == "Critical"
