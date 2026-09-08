# Sauce Demo Test Automation Suite

An automated test suite for [Sauce Demo](https://www.saucedemo.com/), built with Python, Selenium, and pytest, using the Page Object Model design pattern.

## Tech Stack
- Python
- Selenium WebDriver
- pytest
- pytest-html (for test reporting)

## What's Covered
- **Login** — valid login, invalid password, locked-out user (parametrized tests)
- **Products** — sorting products, adding/removing items from cart
- **Checkout** — full end-to-end purchase flow, from login through order confirmation

## Project Structure
project/
├── login_page.py # Page Object for the login page
├── products_page.py # Page Object for the products/inventory page
├── checkout_page.py # Page Object for the checkout flow
├── test_login.py # Login test scenarios
├── test_product.py # Product page tests
├── test_checkout.py # End-to-end checkout flow test


## How to Run
1. Install dependencies: pip install selenium pytest pytest-html
2. Run all tests with an HTML report: python -m pytest --html=report.html --self-contained-html -v


## Test Results
7 tests, all passing — covering login validation, product interactions, and a full checkout flow.

## Key Techniques Used
- Page Object Model (POM) for maintainable, reusable page logic
- Explicit waits (`WebDriverWait`) instead of hardcoded sleeps
- Parametrized testing (`@pytest.mark.parametrize`) for multiple login scenarios in one test function
- pytest fixtures for clean browser setup/teardown