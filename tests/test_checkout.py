import pytest
from pages.checkout_page import error_checkout, info_custom_user, back_button_cart

#Informações válidas
def test_info_valid(usuario_checkout):
    info_custom_user(usuario_checkout, "André Ryan", "De Paula Moreira", "05210290")
    assert "checkout-step-two.html" in usuario_checkout.current_url

#Informações inválidas
@pytest.mark.parametrize("First_Name, Last_Name, Postal_Code, esperado",[
("", "valid", "valido", "Error: First Name is required"),
("valid", "", "valid", "Error: Last Name is required"),
("valid", "valid", "", "Error: Postal Code is required")
])

#Teste de informações inválidas
def test_info_invalid(usuario_checkout, First_Name, Last_Name, Postal_Code, esperado):
    info_custom_user(usuario_checkout, First_Name, Last_Name, Postal_Code,)
    assert error_checkout(usuario_checkout) == esperado

#Teste do botão de voltar à página
def test_back_page(usuario_checkout):
    back_button_cart(usuario_checkout)
    assert "cart.html" in usuario_checkout.current_url