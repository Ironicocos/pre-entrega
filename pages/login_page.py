from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.__usernameInput = (By.ID, "user-name")
        self.__passwordInput = (By.ID, "password")
        self.__loginButton = (By.ID, "login-button")
        self.__credentialsErrorMessage = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
    
    def inputUsername(self, usuario):
        self.driver.find_element(*self.__usernameInput).send_keys(usuario)

    def inputPassword(self, password):
        self.driver.find_element(*self.__passwordInput).send_keys(password)

    def buttonClick(self):
        self.driver.find_element(*self.__loginButton).click()
    
    def login(self, usuario, password):
        self.open()
        self.inputUsername(usuario)
        self.inputPassword(password)
        self.buttonClick()

    def getErrorMessageContent(self):
        return self.driver.find_element(*self.__credentialsErrorMessage).text
    