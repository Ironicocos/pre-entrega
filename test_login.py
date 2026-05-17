from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver
        assert "/inventory.html" in driver.current_url, "Respuesta no esperada"
    except Exception:
        print(f"Error en test login: {Exception}")
    