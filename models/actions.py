from pydantic import BaseModel
from enum import Enum

class ActionType(Enum):
    VIEW = "view",
    BROADCAST = "broadcast",
    HTTP = "http"

class Actions(BaseModel):
    actionType: ActionType
    label: str
    url: str