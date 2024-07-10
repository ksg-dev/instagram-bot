import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

INSTA_ROOT_URL = "https://www.instagram.com/"
INSTA_USER = os.environ["INSTA_USERNAME"]
INSTA_PW = os.environ["INSTA_PW"]
INSTA_EMAIL = os.environ["INSTA_EMAIL"]
SIMILAR_ACCT = os.environ["SIMILAR_ACCOUNT"]

# INSTA_USER_XPATH =
# INSTA_PASSWORD_XPATH


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username = self.driver.find_element(By.NAME, value="username")
        username.send_keys(INSTA_USER)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(INSTA_PW)
        password.send_keys(Keys.ENTER)
        time.sleep(7)

        no_save_login = self.driver.find_element(By.CLASS_NAME, value="x1i10hfl")
        no_save_login.click()
        time.sleep(5)

        try:
            notification_button = self.driver.find_element(By.CSS_SELECTOR, value="._a9_1")

        except NoSuchElementException:
            pass

        else:
            notification_button.click()



    def find_followers(self):
        self.driver.get(INSTA_ROOT_URL + SIMILAR_ACCT)
        time.sleep(2)

        followers_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, value="followers")
        followers_button.click()
        time.sleep(3)

        followers_popup_XPATH = "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        popup = self.driver.find_element(By.XPATH, followers_popup_XPATH)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            time.sleep(2)


    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
# bot.follow()

