from pages.login_page import LoginPage
from utils.dataReader import read_users_csv
import pytest
from utils.logger import logger
@pytest.mark.parametrize("user", read_users_csv())
def test_login(driver,user):
    logger.info("Inicializando el driver para test_login")
    loginPage = LoginPage(driver)
    logger.info("Ingresando credenciales...")
    loginPage.login(user["username"], user["password"])
    logger.info("Verificando que las credenciales sean correctas...")
    if user["valid"] == "true":
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        logger.info("Se inició sesión correctamente")
    else: 
        error = loginPage.getErrorMessageContent()
        assert "Epic sadface" in error
        logger.info("Las credenciales son incorrectas o hay campos vacios")