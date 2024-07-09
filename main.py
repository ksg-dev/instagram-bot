from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

INSTA_USER = os.environ["INSTA_USERNAME"]
INSTA_PW = os.environ["INSTA_PW"]
INSTA_EMAIL = os.environ["INSTA_EMAIL"]
SIMILAR_ACCT = os.environ["SIMILAR_ACCOUNT"]


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

