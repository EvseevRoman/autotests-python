from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def set_up_browser():
    chrome_options = Options()
    chrome_options.page_load_strategy = 'none'   # Режим ожидания
   # chrome_options.add_argument("--headless")   # Включаем headless режим
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    #driver.implicitly_wait(60)   # Время ожидания при поиске элемента
    yield driver
    driver.quit()