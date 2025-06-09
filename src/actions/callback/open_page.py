import allure
import pytest


@pytest.fixture
def open_page(selenium):
    @allure.step('Открываем страницу {url}')
    def callback(url):
        selenium.get(url)
    return callback
