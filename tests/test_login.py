import allure
from pages.login import LoginPage
from pages.product import ProductPage

@allure.title("Login Test")
@allure.description("Test Untuk Login") 
@allure.severity(allure.severity_level.CRITICAL) 

def test_login(setup):    
   login = LoginPage(setup)
   product = ProductPage(setup)

   login.inputUsername('standard_user')
   login.inputPassword('secret_sauce')
   login.clickButtonLogin()
   product.check_product_page()
