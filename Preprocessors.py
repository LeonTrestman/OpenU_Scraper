"""Contains all preprocess functions for Scraper"""
import pandas as pd

def get_list_from_table_row(scraped_row) -> list:
    """ Returns the scraped row as a list """
    return scraped_row.get_text(separator=',', strip=True).split(',')

def preprocess_user_course_info(grade_table: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the grade table.
    removes unnecessary columns and fixes encoding issues.
    """

    drop_labels = ["פירוט", 'אתרהקורס']
    procceeded_grade_table = grade_table.drop(drop_labels, axis=1)
    procceeded_grade_table = procceeded_grade_table.rename(columns={'נקודותזכות': 'נקודות זכות',
                                'ציוןסופי':'ציון סופי',
                                'ציוןבחינה':'ציון בחינה',
                                'קורסלתואר': 'קורסל תואר'},
                       )
    return procceeded_grade_table


def preprocess_latest_grades_table(latest_grades_table: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the latest grades table.
    removes unnecessary columns and fixes encoding issues.
    """
    # drop unnecessary columns
    proccessed_lgs = latest_grades_table.drop(latest_grades_table.columns[-1], axis=1)
    # revrese the order of the columns
    proccessed_lgs = proccessed_lgs.iloc[:, ::-1]
    # set headers
    proccessed_lgs.columns = proccessed_lgs.iloc[1]
    proccessed_lgs = proccessed_lgs.iloc[2:]
    # reset index
    proccessed_lgs = proccessed_lgs.reset_index(drop=True)

    return proccessed_lgs