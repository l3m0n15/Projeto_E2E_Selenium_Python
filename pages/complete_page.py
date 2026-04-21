from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Titulo da pagina complete
def title_complete(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_title_complete = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="title"]')))
    return located_title_complete.text

#Botao back home = volta para inventory
def go_to_home(usuario_login):
    wait = WebDriverWait(usuario_login, 5)
    located_go_to_home = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="back-to-products"]')))
    located_go_to_home.click()
