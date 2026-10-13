from enum import Enum


class _StrEnum(str, Enum):
    """Base so values serialize cleanly to JSON."""

    def __str__(self) -> str:
        return self.value


# ---------- AI analysis domain enums ----------


class RequirementType(_StrEnum):
    FUNCTIONAL = "Functional"
    SECURITY = "Security"
    PERFORMANCE = "Performance"
    USABILITY = "Usability"
    ACCESSIBILITY = "Accessibility"
    COMPATIBILITY = "Compatibility"
    RELIABILITY = "Reliability"
    COMPLIANCE = "Compliance"
    UI_UX = "UI/UX"
    INTEGRATION = "Integration"
    DATA = "Data"
    BUSINESS_RULE = "Business Rule"
    REPORTING = "Reporting"
    NON_FUNCTIONAL_OTHER = "Non-Functional (Other)"


class RiskLevel(_StrEnum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class RiskCategory(_StrEnum):
    SECURITY = "Security"
    DATA_LOSS = "Data Loss"
    FINANCIAL = "Financial"
    COMPLIANCE = "Compliance"
    PERFORMANCE = "Performance"
    USER_EXPERIENCE = "User Experience"
    INTEGRATION = "Integration"
    RELIABILITY = "Reliability"


class PriorityLevel(_StrEnum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class TestabilityStatus(_StrEnum):
    __test__ = False
    TESTABLE = "Testable"
    PARTIALLY_TESTABLE = "Partially Testable"
    NOT_TESTABLE = "Not Testable"


class ConfidenceLevel(_StrEnum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class QualityFlag(_StrEnum):
    AMBIGUOUS = "Ambiguous"
    INCOMPLETE = "Incomplete"
    CONFLICTING = "Conflicting"
    UNTESTABLE = "Untestable"
    DUPLICATE = "Duplicate"


class ScenarioType(_StrEnum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    BOUNDARY = "Boundary"
    EDGE_CASE = "Edge Case"
    RECOVERY = "Recovery"


class TestLevel(_StrEnum):
    __test__ = False
    UNIT = "Unit"
    INTEGRATION = "Integration"
    SYSTEM = "System"
    END_TO_END = "End-to-End"
    ACCEPTANCE = "Acceptance"


class TestCategory(_StrEnum):
    __test__ = False
    FUNCTIONAL = "Functional"
    PERFORMANCE = "Performance"
    SECURITY = "Security"
    USABILITY = "Usability"
    ACCESSIBILITY = "Accessibility"
    COMPATIBILITY = "Compatibility"
    DATA_VALIDATION = "Data Validation"
    API = "API"


class TestApproach(_StrEnum):
    __test__ = False
    BLACK_BOX = "Black Box"
    GREY_BOX = "Grey Box"
    WHITE_BOX = "White Box"


class TestDesignTechnique(_StrEnum):
    __test__ = False
    EQUIVALENCE_PARTITIONING = "Equivalence Partitioning"
    BOUNDARY_VALUE_ANALYSIS = "Boundary Value Analysis"
    DECISION_TABLE = "Decision Table"
    STATE_TRANSITION = "State Transition"
    ERROR_GUESSING = "Error Guessing"
    USE_CASE = "Use Case"


class TestPurpose(_StrEnum):
    __test__ = False
    SMOKE = "Smoke"
    SANITY = "Sanity"
    REGRESSION = "Regression"
    EXPLORATORY = "Exploratory"
    RETEST = "Retest"


# ---------- Human / system workflow enums (never in AI output) ----------


class ReviewStatus(_StrEnum):
    PENDING = "Pending"
    APPROVED = "Approved"
    EDITED = "Edited"
    REJECTED = "Rejected"


class RequirementStatus(_StrEnum):
    DRAFT = "Draft"
    NEEDS_CLARIFICATION = "Needs Clarification"
    REVIEW = "Review"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    IN_DEVELOPMENT = "In Development"
    READY_FOR_TEST = "Ready for Test"
    IMPLEMENTED = "Implemented"
    VERIFIED = "Verified"
    DEFERRED = "Deferred"
    OBSOLETE = "Obsolete"


class TestCaseStatus(_StrEnum):
    __test__ = False
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    PASSED = "Passed"
    FAILED = "Failed"
    BLOCKED = "Blocked"
    SKIPPED = "Skipped"
    RETEST = "Retest"
    DEPRECATED = "Deprecated"
