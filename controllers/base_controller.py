from fastapi import APIRouter

class BaseController:
    """
    BaseController Class for all controllers to extend.
    """
    router = APIRouter()