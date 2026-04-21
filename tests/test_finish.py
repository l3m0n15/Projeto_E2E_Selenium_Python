import pytest
from pages.finish_page import subtotal_checkout, tax_checkout, total_checkout, soma_total
#Atalho para todos os produtos
all_products= [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
]

#Teste 1 item por vez
@pytest.mark.parametrize("products", all_products)
def test_soma_one_products(usuario_finish_produto):

    subtotal = soma_total(subtotal_checkout(usuario_finish_produto))
    tax = soma_total(tax_checkout(usuario_finish_produto))
    total = soma_total(total_checkout(usuario_finish_produto))

    assert round(subtotal + tax, 2) ==round(total, 2)

#Teste com todos os produtos adicionados no checkout final
def test_finish_all(usuario_finish):
    subtotal = soma_total(subtotal_checkout(usuario_finish))
    tax = soma_total(tax_checkout(usuario_finish))
    total = soma_total(total_checkout(usuario_finish))

    assert round(subtotal + tax, 2) == round (total, 2)