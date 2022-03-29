
import pandas as pd
from Sheilta_Webdriver import Sheilta_Webdriver
from Table_Locations import *
from URLs import User_Course_Info_URL
from Preprocessors import preprocess_latest_grades_table, preprocess_user_course_info


class Scraper:

    def __init__(self):
        sheilta_webdriver = Sheilta_Webdriver()
        self.session = sheilta_webdriver.get_logged_in_session()
        self.sheilta_page_source = sheilta_webdriver.driver.page_source

    def get_user_course_info(self) -> pd.DataFrame:
        """Returns user course info as a dataframe"""
        response = self.session.get(User_Course_Info_URL)
        user_course_info_table = pd.read_html(response.content)[USER_COURSE_INFO_TABLE_LOCATION]
        res = preprocess_user_course_info(user_course_info_table)
        print(res.columns)
        print(res)
        res.to_excel('user_course_info.xlsx')
        return res

    def get_latest_grades(self) -> pd.DataFrame:
        """Returns latest grades as a dataframe"""
        table = pd.read_html(self.sheilta_page_source)[LATEST_GRADES_TABLE_LOCATION]
        return preprocess_latest_grades_table(table)


