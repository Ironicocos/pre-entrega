from selenium import webdriver
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, cart_page):
        self.driver = cart_page
        self.__inventoryLink = (By.ID, "continue-shopping")
        self.__cartItemsInfo = (By.CSS_SELECTOR, "[data-test='inventory-item']")
        self.__cartLink = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        self.__displayedItems = (By.CLASS_NAME, "inventory_item")
    
    def returnToInventory(self):
        self.driver.find_element(*self.__inventoryLink).click()

    def returnToCart(self):
        self.driver.find_element(*self.__cartLink).click()

    def itemsInfo(self):
        if "/cart.html" in self.driver.current_url:
            self.returnToInventory()
        return self.driver.find_elements(*self.__displayedItems)

    def addItemToCart(self, index):
        self.returnToInventory()
        itemInfo = self.itemsInfo()
        itemName =  itemInfo[index].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
        itemInfo[index].find_element(By.TAG_NAME, 'button').click()
        return itemName
    
    def cartItemsInfo(self):
        if "/inventory.html" in self.driver.current_url:
            self.returnToCart()
        return self.driver.find_elements(*self.__cartItemsInfo)

    def getCartItems(self, index):
        if "/inventory.html" in self.driver.current_url:
            self.returnToCart()
        itemInfo = self.cartItemsInfo()
        itemName = itemInfo[index].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
        return itemName

    def checkItems(self, item1, item2):
        if item1 == item2:
            return True