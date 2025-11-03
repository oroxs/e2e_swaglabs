import allure
from pages.login import LoginPage
from pages.product import ProductPage
from pages.cart import CartPage
from pages.checkout_info import CheckoutInfoPage
from pages.checkout_overview import CheckoutOverviewPage
from pages.checkout_complete import CheckoutCompletPage

@allure.title("Login Test")
@allure.description("Test Untuk Login") 
@allure.severity(allure.severity_level.CRITICAL) 

def test_login(setup):    
   login = LoginPage(setup)
   product = ProductPage(setup)
   cart = CartPage(setup)
   info = CheckoutInfoPage(setup)
   overview = CheckoutOverviewPage(setup)
   complete = CheckoutCompletPage (setup)

   login.inputUsername('standard_user')
   login.inputPassword('secret_sauce')
   login.clickButtonLogin()
   product.check_product_page()
   product.select_product()
   product.click_icon_cart()
   cart.check_title()
   cart.click_checkout()
   info.check_title()
   info.inputFirstName('Vedy')
   info.inputLastName('Aditya')
   info.inputPostalCode('123123')
   info.clickContinue()
   overview.check_title()
   overview.scroll_down()
   overview.check_total_price()
   overview.check_total_tax()
   overview.check_grand_total()
   overview.click_finish_button()
   complete.check_title()


