from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Título do checkout
def title_text(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
#Localizando título do checkout
    located_title_text = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="title"]')))
#Retornando localizador checkout
    return located_title_text.is_displayed()

#Preenchimento do usuário
def info_custom_user(usuario_login, First_Name, Last_Name, Postal_Code):
    wait = WebDriverWait(usuario_login, 5)

#Primeiro campo de preenchimento #1 'First Name'
    located_first_name = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="firstName"]')))
    located_first_name.clear()
    located_first_name.send_keys(First_Name)

#Segundo campo de preenchimento 2# 'Last Name'
    located_last_name = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="lastName"]')))
    located_last_name.clear()
    located_last_name.send_keys(Last_Name)

#Terceiro campo de preenchimento 3# 'Zip/Postal Code'
    located_postal_code = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="postalCode"]')))
    located_postal_code.clear()
    located_postal_code.send_keys(Postal_Code)

#Botão de continuar após preencher
    located_button_continue = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="continue"]')))
    located_button_continue.click()

#Botão de voltar para o carrinho
def back_button_cart(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_button_back = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="cancel"]')))
    located_button_back.click()

#Erro ao preencher na aba checkout
def error_checkout(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_error_checkou = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]')))
    return located_error_checkou.text


