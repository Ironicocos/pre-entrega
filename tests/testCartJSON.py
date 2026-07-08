from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.dataReader import read_products_json
from utils.logger import logger

def testCartPage(login_in_driver):
    logger.info("Inicializando el driver para testCartPage")
    cartPage = CartPage(login_in_driver)
    logger.info("Accediendo al carrito...")
    cartPage.cartLink()
    logger.info("Verificando que la url se la correcta...")
    assert "/cart.html" in login_in_driver.current_url, "Hubo un error en la redirección"
    logger.info("Se accedió a la página esperada correctamente")

def testItem(login_in_driver):
    logger.info("Inicializando el driver para testItem")
    cartPage = CartPage(login_in_driver)
    inventoryPage = InventoryPage(login_in_driver)
    logger.info("Obteniendo los productos desplegados en el inventario...")
    items = read_products_json()
    logger.info("Añadiendo productos por nombre...")
    for item in items:
        inventoryPage.addItemByName(item["nombre"])
    logger.info("Accediendo al carrito...")
    inventoryPage.shopCartButtonClick()
    logger.info("Obteniendo los productos del carrito...")
    cartItems = cartPage.getItemsInfo()
    logger.info("Verificando que los productos del JSON y los del carrito coincidan")
    for expectedItem in items:
        found = False
        for cartItem in cartItems:
            print(cartItem["name"])
            if(cartItem["name"] in expectedItem["nombre"] and cartItem["value"] in expectedItem["precio"]):
                found = True
            
    assert found, f"Producto incorrecto o faltante {expectedItem["nombre"]} {expectedItem["precio"]}"
    logger.info("Todos los productos coinciden con los esperados")