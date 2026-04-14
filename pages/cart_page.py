from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Itens no carrinho
def products_cart(driver,name_products: list):
    wait = WebDriverWait(driver, 10)
    for name_product in name_products:

#Localizando itens no carrinho
        located_product = wait.until(
            EC.visibility_of_element_located((By.XPATH, f"//div[contains(@class,'cart_list')]//div[contains(@class,'inventory_item_name') and text()='{name_product}']")))
        
#Verificação para sabre se o elemetno está visivel
    return located_product.is_displayed()
 
#Botão de remover do carrinho
def remove_button(driver, name_products: list):
    wait = WebDriverWait(driver, 10)
    for name_product in name_products:

#Localizando botão de remover do carrinho
        located_remove_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(@data-test,'cart-list')]//div[contains(@data-test, 'remove-sauce-labs-backpack') and text()='{name_product}']")))
        
    located_remove_button.click()

#Botão de continuar = 'Checkout'
def continue_button_cart(driver):
    wait = WebDriverWait(driver, 10)
    
#localizando botão de continuar para proxima pagina
    located_continue_button_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='checkout']")))
    
    located_continue_button_cart.click()

#Botão de voltar para a loja
def back_button_cart(driver):
    wait = WebDriverWait(driver, 10)

#Localizando botão de voltar para a loja
    located_back_button_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="continue-shopping"]')))
    
    located_back_button_cart.click()

