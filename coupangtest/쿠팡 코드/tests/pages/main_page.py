from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

class MainPage:
    URL = "https://www.coupang.com"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)

    def search_item(self, item_name: str):
        search_input_box = self.driver.find_element(By.ID, "headerSearchKeyword")
        search_input_box.send_keys(item_name)

        search_button = self.driver.find_element(By.ID, "headerSearchBtn")
        search_button.click()