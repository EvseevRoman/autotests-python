from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def selenium_fox(pytestconfig):
    firefox_options = Options()
    # chrome_options.add_argument("--headless")  # Включаем headless режим
    driver = Firefox(
        service=FirefoxService(GeckoDriverManager().install()), options=firefox_options
    )
    yield driver
    driver.quit()
