from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver

#def test_inventory(login_in_driver):
#    driver = login_in_driver
#    titulo = driver.find_element(By.CLASS_NAME, "title").text
#    assert titulo == "Products", "El título no coincide"

def test_inventory(login_in_driver):
    driver = login_in_driver
    titulo = driver.title
    assert titulo == "Swag Labs", "Título no esperado"

def test_shoppingCart(login_in_driver):
    driver = login_in_driver
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    addedToCart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert addedToCart == "1", "No se agregó al carrito"

def test_shoppingCart(login_in_driver):
    driver = login_in_driver
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    addedItems = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
    driver.find_element(By.ID, "shopping_cart_container").click()
    displayedItem = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
    assert displayedItem == addedItems, "No es el producto seleccionado"

def test_displayedItems(login_in_driver):
    driver = login_in_driver
    availableItems = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(availableItems) > 0

def test_essentials(login_in_driver):
    driver = login_in_driver
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filter = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed(), "El ícono del menú no está siendo mostrado"
    assert filter.is_displayed(), "El filtro de catálogo no esta siendo mostrado"