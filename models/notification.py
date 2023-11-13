from pydantic import BaseModel
from models.actions import Actions
from models.priority import Priority

class Notification(BaseModel):
    topic: str
    data: str
    priority: Priority = Priority.DEFAULT
    tags: list[str] = [""]
    title: str = ""
    link: str = ""
    attachment: str = ""
    actions: list[Actions] = []
    email: str = ""
    
    def getHeaders(self):
        headers = {}
        headers["X-Priority"] = self.priority.value
        if len(self.tags) > 0:
            headers["X-Tags"] = ",".join(self.tags)

        if self.title:
            headers["X-Title"] = self.title

        if self.link:
            headers["X-Click"] = self.link

        if self.attachment:
            headers["X-Attach"] = self.attachment

        if self.actions and len(self.actions) > 0:
            actionList = []
            for action in self.actions:
                actionList.append(",".join([action.actionType.value, action.label, action.url]))
            headers["X-Actions"] = ";".join(actionList)

        if self.email:
                headers["X-Email"] = self.email
        return headers
    