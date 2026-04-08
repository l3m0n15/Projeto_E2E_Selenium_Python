from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def fazer_login(driver, username_text,password_text):
    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name")))
    username.send_keys(username_text)

    password = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='password']")))
    password.send_keys(password_text)

    button_login = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='submit-button btn_action']" )))
    button_login.click()

    
def error_login(driver):
    wait = WebDriverWait(driver, 10)
    error_login = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    
    return error_login.text