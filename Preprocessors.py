"""Contains all preprocess functions for Scraper"""
from pandas import DataFrame

def preprocess_user_course_info(grade_table: DataFrame) -> DataFrame:
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


def preprocess_latest_grades_table(latest_grades_table: DataFrame) -> DataFrame:
    """
    Preprocesses the latest grades table.
    removes unnecessary columns and fixes encoding issues.
    """
    # drop unnecessary columns
    proccessed_lgs = latest_grades_table.drop(latest_grades_table.columns[-1], axis=1)
    # reverses the order of the columns
    proccessed_lgs = proccessed_lgs.iloc[:, ::-1]
    # set headers
    proccessed_lgs.columns = proccessed_lgs.iloc[1]
    proccessed_lgs = proccessed_lgs.iloc[2:]
    #remove headers (serise) name
    proccessed_lgs = proccessed_lgs.rename_axis(None,index=0 , axis=1)
    # reset index
    proccessed_lgs = proccessed_lgs.reset_index(drop=True)

    return proccessed_lgs