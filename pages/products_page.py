from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def add_product(driver, name_product):
    wait = WebDriverWait(driver, 10)

    locator_product = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'inventory_item_name ' and text()='{name_product}']/ancestor::ID")))
    
    button_add_cart = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='add-to-cart']")))

    button_add_cart.click()



    produtos = [
        ('Sauce Labs Backpack'),
        ('Sauce Labs Bike Light'),
        ('Sauce Labs Bolt T-Shirt'),
        ('Sauce Labs Fleece Jacket'),
        ('Sauce Labs Onesie'),
        ('Test.allTheThings() T-Shirt (Red)')
    ]