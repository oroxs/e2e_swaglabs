import allure
from locators.checkout_overview import Loc
from appium.webdriver.common.appiumby import AppiumBy

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
    
