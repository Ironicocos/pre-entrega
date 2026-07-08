from selenium import webdriver
from selenium.webdriver.common.by import By
class CartPage:
    def __init__(self, login_in_driver):
        self.driver = login_in_driver
        self.__cartItems = (By.CSS_SELECTOR, "[data-test='inventory-item']")
        self.__cartLink = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        self.__displayedItems = (By.CLASS_NAME, "inventory_item")
        self.__inventoryButton = (By.ID, 'continue-shopping')
        self.__itemValue = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
        self.__itemName = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
        self.__addItemButton = (By.TAG_NAME, 'button')

    def cartLink(self):
        self.driver.find_element(*self.__cartLink).click()

    def continueShopping(self):
        self.driver.find_element(*self.__inventoryButton).click()

    def getItems(self):
        return self.driver.find_elements(*self.__displayedItems)
    
    def addItemToCart(self, index):
        self.getItems()[index].find_element(*self.__addItemButton).click()

    def getCartItems(self):
        return self.driver.find_elements(*self.__cartItems)
    
    def getCartItem(self, index):
        return self.getCartItems()[index].find_element(*self.__itemName).text

    def cartLink(self):
        self.driver.find_element(*self.__cartLink).click()

    def getItemName(self, index):
        return self.getItems()[index].find_element(*self.__itemName).text

    def getItemsInfo(self):
        items = self.getCartItems()
        itemList = []
        for item in items:
            itemName = item.find_element(*self.__itemName).text
            itemValue = item.find_element(*self.__itemValue).text

            itemList.append(
                {
                    "name": itemName,
                    "value": itemValue
                }
            )
        return itemList
    
