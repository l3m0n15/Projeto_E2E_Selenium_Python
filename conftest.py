from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from login_page import fazer_login


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def usuario_login(driver):
    fazer_login(driver, "standard_user", "secret_sauce")
    return driver