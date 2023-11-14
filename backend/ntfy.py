import base64
from controllers.config import Config
from models.notification import Notification
import requests

class ntfy:
    """
    A class to handle notifications.
    """
    AUTHORIZATION = "Authorization"
    BASIC = "Basic "

    def __init__(self, config: Config) -> None:
        """
        Initialize with configuration.
        """
        self.url = config.get("NTFY_SERVER")
        self.user = config.get("NTFY_USER")
        self.userpwd = config.get("NTFY_PASS")

    def send(self, notification: Notification) -> int:
        """
        Send a notification.
        
        :param notification: Notification object to be sent.
        :return: HTTP status code of the sent request.
        """
        final_url = f"{self.url}/{notification.topic}"
        final_headers = notification.getHeaders()
        final_headers[self.AUTHORIZATION] = self.__gen_auth_header()
        try:
            request = requests.post(
                url=final_url,
                data=notification.data,
                headers=final_headers
            )
            return request.status_code
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return -1

    def __gen_auth_header(self) -> str:
        """
        Generate authorization header.
        
        :return: Base64 encoded authorization string.
        """
        auth_str = f"{self.user}:{self.userpwd}"
        b64_bytes = base64.b64encode(auth_str.encode())
        return f"{self.BASIC}{b64_bytes.decode()}"