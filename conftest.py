import pytest
import tempfile
from selenium import webdriver
from pages.login_page import go_to_login
from pages.products_page import go_to_products
from pages.cart_page import go_to_cart
from pages.checkout_page import go_to_checkout
from pages.finish_page import go_to_finish




@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "translate.enabled": False,
        "intl.accept_languages": "en,en_US"
    }

    options.add_experimental_option("prefs", prefs)

    # força inglês e tenta matar tradução do Chrome
    options.add_argument("--lang=en-US")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=Translate,TranslateUI")

    # cria perfil temporário limpo
    temp_profile = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_profile}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def usuario_login(driver):
    go_to_login(driver, "standard_user", "secret_sauce")
    return driver

@pytest.fixture
def (driver):
    usuario_login_main(driver, "standard_user", "secret_sauce")
    return driver

@pytest.fixture
def usuario_login(driver):
    usuario_login_main(driver, "standard_user", "secret_sauce")
    return driver

@pytest.fixture
def usuario_login(driver):
    usuario_login_main(driver, "standard_user", "secret_sauce")
    return driver



@pytest.fixture
def usuario_overview(usuario_login)
    open_cart(usuario_login)
    continue_button_cart(usuario_login)
    info_custom_user(usuario_login, "André", "Ryan" "05210290")