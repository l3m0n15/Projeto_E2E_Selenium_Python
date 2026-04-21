from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Função base driver/Login principal
def fazer_login(driver, username_text,password_text):
    wait = WebDriverWait(driver, 5)

#Username localizado
    username = wait.until(
        EC.element_to_be_clickable((By.ID, "user-name")))
    username.clear()
    username.send_keys(username_text)

#Password localizado
    password = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='password']")))
    password.clear()
    password.send_keys(password_text)

#Botão de login localizado
    located_go_to_login = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='submit-button btn_action']" )))
    located_go_to_login.click()

#Erro de login
def error_login(driver):
    wait = WebDriverWait(driver, 5)
    located_error_login = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    return located_error_login.text