import os
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

load_dotenv(find_dotenv())
driver_url = 'D:\Python\chromeDriver\chromedriver.exe'

EMAIL = os.environ["TWITTERMAIL"]
PASSWORD = os.environ["TWITTERPASSWORD"]

DOWNLOAD = 150
UPLOAD = 50


class InternetSpeedTwitterbot:
    def __init__(self, d):
        self.path = Service(executable_path=d)
        self.driver = webdriver.Chrome(service=self.path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get(url="https://www.speedtest.net/")

        go = self.driver.find_element(by="xpath",
                                      value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        time.sleep(40)
        self.down = self.driver.find_element(by="xpath",
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up = self.driver.find_element(by="xpath",
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

        self.up = float(self.up.text)
        self.down = float(self.down.text)
        if self.down<float(DOWNLOAD) and self.up<float(UPLOAD):
            self.tweet_at_provider(self.up, self.down)

    def tweet_at_provider(self, up, down):
        self.driver.get(url="https://twitter.com/login")

        time.sleep(3)
        input_field = self.driver.find_element(by="xpath",
                                               value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        input_field.send_keys(EMAIL)
        next_button = self.driver.find_element(by="xpath",
                                               value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(3)

        pass_field = self.driver.find_element(by="xpath",
                                              value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_field.send_keys(PASSWORD)
        time.sleep(1)
        login_button = self.driver.find_element(by="xpath",
                                                value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login_button.click()
        time.sleep(5)

        self.messge = f"@link3 Afnara koisla net speed {DOWNLOAD}/{UPLOAD} thabo kintu idaning dekha jar speed {down}/{up}, eto kom kene"
        write_complain = self.driver.find_element(by='xpath',
                                                  value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div')
        write_complain.click()
        time.sleep(2)
        write_complain = self.driver.find_element(by="xpath",
                                                  value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        write_complain.send_keys(self.messge)
        time.sleep(2)
        tweet = self.driver.find_element(by="xpath", value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet.click()


bot = InternetSpeedTwitterbot(driver_url)
bot.get_internet_speed()
