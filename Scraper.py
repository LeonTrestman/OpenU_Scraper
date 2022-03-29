
import pandas as pd
from Sheilta_Webdriver import Sheilta_Webdriver
from Table_Locations import *
from URLs import User_Course_Info_URL
from Preprocessors import preprocess_latest_grades_table, preprocess_user_course_info


class Scraper:

    def __init__(self):
        sheilta_webdriver = Sheilta_Webdriver()
        self.session = sheilta_webdriver.get_logged_in_session()

    def get_user_course_info(self) -> pd.DataFrame:
        """Returns user course info as a dataframe"""
        response = self.session.get(User_Course_Info_URL)
        user_course_info_table = pd.read_html(response.content)[USER_COURSE_INFO_TABLE_LOCATION]
        res = preprocess_user_course_info(user_course_info_table)
        return res

    def get_latest_grades(self) -> pd.DataFrame:
        """Returns latest grades as a dataframe"""
        response = self.session.get('https://sheilta.apps.openu.ac.il/pls/dmyopt2/myop.myop_screen')
        table = pd.read_html(response.content)[LATEST_GRADES_TABLE_LOCATION]
        return preprocess_latest_grades_table(table)


    def test(self):
        response = self.session.get('https://sheilta.apps.openu.ac.il/pls/dmyopt2/myop.myop_screen')
        print(response.text)

leon = Scraper()
table : pd.DataFrame = leon.get_latest_grades()
table2 = leon.get_user_course_info()
print(table2.columns)
table.name = 'Leon'
print(table.columns)
print(table)