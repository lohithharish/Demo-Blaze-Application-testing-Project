def test_open_website(setup):
    driver = setup
    assert "STORE" in driver.page_source