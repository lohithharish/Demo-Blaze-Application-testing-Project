from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    product_link = (By.LINK_TEXT, "Samsung galaxy s6")
    add_to_cart_btn = (By.XPATH, "//a[text()='Add to cart']")
    cart_btn = (By.ID, "cartur")

    # Actions
    def select_product(self):
        self.wait.until(EC.element_to_be_clickable(self.product_link)).click()

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart_btn)).click()

    def handle_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_btn)).click()