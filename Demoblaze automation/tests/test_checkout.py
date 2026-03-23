from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_place_order(setup):

    driver = setup

    home = HomePage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Add product first
    home.select_product()
    home.add_to_cart()
    home.handle_alert()
    home.go_to_cart()

    # Checkout
    checkout.click_place_order()
    checkout.fill_details()
    checkout.click_purchase()

    # Validate success
    assert checkout.is_order_successful()