import pytest
from pages.checkout_page import error_checkout, info_custom_user, back_button_cart
from pages.products_page import open_cart
from pages.cart_page import continue_button_cart

#Informações validas
def test_info_valid(usuario_login):
    open_cart(usuario_login)
    continue_button_cart(usuario_login)
    info_custom_user(usuario_login, "André Ryan", "De Paula Moreira", "05210290")
    assert "checkout-step-two.html" in usuario_login.current_url

#Informações invalidas
@pytest.mark.parametrize("First_Name, Last_Name, Postal_Code, esperado",[
("", "valid", "valido", "Error: First Name is required"),
("valid", "", "valid", "Error: Last Name is required"),
("valid", "valid", "", "Error: Postal Code is required")

])

#Teste de informações de usuario invalidas
def test_info_invalid(usuario_login, First_name, Last_name, Postal_Code, esperado):
    open_cart(usuario_login)
    continue_button_cart(usuario_login)
    info_custom_user(usuario_login, First_name, Last_name, Postal_Code)
    assert error_checkout(usuario_login) == esperado

def test_back_page(usuario_login):
    open_cart(usuario_login)
    continue_button_cart(usuario_login)
    back_button_cart(usuario_login)

    assert "cart.html" in usuario_login.current_url