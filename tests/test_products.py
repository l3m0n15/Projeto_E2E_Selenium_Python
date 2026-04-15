from pages.products_page import add_very_products
from pages.products_page import button_add
from pages.products_page import back_shopping
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
    button_add(usuario_login, [products])
    back_shopping(usuario_login, [products])

    

    assert add_very_products(usuario_login, products)
    assert button_add(usuario_login, products)
    assert back_shopping(usuario_login, products)



def test_add_lis(usuario_login):
    add_very_products(usuario_login, all_products)
    button_add(usuario_login, all_products)
    back_shopping(usuario_login, all_products)


    assert add_very_products(usuario_login, all_products)
    assert button_add(usuario_login, all_products)
    assert back_shopping(usuario_login, all_products)



