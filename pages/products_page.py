from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Titulo Loja
def title_product(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_title_product = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']" )))
    return located_title_product.is_displayed()

#Produto name
def add_very_products(usuario_login, name_products: list):
    wait = WebDriverWait(usuario_login, 5)
    for name_product in name_products:
        located_very_products = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{name_product}']/ancestor::a")))
        located_very_products.click()
#Está colocando a função dentro do loop do FOR, assim nao preciso chamar elas no TEST_PRODUCTS.PY
        button_add(usuario_login)
#Está colocando a função dentro do loop do FOR, assim nao preciso chamar elas no TEST_PRODUCTS.PY
        back_shopping(usuario_login)
        
#Botão adicionar ao carrinho
def button_add(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_button_add_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='add-to-cart']")))
    located_button_add_cart.click()

#Voltar para a loja
def back_shopping(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_back_to_products = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="back-to-products"]')))
    located_back_to_products.click()

#Localizando valor do icone do carrinho
def checkout_cart(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_checkout_cart = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-link']")))
    return located_checkout_cart.text
    
#Acessando icone do carrinho
def open_cart(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_open_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')))
    located_open_cart.click()

#Preço dos produtos
def price_products(usuario_login, name_products):
    wait = WebDriverWait(usuario_login, 5)
    for name_product in name_products:
        located_price_products = wait.until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{name_product}']/../../..//div[@data-test='inventory-item-price']")))
    return located_price_products.text