from pages.products_page import add_very_products
import pytest

all_products= [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
]

@pytest.mark.parametrize('products','all_products')
def test_add_one_product(usuario_login, products):
    add_very_products(usuario_login, [products])

    assert add_very_products(usuario_login, products)

def test_add_lis(usuario_login):
    add_very_products(usuario_login, all_products)

    assert add_very_products(usuario_login, all_products)

