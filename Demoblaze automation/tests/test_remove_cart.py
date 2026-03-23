from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_remove_from_cart():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.demoblaze.com")

    driver.maximize_window()

    time.sleep(50)

    # open product
    driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()

    time.sleep(50)

    # add to cart
    driver.find_element(By.LINK_TEXT, "Add to cart").click()

    time.sleep(50)

    # accept alert
    driver.switch_to.alert.accept()

    time.sleep(50)

    # open cart
    driver.find_element(By.ID, "cartur").click()

    time.sleep(50)

    # delete product
    driver.find_element(By.LINK_TEXT, "Delete").click()

    time.sleep(50)

    # verify product removed
    assert "Samsung galaxy s6" not in driver.page_source

    driver.quit()