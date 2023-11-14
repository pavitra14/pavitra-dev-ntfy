from pydantic import BaseModel
from enum import Enum

class ActionType(Enum):
    """
    Enum class for possible action types.
    """
    VIEW = "view"
    BROADCAST = "broadcast"
    HTTP = "http"

class Actions(BaseModel):
    """
    BaseModel class for action data.
    """
    actionType: ActionType
    label: str
    url: str