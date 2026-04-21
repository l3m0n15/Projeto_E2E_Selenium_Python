from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Título da página final
def title_finish(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_title_finish = wait.until (
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="title"]')))
    return located_title_finish.is_displayed()

#Produtos que estão na aba final
def products_finish(usuario_login, products: list):
    wait = WebDriverWait(usuario_login, 5)
    results = []
    for product in products:
        located_products_finish = wait.until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{product}']")))
        results.append(located_products_finish.is_displayed())
    return results

#Valor do 'SUBTOTAL' dos produtos
def subtotal_checkout(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_subtotal_checkout = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="subtotal-label"]')))
    return located_subtotal_checkout.text
    
#Valor do 'TAX' dos produtos
def tax_checkout(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_tax_checkout = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="tax-label"]')))
    return located_tax_checkout.text

#Valor do 'TOTAL' dos produtos
def total_checkout(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_total_checkout = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="total-label"]')))
    return located_total_checkout.text

#Soma total de todos os valores
def soma_total(texto):
    valor = texto.split("$")[1]
    return float(valor)

#Botão de finalizar toda a compra
def go_to_finish(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_go_to_finish = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="finish"]')))
    located_go_to_finish.click()

#Botão de cancelar toda a compra
def button_cancel(usuario_login):
    wait = WebDriverWait(usuario_login, 5) 
    located_button_cancel = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="cancel"]')))
    located_button_cancel.click()