import allure
from locators.checkout_overview import Loc
from appium.webdriver.common.appiumby import AppiumBy

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
    
    def check_title(self):
        with allure.step("Check Title"):
            check_title = self.driver.find_element(AppiumBy.XPATH, Loc.title).text
            assert check_title == 'CHECKOUT: OVERVIEW'

    def click_finish_button (self):
        with allure.step("Klik button finish"):
            finish_btn=self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(false).instance(0))'
            '.scrollIntoView(new UiSelector().text("FINISH").instance(0));'
            )
            finish_btn.click()
            
    def scroll_down (self):
        with allure.step("scroll down"):
            self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(false).instance(0))'
            '.scrollIntoView(new UiSelector().text("FINISH").instance(0));'
            )

    def check_total_price (self):
        with allure.step("Check Harga"):
            item_total = self.driver.find_element(AppiumBy.XPATH, Loc.total_price).text
            itemTotal = item_total.replace("Item total: $", "")
            assert float(itemTotal) == 39.98

    def check_total_tax (self):
        with allure.step("Check Pajak"):
            tax = self.driver.find_element(AppiumBy.XPATH, Loc.tax).text
            pajak = tax.replace("Tax: $", "")
            assert float(pajak) == 3.20

    def check_grand_total (self):
        with allure.step("Check Total Bayar"):
            grand_total = self.driver.find_element(AppiumBy.XPATH, Loc.total).text
            grandTotal = grand_total.replace("Total: $", "")
            assert float(grandTotal) == 43.18