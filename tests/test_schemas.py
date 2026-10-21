from app.backend.models import (
    ConfidenceLevel,
    PriorityLevel,
    RequirementType,
    RiskCategory,
    RiskLevel,
    ScenarioType,
    TestCategory,
    TestabilityStatus,
)

from app.backend.schemas import (
    ConfidenceAssessment,
    RequirementAnalysis,
    Risk,
    RiskAssessment,
    TestabilityAssessment,
    TestScenario,
)

from pydantic import ValidationError
import pytest


def test_valid_requirement_analysis():
    analysis = RequirementAnalysis(
        summary="Users can reset their password using their registered email.",
        requirement_types=[
            RequirementType.FUNCTIONAL,
            RequirementType.SECURITY,
        ],
        testability=TestabilityAssessment(
            status=TestabilityStatus.PARTIALLY_TESTABLE,
            reason="Reset-link expiry is not specified.",
        ),
        overall_risk=RiskAssessment(
            level=RiskLevel.HIGH,
            reason="Password reset affects account security.",
        ),
        risks=[
            Risk(
                category=RiskCategory.SECURITY,
                level=RiskLevel.HIGH,
                description="Reset links could potentially be reused.",
            )
        ],
        quality_flags=[],
        edge_cases=[
            "Multiple password reset requests",
            "Expired reset link",
        ],
        dependencies=[
            "Email delivery service",
        ],
        assumptions=[
            "The user already has a registered account.",
        ],
        clarification_questions=[
            "How long should the reset link remain valid?",
        ],
        test_scenarios=[
            TestScenario(
                title="Reset password using registered email",
                description=(
                    "Verify that a registered user can request a password reset "
                    "using their registered email address."
                ),
                scenario_type=ScenarioType.POSITIVE,
                category=TestCategory.FUNCTIONAL,
                priority=PriorityLevel.HIGH,
                expected_outcome="Password reset instructions are sent.",
            )
        ],
        confidence=ConfidenceAssessment(
            level=ConfidenceLevel.HIGH,
            reason="The main user flow is clearly stated.",
        ),
    )
    assert analysis.overall_risk.level == RiskLevel.HIGH
    assert len(analysis.test_scenarios) == 1
    assert analysis.test_scenarios[0].priority == PriorityLevel.HIGH


def test_invalid_requirement_analysis():
    with pytest.raises(ValidationError):
        Risk(
            category=RiskCategory.SECURITY,
            level="Extremely Dangerous",
            description="This AI assessment is invalid.",
        )


def test_invalid_scenario_priority_is_rejected():
    with pytest.raises(ValidationError):
        TestScenario(
            title="Reset password",
            description="Verify password reset.",
            scenario_type=ScenarioType.POSITIVE,
            category=TestCategory.FUNCTIONAL,
            priority="Urgent",
            expected_outcome="Password reset succeeds.",
        )


def test_invalid_requirement_type_is_rejected():
    with pytest.raises(ValidationError) as error:
        RequirementAnalysis(
            summary="Users can reset their password.",
            requirement_types=["Magic Requirement"],
            testability=TestabilityAssessment(
                status=TestabilityStatus.TESTABLE,
                reason="The requirement can be tested.",
            ),
            overall_risk=RiskAssessment(
                level=RiskLevel.MEDIUM,
                reason="Password reset affects account access.",
            ),
            risks=[],
            quality_flags=[],
            edge_cases=[],
            dependencies=[],
            assumptions=[],
            clarification_questions=[],
            test_scenarios=[],
            confidence=ConfidenceAssessment(
                level=ConfidenceLevel.HIGH,
                reason="The requirement is understandable.",
            ),
        )

    errors = error.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("requirement_types", 0)
    assert errors[0]["type"] == "enum"


def test_missing_risk_description_is_rejected():
    with pytest.raises(ValidationError):
        Risk(
            category=RiskCategory.SECURITY,
            level=RiskLevel.HIGH,
        )
