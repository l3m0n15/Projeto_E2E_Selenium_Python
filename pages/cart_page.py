from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def products_cart(driver,name_product):
    wait = WebDriverWait(driver, 10)

    located_product = wait.until(
        EC.visibility_of_element_located((By.XPATH, f"//div[contains(@class,'cart_list')]//div[contains(@class,'inventory_item_name') and text()='{name_product}']")))
    
    return located_product.is_displayed()

def remove_button(driver, remove_button):
    wait = WebDriverWait(driver, 10)
    
    located_remove_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//div[contains(@data-test,'cart-list')]//div[contains(@data-test, 'remove-sauce-labs-backpack') and text()='{remove_button}']")))
    
    located_remove_button.click()