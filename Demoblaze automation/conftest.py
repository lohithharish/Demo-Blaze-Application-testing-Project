import pytest
import pytest_html
from utils.driver_setup import get_driver



@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        # Get driver safely
        driver = item.funcargs.get("setup", None)

        if driver:
            # Create screenshot file name using test name
            file_name = f"reports/{item.name}.png"

            # Take screenshot
            driver.save_screenshot(file_name)

            # Attach screenshot to HTML report
            if hasattr(report, "extra"):
                report.extra.append(pytest_html.extras.image(file_name))