import argparse

from scrapers.Scraper_OpenU import Scraper_OpenU


class CLI:

    def __init__(self):
        self.Scraper = Scraper_OpenU()

        self.parser = argparse.ArgumentParser(description='OpenU Scraper')
        self.subparsers = self.parser.add_subparsers(help='sub-command help')

        # command generate to generate secrets.py
        self.add_generate_command()
        self.add_courses_info_command()

        self.args = self.parser.parse_args()
        self.args.func()

    def add_generate_command(self):
        parser_generate = self.subparsers.add_parser('generate',
                                                     help='Generate secrets.py file for user quthentication,'
                                                          'Required to run the scrapers')
        parser_generate.add_argument('username', type=str, help='User Name')
        parser_generate.add_argument('password', type=str, help='User password')
        parser_generate.add_argument('id', type=str, help='User id number')
        parser_generate.set_defaults(func=self.generate_secrets)

    def add_courses_info_command(self):
        parser_courses_info = self.subparsers.add_parser('courses',
                                                         help='Scrape users courses information from OpenU website')
        parser_courses_info.add_argument('-t' , '--type', choices=[])
        parser_courses_info.set_defaults(func=self.scrape_courses)

    def scrape_courses(self):
        """
        Scrape courses from OpenU website
        """

        self.Scraper.get_user_course_info().to_csv('courses.csv')

    def generate_secrets(self):
        """
        Generate secrets.py file for user quthentication
        Please provide username password and id to authenticate
        example :
        py OpenU_Scraper generate bob 1234568 315468467
        where username is bob , password is 1234568 , id is 315468467
        """

        with open('secrets-text-test.py', "w") as f:
            f.write(f"USER_NAME = '{self.args.username}'\n"
                    f"USER_PASSWORD = '{self.args.password}'\n"
                    f"USER_ID_NUMBER = '{self.args.id}'")

