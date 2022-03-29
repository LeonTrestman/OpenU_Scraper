import requests

from Sheilta_Webdriver import Sheilta_Webdriver
from utils import *


class Scraper:
    def __init__(self):
        session = self.get_logged_in_session()

    def get_logged_in_session(self) -> requests.Session:
        """Returns a logged in to sheilta session"""
        session = requests.Session()
        login_cookies = Sheilta_Webdriver().get_login_cookies()
        session.cookies.update(login_cookies)
        return session






leon = Scraper()
