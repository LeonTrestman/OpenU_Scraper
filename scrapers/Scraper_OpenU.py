
import pandas as pd
from pandas import DataFrame
from requests import HTTPError, Session
from Table_Locations import *
from URLs import *
from Preprocessors import preprocess_latest_grades_table, preprocess_user_course_info
from scrapers.Scraper import Scraper
from scrapers.secrets import Secret_OpenU


class Scraper_OpenU(Scraper):

    def login(self) -> None:
        payload = {'p_user': Secret_OpenU.USER_NAME,
                   'p_sisma': Secret_OpenU.USER_PASSWORD,
                   'p_mis_student': Secret_OpenU.USER_ID_NUMBER,
                   'T_PLACE': T_PLACE_URL}
        session = self.session
        #get login cookies otherwise error no cookies enable in browser
        session.get(LOGIN_GET_URL)
        #post login request
        session.post(LOGIN_POST_URL, data=payload)


    def _validate_login(self) -> None:
        """validates login by checking cookies , if login fails, raises exception"""
        logged_in_cookie_verifier = 'opus_user_id' #logged in cookie contains opus_user_id
        if logged_in_cookie_verifier not in self.session.cookies:
            raise HTTPError('Login failed')


    def get_data(self) -> DataFrame:
        # get data
        # preprocess data
        pass

    def get_user_course_info(self) -> DataFrame:
        """Returns user course info as a dataframe"""
        response = self.session.get(USER_COURSE_INFO_URL)
        user_course_info_table = pd.read_html(response.content)[USER_COURSE_INFO_TABLE_LOCATION]
        return preprocess_user_course_info(user_course_info_table)


    def get_latest_grades(self) -> DataFrame:
        """Returns latest grades as a dataframe"""
        response = self.session.get(SHEILTA_MAIN_PAGE_URL)
        table : DataFrame = pd.read_html(response.content)[LATEST_GRADES_TABLE_LOCATION]
        return preprocess_latest_grades_table(table)


    def generate_secrets(self):
        pass



    def _validate_login(self) -> None:
        pass



