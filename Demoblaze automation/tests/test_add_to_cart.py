from pages.home_page import HomePage
from pages.cart_page import CartPage

def test_add_product_to_cart(setup):

    driver = setup

    home = HomePage(driver)
    cart = CartPage(driver)

    # Step 1: Select product
    home.select_product()

    # Step 2: Add to cart
    home.add_to_cart()

    # Step 3: Handle alert
    home.handle_alert()

    # Step 4: Go to cart
    home.go_to_cart()

    # Step 5: Validate product in cart
    assert cart.is_product_in_cart()