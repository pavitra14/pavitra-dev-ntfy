from enum import Enum

class Priority(Enum):
    """
    Enum class for priority levels.
    """
    MIN = "min"
    LOW = "low"
    DEFAULT = "default"
    HIGH = "high"
    MAX = "max"