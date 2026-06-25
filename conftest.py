import pytest 
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.dataReader import read_users_csv

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Edge(options=options)

    yield driver

    driver.quit()
@pytest.fixture
def login_in_driver(driver):
    loginPage = LoginPage(driver)
    user = read_users_csv()[0]
    loginPage.login(user["username"], user["password"])
    return driver
@pytest.fixture
def cart_page(login_in_driver):
    inventoryPage = InventoryPage(login_in_driver)
    inventoryPage.shopCartButtonClick()
    return login_in_driver