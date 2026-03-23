from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_verify_cart():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.demoblaze.com")

    driver.maximize_window()

    time.sleep(5)

    # open product
    driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()

    time.sleep(5)

    # add to cart
    driver.find_element(By.LINK_TEXT, "Add to cart").click()

    time.sleep(5)

    driver.switch_to.alert.accept()

    # go to cart
    driver.find_element(By.ID, "cartur").click()

    time.sleep(5)

    # verify product in cart
    assert "Samsung galaxy s6" in driver.page_source

    driver.quit()