from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Titulo da pagina do carrinho
def title_cart(usuario_login):
    wait = WebDriverWait(usuario_login, 10)
    located_title_cart = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']")))
    return located_title_cart.is_displayed()

#Itens no carrinho
def products_cart(usuario_login,name_products: list):
    wait = WebDriverWait(usuario_login, 10)
    results = []
    for name_product in name_products:
        located_product = wait.until(
            EC.visibility_of_element_located((By.XPATH, f"//div[contains(@class,'cart_list')]//div[contains(@class,'inventory_item_name') and text()='{name_product}']")))
        results.append(located_product.is_displayed())
    return results

#Botão de remover do carrinho
def remove_button(usuario_login, name_products: list):
    wait = WebDriverWait(usuario_login, 10)
    for name_product in name_products:
        located_remove_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@data-test= 'inventory-item-name' and text()='{name_product}']/../..//button[contains(@data-test,'remove')]")))
        located_remove_button.click()

#Botão de continuar = 'Checkout'
def usuario_cart(usuario_login):
    wait = WebDriverWait(usuario_login, 10)
    located_usuario_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='checkout']")))
    located_usuario_cart.click()

#Botão de voltar para a loja
def back_button_cart(usuario_login):
    wait = WebDriverWait(usuario_login, 10)
    located_back_button_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="continue-shopping"]')))
    located_back_button_cart.click()

#Preço do produto dentro do carrinho
def preco_product_cart(usuario_login, name_products):
    wait = WebDriverWait(usuario_login, 5)
    results = []
    for name_product in name_products:
        located_product_cart = wait.until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{name_product}']/../..//div[contains(@data-test, 'inventory-item-price')]")))
        results.append(located_product_cart.text)
    return results

