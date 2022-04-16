import pandas as pd
from pandas import DataFrame
from requests import HTTPError
from Table_Locations import *
from URLs import *
from Preprocessors import preprocess_latest_grades_table, preprocess_user_course_info
from commands.Commands import command
from scrapers.Scraper import Scraper
from scrapers.secrets import Secret_OpenU

data_choices =['latest', 'courses']

class Scraper_OpenU(Scraper):


    def __init__(self):
        super().__init__(data_choices)


    def _login(self) -> None:
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


    def get_data(self,data) -> DataFrame:
        """
        :param type: type of data to be scraped
        :return: dataframe of scraped data
        """
        data_funcs = {'latest': 'test',
                'courses': get_latest_grade_command().execute(self.session)}

        return data_funcs[data]
        # get data
        # preprocess data
        pass


    def generate_secrets(self):
        pass

#changed to classes to be more oop , needs work

class get_user_course_info_command(command):
    def execute(self , session) -> DataFrame:
        """Returns user course info as a dataframe"""
        response = session.get(USER_COURSE_INFO_URL)
        user_course_info_table = pd.read_html(response.content)[USER_COURSE_INFO_TABLE_LOCATION]
        return preprocess_user_course_info(user_course_info_table)


class get_latest_grade_command():
    def execute(self , session) -> DataFrame:
        """Returns latest grades as a dataframe"""
        response = session.get(SHEILTA_MAIN_PAGE_URL)
        table : DataFrame = pd.read_html(response.content)[LATEST_GRADES_TABLE_LOCATION]
        return preprocess_latest_grades_table(table)






