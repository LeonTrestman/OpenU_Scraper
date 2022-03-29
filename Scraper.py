import pandas as pd
from Secrets import *
import requests
from Table_Locations import *
from URLs import USER_COURSE_INFO_URL, SHEILTA_MAIN_PAGE_URL, LOGIN_POST_URL, LOGIN_GET_URL
from Preprocessors import preprocess_latest_grades_table, preprocess_user_course_info


class Scraper:

    def __init__(self):
        self.session = self.get_logged_in_session()

    def get_logged_in_session(self) -> requests.Session:
        """Returns logged in session"""
        login_url = 'https://sso.apps.openu.ac.il/process'
        payload = {'p_user': USER_NAME, 'p_sisma': USER_PASSWORD, 'p_mis_student': USER_ID_NUMBER,
                   'T_PLACE': 'https://sheilta.apps.openu.ac.il/Main/Home/Index'}
        session = requests.Session()
        #get login cookies otherwise error no cookies enable in browser
        session.get(LOGIN_GET_URL)
        #post login request
        session.post(LOGIN_POST_URL, data=payload)
        return session


    def get_user_course_info(self) -> pd.DataFrame:
        """Returns user course info as a dataframe"""
        response = self.session.get(USER_COURSE_INFO_URL)
        user_course_info_table = pd.read_html(response.content)[USER_COURSE_INFO_TABLE_LOCATION]
        return preprocess_user_course_info(user_course_info_table)


    def get_latest_grades(self) -> pd.DataFrame:
        """Returns latest grades as a dataframe"""
        response = self.session.get(SHEILTA_MAIN_PAGE_URL)
        table = pd.read_html(response.content)[LATEST_GRADES_TABLE_LOCATION]
        return preprocess_latest_grades_table(table)
