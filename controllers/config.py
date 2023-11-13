from dotenv import dotenv_values, load_dotenv

class Config:
    def __init__(self) -> None:
        load_dotenv()
        self.__config = dotenv_values()

    def get(self, key: str) -> str:
        return self.__config[key]
        
    def getAll(self) -> dict:
        return self.__config