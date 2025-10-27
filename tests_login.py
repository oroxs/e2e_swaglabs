import os
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login():
    options = UiAutomator2Options()

    options.udid = '14191JEC207644'
    options.platform_name = 'Android'
    options.app_package = 'com.swaglabsmobileapp'
    options.app_activity = 'MainActivity'
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    # Login Page
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Username"]').send_keys('standard_user')
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Password"]').send_keys('secret_sauce')
    driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-LOGIN"]').click()

    # Product Page
    judul = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="PRODUCTS"]').text
    assert judul == "PRODUCTS"
    driver.quit()

users =[("standar_user","",True),("","secret_sauce",True),("","",True)]
@pytest.mark.parametrize("username,password,error_message",users)

def test_login_failed(username,password,error_message):
    options = UiAutomator2Options()

    options.udid = '14191JEC207644'
    options.platform_name = 'Android'
    options.app_package = 'com.swaglabsmobileapp'
    options.app_activity = 'MainActivity'
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    # Login Page
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Username"]').send_keys(username)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Password"]').send_keys(password)
    driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-LOGIN"]').click()

    # Error Message
    error = driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-Error message"]').is_displayed()
    assert error == error_message
    driver.quit()
