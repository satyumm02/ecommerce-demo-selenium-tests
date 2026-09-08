import pytest
from selenium import webdriver
from login_page import LoginPage
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

@pytest.mark.parametrize("username, password, expected_outcome", [
    ("standard_user", "secret_sauce", "success"),
    ("standard_user", "wrong_password", "error"),
    ("locked_out_user", "secret_sauce", "locked"),
])
def test_login_scenarios(driver, username, password, expected_outcome):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login(username, password)

    if expected_outcome == "success":
        assert "inventory" in driver.current_url
    else:
        error_text = login_page.get_error_message()
        assert "Epic sadface" in error_text   # Sauce Demo's error messages all start with this

