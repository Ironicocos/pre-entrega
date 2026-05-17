from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def inventory(driver):
    driver.get("https://www.saucedemo.com/")

    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    password.send_keys(Keys.RETURN)

    titulo = driver.find_element(By.CLASS_NAME, "title").text

    return titulo
    
