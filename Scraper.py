import time

import pandas as pd
from Sheilta_Webdriver import Sheilta_Webdriver
from Table_Locations import *
from URLs import User_Course_Info_URL, Sheilta_URL
from utils import user_course_info, preprocess_latest_grades_table


class Scraper:

    def __init__(self):
        sheilta_webdriver = Sheilta_Webdriver()
        self.session = sheilta_webdriver.get_logged_in_session()
        self.sheilta_page_source = sheilta_webdriver.driver.page_source

    def get_user_course_info(self) -> pd.DataFrame:
        """Returns user course info as a dataframe"""
        response = self.session.get(User_Course_Info_URL)
        user_course_info_table = pd.read_html(response.content)[USER_COURSE_INFO_TABLE_LOCATION]
        return user_course_info(user_course_info_table)

    def get_latest_grades(self) -> pd.DataFrame:
        """Returns latest grades as a dataframe"""
        table = pd.read_html(self.sheilta_page_source)[LATEST_GRADES_TABLE_LOCATION]
        return table

leon = Scraper()
leon.get_latest_grades().to_excel('leon_latest_grades.xlsx')