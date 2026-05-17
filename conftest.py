import pytest 
from selenium import webdriver
from loginPage import login

@pytest.fixture
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Edge(options=options)

    yield driver

    driver.quit

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver