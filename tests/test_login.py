from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

#Navegador sendo acessado
driver = webdriver.Chrome()

#Webdriver definido com o nome de wait, e progarmado para até 10s
wait = WebDriverWait(driver, 5)

#Maximizando tela do navegadorm antes de abrir
driver.maximize_window()

#Entrando nesse site 
driver.get("https://www.saucedemo.com/")

#Localizando elemento de "Username" e "Password" visivil na tela
username = wait.until(
    EC.visibility_of_element_located((By.ID, "user-name")))
password = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]')))

#Preenchendo campo de "Username" e "Password"
username.send_keys('standard_user')
password.send_keys('secret_sauce')

#Localizando botão de login clicável na tela
login_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//input[@data-test="login-button"]')))

#Clicando com o botão de login
login_button.click()

# ........................... PARTE DENTRO DA LOJA DE COMPRAS............................................


#Localizando o titulo da proxima página com 
titulo = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//span[@data-test="title"]')))

#Aguarda o titulo da página "Products" ficar visível, após navegação.
assert titulo.text == "Products", f"Esperado 'Products', mas veio '{titulo.text}'"


# ADICIONAR PRODUTOS PELO NOME
def add_by_name(driver, product_name):

#Localizou o nome do produto, link clicavél
    locator_product = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//div[text()='{product_name}']/ancestor::a")))
    
#Clicou no nome do produto
    locator_product.click()

#Botão de adcionar o arrrinho, localizado
    add_product_car = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))

#Clicado e adcionado com o botão do carrinho
    add_product_car.click()

    driver.back()


@pytest.mark.parametrize("product_name",[
"Sauce-labs-backpack",
"Sauce-labs-bike-light",
"Sauce-labs-bolt-t-shirt",
"Sauce-labs-fleece-jacket",
"Sauce-labs-onesie",
"Test.allthethings()-t-shirt-(red)"
])

def test_add_by_name(driver, product_name):
    add_by_name(driver, product_name)

    assert "Remove" in driver.page_source



# REMOVER PRODUTOS
def remove_button(driver, remove_product):

    locator_remove_button = wait.until(
        EC.element_to_be_clickable((By.ID, f"{remove_product}")))
    
    locator_remove_button.click()

    return locator_remove_button

@pytest.mark.parametrize("remove_product",[
"remove-sauce-labs-backpack",
"remove-sauce-labs-bike-light",
"remove-sauce-labs-bolt-t-shirt",
"remove-sauce-labs-fleece-jacket",
"remove-sauce-labs-onesie",
"remove-test.allthethings()-t-shirt-(red)"
])

def test_remove_button(driver, remove_product):
    remove_button(driver, remove_product)
    assert "Add to cart" in driver.page_source



# ADICIONAR PRODUTOS PELA IMAGEM
def add_by_image(driver, product_img):

    #Localizador da imagem
    locator_img = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//img[@alt='{product_img}']/ancestor::a")))
    
    #Clique na imagem
    locator_img.click()

    #Localizador de botão do carrinho
    add_product_car = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
    
        #Clique na carrinho
    add_product_car.click()
    
    driver.back()

@pytest.mark.parametrize("product_img",[

"Sauce-labs-backpack",
"Sauce-labs-bike-light",
"Sauce-labs-bolt-t-shirt",
"Sauce-labs-fleece-jacket",
"Sauce-labs-onesie",
"Test.allthethings()-t-shirt-(red)"
])

def test_add_by_image(driver, product_img):
    add_by_image(driver, product_img)

    assert "Remove" in driver.page_source





# ........................... PARTE PARA ENCERRAR COMPRAS DA LOJA............................................

#botão de finalizar as compras e prosseguir localizado
button_finish = wait.until(
    EC.element_to_be_clickable((By.ID, "checkout")))


#clicando no botão de finalizar as compras
button_finish.click()

text_your_information = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "title")))

assert text_your_information.text == "Checkout: Your Information"

time.sleep(2.5)

dados = [

    (By.ID, "first-name", "André Ryan"),
    (By.NAME, "lastName", "De Paula Moreira"),
    (By.XPATH, '//input[contains(@class, "input_error form_input") and contains(@placeholder, "Zip/Postal Code")]', "06240190")
]

for by, locator, valor_usuario in dados: 
    dados_usuario = wait.until(
    EC.visibility_of_element_located((by, locator))
    )
    dados_usuario.send_keys(valor_usuario)

button_continue = wait.until(
          EC.element_to_be_clickable((By.ID, "continue"))
          )
button_continue.click()

time.sleep(1.5)




