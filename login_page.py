from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # your code here: wait for username field, send_keys
        wait = WebDriverWait(self.driver,10)
        user = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        user.send_keys(username)
        # wait for password field, send_keys
        passw = wait.until(EC.presence_of_element_located((By.ID, "password")))
        passw.send_keys(password)
        # wait for login button, click
        btn = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
        btn.click()

    def get_error_message(self):
        error = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        return error.text