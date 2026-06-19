from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def testLoginValidation(driver):
    login_page = LoginPage(driver)
    
    login_page.login("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url, "No se redirigió correctamente"

def testWrongPasswordInput(driver):
    login_page = LoginPage(driver)    
    login_page.login("standard_user", ".")
    error = login_page.getErrorMessageContent()
    assert "Epic sadface: Username and password do not match any user in this service" in error
