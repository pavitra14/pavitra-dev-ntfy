import base64
from controllers.config import Config
from models.notification import Notification
import requests

class ntfy:
    def __init__(self, config: Config) -> None:
        self.url = config.get("NTFY_SERVER")
        self.user = config.get("NTFY_USER")
        self.userpwd = config.get("NTFY_PASS")
        
    def send(self, notification: Notification):
        final_url = "{}/{}".format(self.url, notification.topic)
        final_headers = notification.getHeaders()
        final_headers["Authorization"] = self.__genAuthHeader()
        request = requests.post(
            url=final_url,
            data=notification.data,
            headers=final_headers
        )
        return request.status_code
    
    def __genAuthHeader(self) -> str:
        authStr = self.user + ":" + self.userpwd
        authStrBytes = authStr.encode()
        b64Bytes = base64.b64encode(authStrBytes)
        return "Basic " + b64Bytes.decode()
