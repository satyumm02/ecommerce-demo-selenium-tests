import pytest
from selenium import webdriver
from login_page import LoginPage
from checkout_page import CheckoutPage
from products_page import ProductsPage
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()

def test_full_checkout(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    product_page = ProductsPage(driver)
    product_page.add_first_product_to_cart()

    checkout = CheckoutPage(driver)
    checkout.go_to_cart()
    checkout.checkout()
    checkout.fill_checkout_info("Sat", "Kum", "890")
    checkout.finish()
    checkout_message = checkout.finish_message()
    assert checkout_message == "Thank you for your order!"