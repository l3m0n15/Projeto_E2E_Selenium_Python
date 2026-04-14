from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.cart_page import products_cart
from pages.cart_page import remove_button
from pages.cart_page import continue_button_cart
from pages.cart_page import back_button_cart



#Itens que estavam no carrinho
all_products =  [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
]

#Teste para confirmar 1 item por vem no carrinho
@pytest.mark.parametrize('products', 'all_products')
def test_cart_one_product(usuario_login, products):
    products_cart(usuario_login, [products])

    assert products_cart(usuario_login, products)

#Teste para confirmar varios itens de uma vez no carrinho
def test_add_all_products(usuario_login, all_products):
    products_cart(usuario_login, all_products)

    assert products_cart(usuario_login, all_products)

#Teste para remover 1 item por vem no carrinho
@pytest.mark.parametrize('products','all_products')
def test_remove_one_product(usuario_login, products):
    remove_button(usuario_login, [products])

    assert not remove_button(usuario_login, products)

#Teste para remover varios itens de uma vez no carrinho
def test_remove_all_products(usuario_login, all_products):
    remove_button(usuario_login, all_products)

    assert not remove_button(usuario_login, all_products)

def test_back_page(usuario_login):
    back_button_cart(usuario_login)
    
    assert 'inventory.html' in usuario_login.current_url

