from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.login_page import fazer_login



@pytest.fixture()
def driver():
     # Desativa gerenciador de senha e autofill, para tirar o popus
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "translate": {"enabled": False}
 }
    
 # Argumentos extras pra evitar popup/chateação do Chrome
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-notifications")
    options.add_argument("--guest")  # abre como convidado, sem perfil salvo
    options.add_argument("--disable-translate")


    
    driver = webdriver.Chrome(options=options)


    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

#Driver login está com o nome de usuario_login
@pytest.fixture
def usuario_login(driver):
    fazer_login(driver, "standard_user", "secret_sauce")
    return driver