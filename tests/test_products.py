from pages.products_page import add_very_products, checkout_cart
from pages.products_page import add_product
import pytest

def test_add_very_products(usuario_login):
    produtos = [
    'Sauce Labs Backpack',
    'Sauce Labs Bike Light',
    'Sauce Labs Bolt T-Shirt',
    'Sauce Labs Fleece',
    'Sauce Labs Fleece Jacket',
    'Sauce Labs Onesie',
    'Test.allTheThings() T-Shirt (Red)'
]




@pytest.mark.parametrize("produtos", [
        

        'Sauce Labs Backpack',
        'Sauce Labs Bike Light',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Fleece',
        'Sauce Labs Fleece Jacket',
        'Sauce Labs Onesie',
        'Test.allTheThings() T-Shirt (Red)'
    ])

def test_add_product(driver):
    checkout_cart(driver)

    assert checkout_cart == "6"