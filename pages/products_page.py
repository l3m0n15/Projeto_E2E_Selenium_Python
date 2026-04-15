from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Titulo Loja
def title_product(usuario_login):
    wait = WebDriverWait(usuario_login, 10)
#Localizador do texto da loja
    located_title_product = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']" )))
#Retornando o titulo da loja
    return located_title_product.is_displayed()

#Produto name
def add_very_products(usuario_login, name_products: list):
    wait = WebDriverWait(usuario_login, 10)
    for name_product in name_products:
#Localizador por name do Produto
        located_very_products = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{name_product}']/ancestor::a")))
#clique no nome do produto
        located_very_products.click()
#Está colocando a função dentro do loop do FOR, assim nao preciso chamar elas no TEST_PRODUCTS.PY
        button_add(usuario_login)
#Está colocando a função dentro do loop do FOR, assim nao preciso chamar elas no TEST_PRODUCTS.PY
        back_shopping(usuario_login)
        

#Botão adicionar ao carrinho
def button_add(usuario_login):
    wait = WebDriverWait(usuario_login, 10)
#Localizando botão do carrinho
    located_button_add_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='add-to-cart']")))
#clique no botão para adicionar
    located_button_add_cart.click()


#Voltar para a loja
def back_shopping(usuario_login):
    wait = WebDriverWait(usuario_login, 10)
#Localizando, botão de voltar para loja
    located_back_to_products = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="back-to-products"]')))
#clique no botão para voltar
    located_back_to_products.click()


#Localizando valor do icone do carrinho
def checkout_cart(usuario_login):
    wait = WebDriverWait(usuario_login, 10)
    located_checkout_cart = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-link']")))
#retornando a quantidade de item no carrinho
    return located_checkout_cart.text
    
#Acessando icone do carrinho
def open_cart(usuario_login):
    wait = WebDriverWait(usuario_login, 10)
    located_open_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')))
#Clicando no icone do carrinho
    located_open_cart.click()

    