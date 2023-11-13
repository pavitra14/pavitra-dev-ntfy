from fastapi.responses import HTMLResponse
from controllers.base_controller import BaseController
from controllers.config import Config


class Home(BaseController):
    def __init__(self, config: Config) -> None:
        self.__config = config
        self.router.add_api_route("/", self.hello, methods=["GET"])
        self.router.add_api_route("/env", self.getConfig, methods=["GET"])

    def hello(self) -> HTMLResponse:
        htmlContent = """
        <html>
            <head>
                <title>Hello, World</title>
            </head>
            <body>
                <h1>Look ma! HTML! </h1>
                <h2>Click <a href="/docs">here</a> or <a href="/redoc">here</a> to read docs</h2>
            </body>
        </html>
        """
        return HTMLResponse(content=htmlContent, status_code=200)

    def getConfig(self):
        return {"env":self.__config.getAll()}