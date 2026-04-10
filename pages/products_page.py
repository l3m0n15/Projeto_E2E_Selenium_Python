from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def add_very_products(driver, name_product):
    wait = WebDriverWait(driver, 10)

    located_very_products = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//button[contains(@class,'btn btn_primary btn_small btn_inventory ' and text()= '{name_product}']")))

    located_very_products.click()



def add_product(driver, name_product):
    wait = WebDriverWait(driver, 10)

    locator_product = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'inventory_item_name ' and text()='{name_product}']/ancestor::ID")))
    
    button_add_cart = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='add-to-cart']")))

    button_add_cart.click()

def checkout_cart(driver):
    wait = WebDriverWait(driver, 10)

    located_checkout_cart = wait.until(
        EC._element_if_visible((By.CSS_SELECTOR, "[data-test='shopping-cart-link']")))
        
    return located_checkout_cart.text
    
def open_cart(driver):
    wait = WebDriverWait(driver, 10)

    located_open_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')))
    
    located_open_cart.click()

    