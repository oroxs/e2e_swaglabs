import allure
from appium.webdriver.common.appiumby import AppiumBy
from locators.product import Loc

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_product_page(self):
        with allure.step("Masuk ke halaman product page"):
            judul = self.driver.find_element(AppiumBy.XPATH,Loc.product_title).text
            assert judul == "PRODUCTS"
    
    def select_product(self):
        with allure.step("Pilih product yang diinginkan"):
            product1 = self.driver.find_element(AppiumBy.XPATH,Loc.product1).text
            price1 = product1.replace("$", "")
            self.driver.find_element(AppiumBy.XPATH, Loc.btn_product1).click()
            product2 = self.driver.find_element(AppiumBy.XPATH,Loc.product2).text
            price2 = product2.replace("$", "")
            self.driver.find_element(AppiumBy.XPATH, Loc.btn_product2).click()

            total = float(price1) + float(price2)
            assert total == 39.98
    
    def click_icon_cart(self):
        with allure.step("Klik icon keranjang"):
            self.driver.find_element(AppiumBy.XPATH, Loc.icon_cart).click()