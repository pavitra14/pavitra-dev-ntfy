"""
This script initializes and configures the FastAPI application.
"""
from fastapi import FastAPI
from controllers.config import Config
from controllers.home import Home
from controllers.notify import Notify
from uvicorn import Config as UvicornConfig, Server

# Initialize FastAPI app
app = FastAPI(title="pavitra.dev - Notify Framework", version="0.0.1")

# Initialize Controllers
config = Config()
home = Home(config)
notify = Notify(config)

# Add routes from controllers to the app
app.include_router(home.router)
app.include_router(notify.router)

# Run application
if __name__ == "__main__":
    try:
        uvicorn_config = UvicornConfig("main:app", port=9000, log_level="info")
        server = Server(uvicorn_config)
        server.run()
    except Exception as e:
        print(f"An error occurred: {e}")