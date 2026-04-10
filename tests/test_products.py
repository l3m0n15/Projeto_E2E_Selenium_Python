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
    
    add_very_products(usuario_login, produtos)

    quantidade_very_products = checkout_cart(usuario_login)

    assert quantidade_very_products == "6"

@pytest.mark.parametrize("products", [

        'Sauce Labs Backpack',
        'Sauce Labs Bike Light',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Fleece',
        'Sauce Labs Fleece Jacket',
        'Sauce Labs Onesie',
        'Test.allTheThings() T-Shirt (Red)'
    ])

def test_add_product(usuario_login, products):
    add_product(usuario_login, products)
   
    quantidade_product = checkout_cart(usuario_login, products)
    assert quantidade_product == "1"