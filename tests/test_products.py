from pages.products_page import add_very_products, checkout_cart
import pytest

@pytest.mark_parametrize('products',[
    
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
])

def test_add_very_products(usuario_login, products):
    add_very_products(usuario_login, [products])

def test_add_very_products(checkout_cart):
    produto = [
"Sauce Labs Backpack", 
"(Sauce Labs Bike Light",
"Sauce Labs Bolt T-Shirt",
"Sauce Labs Fleece Jacket",
"Sauce Labs Onesie",
"Test.allTheThings() T-Shirt (Red)"

carrinho = add_very_products():
assert carrinho == checkout_cart


]
