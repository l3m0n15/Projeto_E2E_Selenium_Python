import pytest
from pages.cart_page import products_cart
from pages.cart_page import remove_button
from pages.cart_page import continue_button_cart
from pages.cart_page import back_button_cart
from pages.products_page import add_very_products, go_to_products, open_cart

#Itens que estavam no carrinho
all_products =  [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
]

#Teste para confirmar 1 item por vez no carrinho
@pytest.mark.parametrize('products', all_products)
def test_cart_one_product(usuario_products, products):
    add_very_products(usuario_products, [products])
    open_cart(usuario_products)
    assert all(products_cart(usuario_products, [products]))

#Teste para confirmar vários itens de uma vez no carrinho
def test_add_all_products(usuario_products):
    add_very_products(usuario_products, all_products)
    open_cart(usuario_products)
    assert all(products_cart(usuario_products, all_products))

#Teste para remover 1 item por vez no carrinho
@pytest.mark.parametrize('products', all_products)
def test_remove_one_product(usuario_products, products):
    add_very_products(usuario_products, [products])
    open_cart(usuario_products)
    remove_button(usuario_products, [products])
    assert go_to_products(usuario_products) in ("", "0")

#Teste para remover vários itens de uma vez no carrinho
def test_remove_all_products(usuario_products):
    add_very_products(usuario_products, all_products)
    open_cart(usuario_products)
    remove_button(usuario_products, all_products)
    assert go_to_products(usuario_products) in ("", "0")

#Teste para retornar para a página da loja
def test_back_page(usuario_products):
    open_cart(usuario_products)
    back_button_cart(usuario_products)
    assert 'inventory.html' in usuario_products.current_url

#Teste prosseguir com carrinho vazio
def test_continue_with_item(usuario_products):
    open_cart(usuario_products)
    continue_button_cart(usuario_products)
    assert 'checkout-step-one.html' in usuario_products.current_url

