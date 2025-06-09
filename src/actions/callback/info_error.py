import pytest
from playwright.sync_api import Page


@pytest.fixture
def error_field_telephone(page: Page):
    return page.get_by_text('Поле "Телефон" обязательно для заполнения')


@pytest.fixture
def error_field_username(page: Page):
    return page.get_by_text('Поле "Имя" обязательно для заполнения')
