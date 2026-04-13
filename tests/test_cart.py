from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import products_cart
from pages.cart_page import remove_button
import pytest


all_products =  [
    
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
]

#
@pytest.mark.parametrize('products', 'all_products')
def test_cart_one_product(usuario_login, products):
    products_cart(usuario_login, [products])
    assert products_cart(usuario_login, products)
#
def test_add_all_products(usuario_login, all_products):
    products_cart(usuario_login, all_products)
    assert products_cart(usuario_login, all_products)
#
@pytest.mark.parametrize('products','all_products')
def test_remove_one_product(usuario_login, products):
    remove_button(usuario_login, [products])
    assert not remove_button(usuario_login, products)
#
def test_remove_all_products(usuario_login, all_products):
    remove_button(usuario_login, all_products)
    assert not remove_button(usuario_login, all_products)