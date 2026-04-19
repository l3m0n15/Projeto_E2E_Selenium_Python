import pytest
from pages.checkout_page import error_checkout, go_to_checkout, back_button_cart
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

#Teste de informações de informações invalidas
def test_info_invalid(usuario_checkout, First_Name, Last_Name, Postal_Code, esperado):
    go_to_checkout(usuario_checkout, First_Name, Last_Name, Postal_Code,)
    assert error_checkout(usuario_checkout) == esperado

#Teste botão de voltar a pagina
def test_back_page(usuario_checkout):
    back_button_cart(usuario_checkout)
    assert "cart.html" in usuario_checkout.current_url