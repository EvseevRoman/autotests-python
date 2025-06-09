import allure
from allure_commons._allure import step
from playwright.sync_api import Page, expect
from src.actions.callback.go_to_url import go_to_url
from src.actions.callback.info_error import error_field_telephone


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature('Тестирование функционала сайта Pizzeria')
@allure.story('Позитивные проверки поля "Телефон" в форме бонусной программы')
class TestPositiveValidationFieldPhone:

    @allure.title('Позитивная проверка поля "Телефон". Номер с +7 (11 цифр)')
    def test_valid_phone_seven(self, go_to_url, page: Page, error_field_telephone, error_field_username):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step('Ввести корректное имя на кириллице'):
            page.locator(path_field_username).fill('Стасян')
        with step('Ввести корректный номер телефона начинающийся с +7'):
            page.locator(path_field_telephone).fill('+79005000800')
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Телефон". Номер с 8 (11 цифр)')
    def test_valid_phone_eight(self, go_to_url, page: Page, error_field_telephone, error_field_username):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step('Ввести корректное имя на кириллице'):
            page.locator(path_field_username).fill('Стасян')
        with step('Ввести корректный номер телефона'):
            page.locator(path_field_telephone).fill('89005000800')
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Телефон". Номер с разделителями (+7 900 500-08-00)')
    def test_valid_phone_separator(self, go_to_url, page: Page, error_field_telephone, error_field_username):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step('Ввести корректное имя на кириллице'):
            page.locator(path_field_username).fill('Стасян')
        with step('Ввести номер телефона с разделителями (+7 900 500-08-00)'):
            page.locator(path_field_telephone).fill('+7 900 500-08-00')
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Телефон". Международный номер')
    def test_valid_phone_international(self, go_to_url, page: Page, error_field_telephone, error_field_username):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step('Ввести корректное имя на кириллице'):
            page.locator(path_field_username).fill('Стасян')
        with step('Ввести номер телефона +44 20 7946 0958'):
            page.locator(path_field_telephone).fill('+44 20 7946 0958')
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Телефон". Номер с круглыми скобками')
    def test_valid_phone_bracket(self, go_to_url, page: Page, error_field_telephone, error_field_username):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step('Ввести корректное имя на кириллице'):
            page.locator(path_field_username).fill('Стасян')
        with step('Ввести корректный номер с круглыми скобками'):
            page.locator(path_field_telephone).fill('8 (900) 500-08-00')
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)
