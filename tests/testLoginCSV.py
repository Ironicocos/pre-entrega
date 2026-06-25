from pages.login_page import LoginPage
from utils.dataReader import read_users_csv
import pytest

@pytest.mark.parametrize("user", read_users_csv())
def test_login(driver,user):
    loginPage = LoginPage(driver)

    loginPage.login(user["username"], user["password"])
    if user["valid"] == "true":
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    else: 
        error = loginPage.getErrorMessageContent()
        assert "Epic sadface" in error