import pandas as pd
from Sheilta_Webdriver import Sheilta_Webdriver
from Table_Locations import USER_COURSE_INFO_TABLE_LOCATION
from URLs import User_Course_Info_URL
from utils import preprocess_grade_table


class Scraper:

    def __init__(self):
        self.session = Sheilta_Webdriver().get_logged_in_session()

    def get_user_course_info(self) -> pd.DataFrame:
        """Returns user course info as a dataframe"""
        response = self.session.get(User_Course_Info_URL)
        user_course_info_table = pd.read_html(response.content)[USER_COURSE_INFO_TABLE_LOCATION]
        return preprocess_grade_table(user_course_info_table)

    def get_
