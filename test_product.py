import pytest
from selenium import webdriver
from products_page import ProductsPage
from login_page import LoginPage
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

def test_first_product(driver) :
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    product_page = ProductsPage(driver)
    product_page.sort_by("Name (Z to A)")
    first_product = product_page.get_first_product_name()
    assert first_product == "Test.allTheThings() T-Shirt (Red)"

def test_add_product_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    assert products_page.get_cart_count() == 0   # cart starts empty

    products_page.add_first_product_to_cart()
    assert products_page.get_cart_count() == 1   # one item added

def test_remove_product_from_cart(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    assert products_page.get_cart_count() == 1

    products_page.remove_first_product_from_cart()
    assert products_page.get_cart_count() == 0   # back to empty after removing