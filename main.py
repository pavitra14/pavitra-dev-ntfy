from typing import Union
from fastapi import FastAPI
from controllers.config import Config
from controllers.home import Home
from controllers.notify import Notify

#Initialise FastAPI app
app = FastAPI(title="pavitra.dev - Notify Framework", version="0.0.1")

#Initialise Modules
config = Config()
home = Home(config)
notify = Notify(config)

# Add Routes
app.include_router(home.router)
app.include_router(notify.router)
