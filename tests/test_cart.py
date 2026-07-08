from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

def testCartPage(login_in_driver):
    cartPage = CartPage(login_in_driver)
    cartPage.cartLink()
    assert "/cart.html" in login_in_driver.current_url, "Hubo un error en la redirección"
# py -m pytest -v -s tests/test_cart.py
def testItem(login_in_driver):
    cartPage = CartPage(login_in_driver)
    cartPage.addItemToCart(0)
    item1 = cartPage.getItemName(0)
    print(item1)
    cartPage.cartLink()
    print(cartPage.getCartItems())
    item2 = cartPage.getCartItem(0)
    print(item1, item2)
    assert item1 == item2, "Los objetos no coinciden"