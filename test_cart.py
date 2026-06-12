from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.cart_page import CartPage

def testCartPage(cart_page):
    assert "/cart.html" in cart_page.current_url, "Hubo un error en la redirección"

def testItem(cart_page):
    cartPage = CartPage(cart_page)
    addedItem = cartPage.addItemToCart(1)
    cartItems = cartPage.getCartItems(0)
    assert cartPage.checkItems(addedItem, cartItems) == True, "Los objetos no coinciden"