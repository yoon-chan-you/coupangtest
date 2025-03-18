import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.pages.main_page import MainPage

@pytest.mark.usefixtures("driver")
def test_open_main_page(driver: WebDriver):
    main_page = MainPage(driver)
    main_page.open()
    assert "coupang.com" in driver.current_url, "쿠팡 메인 페이지가 정상적으로 열리지 않았습니다!"

@pytest.mark.usefixtures("driver")
def test_search_item(driver: WebDriver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search_item("노트북")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-product-list")))

    assert "q=%EB%85%B8%ED%8A%B8%EB%B6%81" in driver.current_url, "검색 결과 페이지가 정상적으로 열리지 않았습니다!"