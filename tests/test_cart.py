from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.cart_page import CartPage

def testCartPage(cart_page):
    assert "/cart.html" in cart_page.current_url, "Hubo un error en la redirección"

def testItem(cart_page):
    cartPage = CartPage(cart_page)
    cartPage.addItemToCart(0)
    item1 = cartPage.getItemName(0)
    cartPage.returnToCart()
    item2 = cartPage.cartItemsInfo(0)
    print(item1, item2)
    assert item1 == item2, "Los objetos no coinciden"