from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    place_order_btn = (By.XPATH, "//button[text()='Place Order']")
    name = (By.ID, "name")
    country = (By.ID, "country")
    city = (By.ID, "city")
    card = (By.ID, "card")
    month = (By.ID, "month")
    year = (By.ID, "year")
    purchase_btn = (By.XPATH, "//button[text()='Purchase']")
    success_msg = (By.XPATH, "//h2[text()='Thank you for your purchase!']")

    # Actions
    def click_place_order(self):
        self.wait.until(EC.element_to_be_clickable(self.place_order_btn)).click()

    def fill_details(self):
        self.wait.until(EC.visibility_of_element_located(self.name)).send_keys("Lohith")
        self.driver.find_element(*self.country).send_keys("India")
        self.driver.find_element(*self.city).send_keys("Bangalore")
        self.driver.find_element(*self.card).send_keys("123456789")
        self.driver.find_element(*self.month).send_keys("03")
        self.driver.find_element(*self.year).send_keys("2026")

    def click_purchase(self):
        self.wait.until(EC.element_to_be_clickable(self.purchase_btn)).click()

    def is_order_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_msg)
        ).is_displayed()