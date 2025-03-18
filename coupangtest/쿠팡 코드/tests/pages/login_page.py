from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

class LoginPage:
    URL = "https://www.coupang.com/np/member/login"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)

    def login(self, user_id: str, password: str):
    