from pages.products_page import add_very_products
from pages.products_page import go_to_products
import pytest

#Atalho para todos os produtos
all_products= [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
]

#Adicionando 1 produto por vez no carrinho
@pytest.mark.parametrize('products', all_products)
def test_add_one_product(usuario_products, products):
    add_very_products(usuario_products, [products])
    assert go_to_products(usuario_products) == '1'

#Adicionando todos os produtos de uma vez para o carrinho
def test_add_list(usuario_products):
    add_very_products(usuario_products, all_products)
    assert go_to_products(usuario_products) == '6'