from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.inventory_page import InventoryPage

def testDisplayedItems(login_in_driver):
    inventoryPage = InventoryPage(login_in_driver)
    itemsCount = inventoryPage.availableItems()
    print(f"Cantidad de productos disponibles: {itemsCount}")
    assert itemsCount > 0, "No hay items disponibles"

def testCartItems(login_in_driver):
    inventoryPage = InventoryPage(login_in_driver)
    inventoryPage.addFirstItemToCart()
    assert inventoryPage.checkCartCount() > 0, "No se pudo añadir al carrito"

def testLogoutSuccessful(login_in_driver):
    inventoryPage = InventoryPage(login_in_driver)
    inventoryPage.burgerMenuClick()
    inventoryPage.logoutButtonClick()
    assert "https://www.saucedemo.com/" == login_in_driver.current_url, "No se cerró sesión correctamente"

def testShoppingCart(login_in_driver):
    inventoryPage = InventoryPage(login_in_driver)
    inventoryPage.shopCartButtonClick()
    assert "https://www.saucedemo.com/cart.html" in login_in_driver.current_url, "No se pudo acceder al carrito"