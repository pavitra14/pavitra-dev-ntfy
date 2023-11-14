from fastapi.responses import ORJSONResponse
from fastapi.encoders import jsonable_encoder
from controllers.base_controller import BaseController
from controllers.config import Config
from models.notification import Notification
from backend.ntfy import ntfy

class Notify(BaseController):
    """
    Class representing the notification controller.
    """
    def __init__(self, config: Config) -> None:
        """
        Initialize Notify controller with configuration.
        """
        self.__config = config
        self.router.add_api_route("/publish", self.publish, methods=["POST"])

    def publish(self, notification: Notification) -> ORJSONResponse:
        """
        Publish a notification.
        """
        channel = ntfy(self.__config)
        try:
            statusCode = channel.send(notification)
            resp = {
                "notification": notification, 
                "headers": notification.getHeaders(),
                "statusCode" : statusCode
                }
            return ORJSONResponse(content=jsonable_encoder(resp), status_code=statusCode)
        except Exception as e:
            return ORJSONResponse(content={"error": str(e)}, status_code=500)