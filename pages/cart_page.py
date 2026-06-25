from selenium import webdriver
from selenium.webdriver.common.by import By
class CartPage:
    def __init__(self, login_in_driver):
        self.driver = login_in_driver
        self.__cartItemsInfo = (By.CSS_SELECTOR, "[data-test='inventory-item']")
        self.__cartLink = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        self.__displayedItems = (By.CLASS_NAME, "inventory_item")
        self.__itemValue = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
        self.__itemName = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")

    def getItems(self):
        return self.driver.find_elements(*self.__cartItemsInfo)

    def getItemsInfo(self):
        items = self.getItems()
        itemList = []
        for item in items:
            itemName = item.find_element(*self.__itemName).text
            itemValue = item.find_element(*self.__itemValue).text

            itemList.append([
                {
                    "name": itemName,
                    "value": itemValue
                }
            ])
        return itemList
    
