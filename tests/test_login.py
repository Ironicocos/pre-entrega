from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.logger import logger

def testLoginValidation(driver):
    logger.info("Inicializando el driver para testLoginValidation")
    login_page = LoginPage(driver)

    logger.info("Ingresando credenciales")    
    login_page.login("standard_user", "secret_sauce")
    logger.info("Iniciando sesion...")
    assert "/inventory.html" in driver.current_url, "No se redirigió correctamente"
    logger.info("Sesión iniciada correctamente")

def testWrongPasswordInput(driver):
    logger.info("Inicializando el driver para testWrongPasswordInput")
    login_page = LoginPage(driver)    
    logger.info("Ingresando credenciales incorrectas")
    login_page.login("standard_user", ".")
    logger.info("Capturando mensaje de error")
    error = login_page.getErrorMessageContent()
    logger.info("Iniciando sesión")
    assert "Epic sadface: Username and password do not match any user in this service" in error
    logger.info("Sesión no iniciada")
