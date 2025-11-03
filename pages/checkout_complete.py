import allure
from locators.checkout_complete import Loc
from appium.webdriver.common.appiumby import AppiumBy

class CheckoutCompletPage:
    def __init__(self, driver):
        self.driver = driver

    def check_title(self):
        with allure.step("Title Complete"):
            complete = self.driver.find_element(AppiumBy.XPATH,Loc.title).text
            assert complete == "CHECKOUT: COMPLETE!"