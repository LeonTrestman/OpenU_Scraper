import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from Secrets import USER_NAME, USER_PASSWORD, USER_ID_NUMBER
from URLs import Sheilta_URL


def get_list_from_table_row(scraped_row) -> list:
    """ Returns the scraped row as a list """
    return scraped_row.get_text(separator=',', strip=True).split(',')

def user_course_info(grade_table: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the grade table.
    removes unnecessary columns and fixes encoding issues.
    """
    drop_labels = ["פירוט", 'אתרהקורס']
    grade_table.drop(drop_labels, axis=1,inplace=True)
    grade_table.rename(columns={'נקודותזכות': 'נקודות זכות',
                                'ציוןסופי':'ציון סופי',
                                'ציוןבחינה':'ציון בחינה',
                                'קורסלתואר': 'קורסל תואר'},
                       inplace=True)
    return grade_table

#TODO:fix index of the table
def preprocess_latest_grades_table(latest_grades_table: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the latest grades table.
    removes unnecessary columns and fixes encoding issues.
    """
    #remove unnecessary row
    latest_grades_table = latest_grades_table.iloc[1:]
    #set headers
    latest_grades_table.columns = latest_grades_table.iloc[0]
    latest_grades_table = latest_grades_table.iloc[1:]
    # latest_grades_table.reset_index(inplace=True, drop=True)

    return latest_grades_table