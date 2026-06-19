from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class InventoryPage:
    def __init__(self, login_in_driver):
        self.driver = login_in_driver
        self.__burgerMenuDisplay = (By.ID, "react-burger-menu-btn")
        self.__logoutButton = (By.ID, "logout_sidebar_link")
        self.__shoppingCartButton = (By.CLASS_NAME, "shopping_cart_link")
        self.__displayedItems = (By.CLASS_NAME, "inventory_item")
        self.__itemsCount = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
        self.__filter = (By.CLASS_NAME, "product_sort_container")

    def burgerMenuClick(self):
        self.driver.find_element(*self.__burgerMenuDisplay).click()

    def filterAvailable(self):
        return self.driver.find_element(*self.__filter).is_displayed()
    
    def burgerAvailable(self):
        return self.driver.find_element(*self.__burgerMenuDisplay).is_displayed()

    def logoutButtonClick(self):
        element = WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable(self.__logoutButton)
        )
        element.click()

    def shopCartButtonClick(self):
        self.driver.find_element(*self.__shoppingCartButton).click()

    def availableItems(self):
        return len(self.driver.find_elements(*self.__displayedItems))
    
    def itemsInfo(self):
        return self.driver.find_elements(*self.__displayedItems)
    
    def getFirstItemName(self):
        return self.itemsInfo()[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text

    def addFirstItemToCart(self):
        self.itemsInfo()[0].find_element(By.TAG_NAME, 'button').click()

    def checkCartCount(self):
        return int(self.driver.find_element(*self.__itemsCount).text)
    
        
