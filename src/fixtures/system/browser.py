import logging

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest


@pytest.fixture()
def selenium(pytestconfig):
    browser_name = pytestconfig.getini("browser_name")  # Получаем переменную browser_name
    logging.info(f'Prepare {browser_name} browser ...')
    if pytestconfig.getini("browser_name") == 'chrome':
        options = ChromeOptions()
        options.page_load_strategy = pytestconfig.getini("wait")  # Режим ожидания
        if pytestconfig.getini("headless") == 'True' and browser_name == 'chrome':  # Условия отображения интерфейса
            options.add_argument("--headless")  # Включаем headless режим
        driver = Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif pytestconfig.getini("browser_name") == 'firefox':
        options = FirefoxOptions()
        options.page_load_strategy = pytestconfig.getini("wait")  # Режим ожидания
        driver = Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    logging.info(f'Browser {browser_name} has been started.')
    yield driver
    driver.quit()
