from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    product_name = (By.XPATH, "//td[text()='Samsung galaxy s6']")

    def is_product_in_cart(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.product_name)
        ).is_displayed()