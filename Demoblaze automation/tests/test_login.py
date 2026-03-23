import pytest
from pages.login_page import LoginPage
from utils.excel_utils import get_login_data

test_data = get_login_data("testdata.xlsx", "LoginData")

@pytest.mark.parametrize("username, password, expected", test_data)
def test_login_data_driven(setup, username, password, expected):

    driver = setup
    login = LoginPage(driver)

    login.open_login_popup()
    login.login(username, password)

    if expected == "success":
        user_text = login.get_logged_in_username()
        assert "Welcome" in user_text

    elif expected == "fail":
        # Check alert popup
        alert = driver.switch_to.alert
        assert "Wrong password" in alert.text or "User does not exist" in alert.text
        alert.accept()