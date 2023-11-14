from dotenv import dotenv_values, load_dotenv

class Config:
    """
    Class for loading and retrieving configuration values from .env file.
    """
    def __init__(self) -> None:
        """
        Load environment variables on initialization.
        """
        load_dotenv()
        self.__config = dotenv_values()

    def get(self, key: str) -> str:
        """
        Return the value for the given configuration key.
        If key is not found, return None.
        """
        return self.__config.get(key)

    def getAll(self) -> dict:
        """
        Return all configuration values.
        """
        return self.__config