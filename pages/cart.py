import allure
from locators.cart import Loc
from appium.webdriver.common.appiumby import AppiumBy

class CartPage:
    def __init__(self, driver):
        self.driver = driver
    
    def check_title(self):
        with allure.step("Check Title"):
            check_title = self.driver.find_element(AppiumBy.XPATH, Loc.title).text
            assert check_title == 'YOUR CART'
        
    def click_checkout(self):
        with allure.step("Klik button checkout"):
            checkout_btn = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(false).instance(0))'
            '.scrollIntoView(new UiSelector().text("CHECKOUT").instance(0));'
            )
            checkout_btn.click()