from controllers.config import Config
from controllers.base_controller import BaseController
from models.notification import Notification
from backend.ntfy import ntfy
from fastapi.responses import ORJSONResponse
from fastapi.encoders import jsonable_encoder


class Notify(BaseController):
    def __init__(self, config: Config) -> None:
        self.__config = config
        self.router.add_api_route("/publish", self.publish, methods=["POST"])
        
    def publish(self, notification: Notification) -> ORJSONResponse:
        channel = ntfy(self.__config)
        statusCode = channel.send(notification)
        resp = {
            "notification": notification, 
            "headers": notification.getHeaders(),
            "statusCode" : statusCode
            }
        return ORJSONResponse(content=jsonable_encoder(resp), status_code=statusCode)