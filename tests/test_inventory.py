from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.inventory_page import InventoryPage
from utils.logger import logger

def testDisplayedItems(login_in_driver):
    logger.info("Inicializando el driver para testDisplayedItems")
    inventoryPage = InventoryPage(login_in_driver)
    logger.info("Calculando cantidad de items disponibles...")
    itemsCount = inventoryPage.availableItems()
    logger.info("Mostrando cantidad de items disponibles...")
    print(f"Cantidad de productos disponibles: {itemsCount}")
    logger.info("Verificando cantidad de items")
    assert itemsCount > 0, "No hay items disponibles"

def testCartItems(login_in_driver):
    logger.info("Inicializando el driver para testCartItems")
    inventoryPage = InventoryPage(login_in_driver)
    logger.info("Añadiendo el primer producto al carrito")
    inventoryPage.addFirstItemToCart()
    logger.info("Verificando que el primer producto haya sigo añadido...")
    assert inventoryPage.checkCartCount() > 0, "No se pudo añadir al carrito"
    logger.info("Producto añadido de forma satisfactoria")

def testLogoutSuccessful(login_in_driver):
    logger.info("Inicializando el driver para testLogoutSuccessful")
    inventoryPage = InventoryPage(login_in_driver)
    logger.info("Accediendo al botón de cerrar sesión")
    inventoryPage.burgerMenuClick()
    inventoryPage.logoutButtonClick()
    logger.info("Verificando cierre sesión...")
    assert "https://www.saucedemo.com/" == login_in_driver.current_url, "No se cerró sesión correctamente"
    logger.info("Sesión cerrada satisfactoriamente")

def testShoppingCart(login_in_driver):
    logger.info("Inicializando el driver para testShoppingCart")
    inventoryPage = InventoryPage(login_in_driver)
    logger.info("Accediendo al carrito...")
    inventoryPage.shopCartButtonClick()
    logger.info("Verificando acceso al carrito")
    assert "https://www.saucedemo.com/cart.html" in login_in_driver.current_url, "No se pudo acceder al carrito"
    logger.info("Se accedió al carrito de forma satisfactoria")

def test_essentials(login_in_driver):
    logger.info("Inicializando el driver para test_essentials")
    inventoryPage = InventoryPage(login_in_driver)
    logger.info("Verificando que el filter menu esté siendo mostrado...")
    assert inventoryPage.filterAvailable(), "El filtro de catálogo no esta siendo mostrado"
    logger.info("El filter menu se muestra correctamente")
    logger.info("Verificando que el burger menu esté siendo mostrado...")
    assert inventoryPage.burgerAvailable(), "El ícono del menú no está siendo mostrado"
    logger.info("El burger menu se muestra correctamente")