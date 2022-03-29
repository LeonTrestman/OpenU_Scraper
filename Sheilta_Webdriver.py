import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from Secrets import USER_NAME, USER_PASSWORD, USER_ID_NUMBER
from URLs import Sheilta_URL


class Sheilta_Webdriver():
    """ Class for the Sheilta Webdriver """

    def __init__(self):
        self.driver = self.start_webdriver()
        self.sheilta_page_source = self.driver.page_source
        self.login()
        self.login_cookies = self.get_login_cookies()

    def start_webdriver(self) -> webdriver:
        """ Returns webdriver"""
        options = webdriver.ChromeOptions()
        options.headless = False
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        driver.get(Sheilta_URL)
        return driver

    def login(self) -> None:
        """Logs in webdriver to Sheilta """
        # get login elements
        user_name_element = self.driver.find_element(value="p_user")
        password_element = self.driver.find_element(value="p_sisma")
        user_id_element = self.driver.find_element(value="p_mis_student")
        # fill form
        user_name_element.send_keys(USER_NAME)
        password_element.send_keys(USER_PASSWORD)
        user_id_element.send_keys(USER_ID_NUMBER)
        # submit login
        user_id_element.submit()
        # wait for completion of login
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "app")))
        except:
            print("Failed to log in ")

    def get_login_cookies(self) -> dict:
        """ Returns the cookies of the logged in user """
        cookies = self.driver.get_cookies()
        # self.driver.quit()
        log_in_cookies = {}
        for cookie in cookies:
            log_in_cookies[cookie['name']] = cookie['value']
        return log_in_cookies

    def get_logged_in_session(self) -> requests.Session:
        """Returns a logged in to sheilta session"""
        session = requests.Session()
        session.cookies.update(self.login_cookies)
        return session