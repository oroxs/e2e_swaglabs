import allure
from locators.login import Loc
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def inputUsername(self, username):
        with allure.step("Masukan user"):
            self.driver.find_element(AppiumBy.XPATH,Loc.input_username).send_keys(username)
    
    def inputPassword(self, password): 
        with allure.step("Masukan Password"):
            self.driver.find_element(AppiumBy.XPATH,Loc.input_password).send_keys(password)
    
    def clickButtonLogin(self):
        with allure.step("Click Button Login"):
            self.driver.find_element(AppiumBy.XPATH,Loc.click_login).click()