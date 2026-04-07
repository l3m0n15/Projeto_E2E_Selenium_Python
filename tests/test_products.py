from pages.products_page import add_product
import pytest



@pytest.mnark.parametrize("produtos", [
        

        ('Sauce Labs Backpack'),
        ('Sauce Labs Bike Light'),
        ('Sauce Labs Bolt T-Shirt'),
        ('Sauce Labs Fleece'),
        ('Sauce Labs Fleece Jacket'),
        ('Sauce Labs Onesie'),
        ('Test.allTheThings() T-Shirt (Red)')
    ])

def test_add_product(driver, produtos):
    add_product()