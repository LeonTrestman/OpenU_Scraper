from abc import ABC , abstractmethod
from requests import Session


class Scraper(ABC):

    def __init__(self):
        self.session = Session()
        self.login()
        self._validate_login()


    @abstractmethod
    def generate_secrets(self):
        ...

    @abstractmethod
    def login(self):
        """implement logged in with session"""
        ...

    @abstractmethod
    def _validate_login(self) -> None:
        """implement validation for login """
        ...

    @abstractmethod
    def get_data(self):
        ...


