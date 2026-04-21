import pytest
import tempfile
from selenium import webdriver
from pages.products_page import add_very_products
from pages.products_page import open_cart
from pages.login_page import fazer_login
from pages.cart_page import continue_button_cart
from pages.checkout_page import info_custom_user
from pages.finish_page import go_to_finish

#Atalho com todos os produtos para cenários de compra completa
all_products = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
]

#Driver base para todos os testes
@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "translate.enabled": False,
        "intl.accept_languages": "en,en_US"
    }
    #Config de browser para evitar popup/chrome traduzindo durante os testes
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--lang=en-US")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-sync")
    options.add_argument("--password-store=basic")
    options.add_argument("--disable-features=Translate,TranslateUI,PasswordLeakDetection,PasswordCheck")

    #Perfil temporário para cada execução de teste
    temp_profile = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_profile}")

    #Abrindo site base e maximizando para manter padrão visual
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

#Usuário logado na página inicial da loja
@pytest.fixture
def usuario_login(driver):
    fazer_login(driver, "standard_user", "secret_sauce")
    return driver

#Usuário na página de produtos (inventário)
@pytest.fixture
def usuario_products(usuario_login):
    return usuario_login

#Usuário dentro do carrinho
@pytest.fixture
def usuario_cart(usuario_products):
    open_cart(usuario_products)
    return usuario_products

#Usuário na tela de checkout step one
@pytest.fixture
def usuario_checkout(usuario_cart):
    continue_button_cart(usuario_cart)
    return usuario_cart

#Fluxo completo até checkout overview com todos os produtos
@pytest.fixture
def usuario_finish(usuario_products):
    add_very_products(usuario_products, all_products)
    open_cart(usuario_products)
    continue_button_cart(usuario_products)
    info_custom_user(usuario_products, "André", "Ryan", "05210290")
    return usuario_products

#Mesmo fluxo de finish, mas com 1 produto por vez vindo do parametrize
@pytest.fixture
def usuario_finish_produto(usuario_products, products):
    add_very_products(usuario_products, [products])
    open_cart(usuario_products)
    continue_button_cart(usuario_products)
    info_custom_user(usuario_products, "André", "Ryan", "05210290")
    return usuario_products

@pytest.fixture
def usuario_complete(usuario_finish):
    go_to_finish(usuario_finish)
    return usuario_finish