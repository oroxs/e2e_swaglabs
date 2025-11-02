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