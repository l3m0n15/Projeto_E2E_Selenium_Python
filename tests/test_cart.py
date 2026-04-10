from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.products_page import add_very_products, add_product, open_cart
from pages.cart_page import remove_button, products_cart

#TESTE PARA VERIFICAR SE O CARRINHO ABRE CORRETAMENTE
def test_open_cart(usuario_login):
    open_cart(usuario_login)

    assert "cart_html" in usuario_login.current_url

#TESTE DE VARIOS PRODUTOS DE UMA VEZ
def test_add_very_products(usuario_login):
        products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)"
        ]



        for product in products:
            add_very_products(usuario_login, product)

        open_cart(usuario_login)

        for product in products:
            assert products_cart(usuario_login, product)



