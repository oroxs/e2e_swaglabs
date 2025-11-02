import pytest
import allure
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options

@pytest.fixture()
def setup():
    with allure.step("Buka applikasi"):
        options = UiAutomator2Options()

        options.udid = '14191JEC207644'
        options.platform_name = 'Android'
        options.app_package = 'com.swaglabsmobileapp'
        options.app_activity = 'MainActivity'
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        driver.implicitly_wait(10)
    
    yield driver
    with allure.step("Close applikasi"):
        driver.quit()