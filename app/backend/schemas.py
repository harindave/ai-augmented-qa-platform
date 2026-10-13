from pydantic import BaseModel, Field

from app.backend.models import (
    ConfidenceLevel,
    PriorityLevel,
    QualityFlag,
    RequirementType,
    RiskCategory,
    RiskLevel,
    ScenarioType,
    TestCategory,
    TestabilityStatus,
)


class Risk(BaseModel):
    category: RiskCategory
    level: RiskLevel
    description: str


class RiskAssessment(BaseModel):
    level: RiskLevel
    reason: str


class TestabilityAssessment(BaseModel):
    __test__ = False
    status: TestabilityStatus
    reason: str


class ConfidenceAssessment(BaseModel):
    level: ConfidenceLevel
    reason: str


class TestScenario(BaseModel):
    __test__ = False
    title: str
    scenario_type: ScenarioType
    category: TestCategory
    description: str
    priority: PriorityLevel
    expected_outcome: str
    quality_flags: list[QualityFlag] = Field(default_factory=list)


class RequirementAnalysis(BaseModel):
    summary: str

    requirement_types: list[RequirementType]

    testability: TestabilityAssessment

    overall_risk: RiskAssessment

    risks: list[Risk]

    quality_flags: list[QualityFlag]

    edge_cases: list[str]

    dependencies: list[str]

    assumptions: list[str]

    clarification_questions: list[str]

    test_scenarios: list[TestScenario]

    confidence: ConfidenceAssessment
