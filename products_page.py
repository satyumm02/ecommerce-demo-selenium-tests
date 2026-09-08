from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def sort_by(self, option_text):
        dropdown = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
        select = Select(dropdown)
        select.select_by_visible_text(option_text)

    def get_first_product_name(self):
        product = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
        return product.text

    def add_first_product_to_cart(self):
        button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_item button")))
        button.click()

    def get_cart_count(self):
        try:
            badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            return int(badge.text)
        except:
            return 0

    def remove_first_product_from_cart(self):
        button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_item button")))
        button.click()   # Sauce Demo's button toggles between "Add to cart" and "Remove"