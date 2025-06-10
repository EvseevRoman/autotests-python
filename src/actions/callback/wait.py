import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def wait_element(selenium):
    @allure.step("Ожидание элемента по {by} со значением {value}")
    def callback(by, value):
        return WebDriverWait(selenium, timeout=60).until(
            lambda driver: driver.find_element(by, value)
        )

    return callback


@pytest.fixture
def wait_elements(selenium):
    @allure.step("Ожидание списка элементов по {by} со значением {value}")
    def callback(by, value):
        return WebDriverWait(selenium, timeout=60).until(
            lambda driver: driver.find_elements(by, value)
        )

    return callback
