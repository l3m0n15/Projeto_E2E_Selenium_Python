from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Botão localizado por nome 
def add_very_products(usuario_login, name_products: list):
    wait = WebDriverWait(usuario_login, 10)
    for name_product in name_products:
        located_very_products = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(@data-test,'item-0-title-link')]//div[contains(@data-test,'inventory-item-name') and text()='{name_product}']")))
#clique no nome do produto
    located_very_products.click()

#Botão adicionar ao carrinho
def button_add(usuario_login):
    wait = WebDriverWait(usuario_login, 10)
    located_button_add_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='add-to-cart']")))

#clique no botão para adicionar
    located_button_add_cart.click()

#Localizando valor do icone do carrinho
def checkout_cart(usuario_login):
    wait = WebDriverWait(usuario_login, 10)
    located_checkout_cart = wait.until(
        EC._element_if_visible((By.CSS_SELECTOR, "[data-test='shopping-cart-link']")))
#retornando a quantidade de item no carrinho
    return located_checkout_cart.text
    

#Acessando icone do carrinho
def open_cart(usuario_login):
    wait = WebDriverWait(usuario_login, 10)

    located_open_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')))
    
#Clicando no icone do carrinho
    located_open_cart.click()

    