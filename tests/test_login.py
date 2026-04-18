from pages.login_page import fazer_login, error_login
import pytest

#Login valido
def test_login_valid(driver):
    fazer_login(driver, "standard_user", "secret_sauce",)

    assert "inventory.html" in driver.current_url

#Login error
@pytest.mark.parametrize('username_text, password_text, esperado',[

    ("errado", "secret_sauce","Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "errado","Epic sadface: Username and password do not match any user in this service"),
    ("", "", "Epic sadface: Username is required"),
    ("standard_user", '', "Epic sadface: Password is required"),
    ("", 'secret_sauce', 'Epic sadface: Username is required')
])

#test login error
def test_login_error(driver, username_text, password_text, esperado):
    fazer_login(driver, username_text, password_text)

    assert error_login(driver) == esperado 