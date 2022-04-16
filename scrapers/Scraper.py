from abc import ABC , abstractmethod
from requests import Session


class Scraper(ABC):

    def __init__(self,data_choises: list):
        self.session = Session()
        self._login()
        self._validate_login()
        self.data_choices = data_choises


    @abstractmethod
    def generate_secrets(self):
        ...

    @abstractmethod
    def _login(self):
        """implement logged in with session"""
        ...

    @abstractmethod
    def _validate_login(self) -> None:
        """implement validation for login """
        ...

    @abstractmethod
    def get_data(self):
        ...


