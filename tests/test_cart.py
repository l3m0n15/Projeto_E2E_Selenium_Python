import pytest
from pages.cart_page import products_cart
from pages.cart_page import remove_button
from pages.cart_page import continue_button_cart
from pages.cart_page import back_button_cart
from pages.products_page import checkout_cart
from pages.products_page import add_very_products, open_cart

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
@pytest.mark.parametrize('products', all_products)
def test_cart_one_product(usuario_login, products):
    add_very_products(usuario_login, [products])
    open_cart(usuario_login)
    assert all(products_cart(usuario_login, [products]))

#Teste para confirmar varios itens de uma vez no carrinho
def test_add_all_products(usuario_login):
    add_very_products(usuario_login, all_products)
    open_cart(usuario_login)
    assert all(products_cart(usuario_login, all_products))

#Teste para remover 1 item por vem no carrinho
@pytest.mark.parametrize('products', all_products)
def test_remove_one_product(usuario_login, products):
    add_very_products(usuario_login, [products])
    open_cart(usuario_login)
    remove_button(usuario_login, [products])
    assert checkout_cart(usuario_login) == "0"

#Teste para remover varios itens de uma vez no carrinho
def test_remove_all_products(usuario_login):
    add_very_products(usuario_login, all_products)
    open_cart(usuario_login)
    remove_button(usuario_login, all_products)
    assert  checkout_cart(usuario_login) == "0"

#Teste retornar para a pagina da Loja
def test_back_page(usuario_login):
    open_cart(usuario_login)
    back_button_cart(usuario_login)
    assert 'inventory.html' in usuario_login.current_url

#Teste prosseguir com carrinho vazio
def test_continue_with_item(usuario_login):
    open_cart(usuario_login)
    continue_button_cart(usuario_login)
    assert 'checkout-step-one.html' in usuario_login.current_url

