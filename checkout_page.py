from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_cart(self):
        cart = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link")))
        cart.click()

    def checkout(self):
        checkout_btn = self.wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        checkout_btn.click()

    def fill_checkout_info(self, f_name, l_name, pin):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(f_name)
        self.driver.find_element(By.ID, "last-name").send_keys(l_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(pin)
        self.driver.find_element(By.ID, "continue").click()

    def finish(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "finish"))).click()

    def finish_message(self):
        message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
        return message.text