from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.dataReader import read_products_json
'''
def testCartPage(cart_page):
    assert "/cart.html" in cart_page.current_url, "Hubo un error en la redirección"
'''
def testItem(login_in_driver):
    cartPage = CartPage(login_in_driver)
    inventoryPage = InventoryPage(login_in_driver)
    items = read_products_json()

    for item in items:
        inventoryPage.addItemByName(item["nombre"])

    inventoryPage.shopCartButtonClick()

    cartItems = cartPage.getItemsInfo()
    for expectedItem in items:
        found = False
        for cartItem in cartItems:
            if(cartItem[0]["name"] in expectedItem["nombre"] and cartItem[0]["value"] in expectedItem["precio"]):
                found = True
        assert found, f"Producto incorrecto o faltante {expectedItem["nombre"]} {expectedItem["precio"]}"