import subprocess
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# helper adb swipe
def adb_swipe(x1, y1, x2, y2, duration=300):
    """
    Swipe dengan adb (x1,y1) ke (x2,y2) selama duration ms
    """
    cmd = f"adb shell input swipe {x1} {y1} {x2} {y2} {duration}"
    subprocess.run(cmd, shell=True)

options = UiAutomator2Options()
options.udid = '14191JEC207644'
options.platform_name = 'Android'
options.app_package = 'com.swaglabsmobileapp'
options.app_activity = 'com.swaglabsmobileapp.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
driver.implicitly_wait(15)

# login
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Username"]').send_keys('standard_user')
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Password"]').send_keys('secret_sauce')
driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-LOGIN"]').click()

# buka menu
driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Toggle"]/android.widget.ImageView').click()
wait = WebDriverWait(driver, 10)

# tambah 3 produk
for i in range(3):
    el = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-ADD TO CART"])[1]'))
    )
    el.click()

# buka cart
driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]').click()

# scroll sampai ketemu CHECKOUT
checkout_btn = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(false).instance(0))'
    '.scrollIntoView(new UiSelector().text("CHECKOUT").instance(0));'
)
checkout_btn.click()

# isi form checkout
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-First Name"]').send_keys('Al')
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Last Name"]').send_keys('Fani')
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Zip/Postal Code"]').send_keys('1')
driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-CONTINUE"]').click()

# scroll sampai ketemu FINISH
finish_btn = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(false).instance(0))'
    '.scrollIntoView(new UiSelector().text("FINISH").instance(0));'
)
finish_btn.click()

# kembali ke home
driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-BACK HOME"]').click()

sleep(15)