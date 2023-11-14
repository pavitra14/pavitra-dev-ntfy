from pydantic import BaseModel
from models.actions import Actions
from models.priority import Priority

class Notification(BaseModel):
    topic: str
    data: str
    priority: Priority = Priority.DEFAULT
    tags: list[str] = []
    title: str = ""
    link: str = ""
    attachment: str = ""
    actions: list[Actions] = []
    email: str = ""
    
    def getHeaders(self):
        """
        Method to get the headers for a notification.
        """
        headers = {
            "X-Priority": self.priority.value,
            "X-Tags": ",".join(self.tags) if self.tags else None,
            "X-Title": self.title if self.title else None,
            "X-Click": self.link if self.link else None,
            "X-Attach": self.attachment if self.attachment else None,
            "X-Actions": ";".join([",".join([action.actionType.value, action.label, action.url]) for action in self.actions]) if self.actions else None,
            "X-Email": self.email if self.email else None,
        }

        # Remove None values
        headers = {k: v for k, v in headers.items() if v is not None}
        return headers
    