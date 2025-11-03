import allure
from locators.checkout_info import Loc
from appium.webdriver.common.appiumby import AppiumBy

class CheckoutInfoPage:
    def __init__(self, driver):
        self.driver = driver
    
    def inputFirstName(self, firstname):
        with allure.step("Masukan First Name"):
            self.driver.find_element(AppiumBy.XPATH,Loc.inputFirstName).send_keys(firstname)
    
    def inputLastName(self, lastname):
        with allure.step("Masukan First Name"):
            self.driver.find_element(AppiumBy.XPATH,Loc.inputLastName).send_keys(lastname)

    def inputPostalCode(self, postalcode):
        with allure.step("Masukan First Name"):
            self.driver.find_element(AppiumBy.XPATH,Loc.inputPostalCode).send_keys(postalcode)
    
    def clickContinue(self):
        with allure.step("Klik button continue"):
            self.driver.find_element(AppiumBy.XPATH,Loc.button_continue).click()