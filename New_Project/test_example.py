from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def set_up_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Включаем headless режим
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

class TestExample:
   def test_example(self, set_up_browser):
       driver = set_up_browser
       driver.get("http://skillbox.ru")
       assert "Skillbox – образовательная платформа с онлайн-курсами." == driver.title
