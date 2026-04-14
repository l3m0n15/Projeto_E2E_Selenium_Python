from pages.login_page import fazer_login, error_login
import pytest


@pytest.mark.parametrize("username_text, password_text, esperado",[
    ("standard_user", "secret_sauce", "sucesso"),
    ("errado", "secret_sauce","Epic sadface: Username and password"),
    ("standard_user", "errado","Epic sadface: Username and password"),
    ("", "", "Epic sadface: Username is required")
    ("standard_user", '', 'Epic sadface: Password is required')
    ("", 'secret_sauce', 'Epic sadface: Username is required')
])

def test_fazer_login(driver, username_text, password_text, esperado):
    fazer_login(driver, username_text, password_text)

    if esperado =="sucesso":
        assert "inventory.html" in driver.current_url

    else:
        assert "O login falhou!" in error_login(driver)



   