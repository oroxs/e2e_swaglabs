import allure
from locators.checkout_complete import Loc
from appium.webdriver.common.appiumby import AppiumBy

class CheckoutCompletPage:
    def __init__(self, driver):
        self.driver = driver