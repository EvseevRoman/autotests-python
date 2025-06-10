import allure
from allure_commons._allure import step
from playwright.sync_api import Page, expect
from src.actions.callback.go_to_url import go_to_url
from src.actions.callback.info_error import error_field_telephone


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story('Негативные проверки поля "Телефон" в форме бонусной программы')
class TestNegativeValidationFieldPhone:

    @allure.title('Негативная проверка поля "Телефон". Пустое поле')
    def test_valid_phone_empty(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести корректное имя на кириллице"):
            page.locator(path_field_username).fill("Стасян")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title('Негативная проверка поля "Телефон". Номер менее 11 цифр')
    def test_valid_phone_few(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести корректное имя на кириллице"):
            page.locator(path_field_username).fill("Стасян")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("8900500080")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title('Негативная проверка поля "Телефон". Буквенные символы')
    def test_valid_phone_letter(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести корректное имя на кириллице"):
            page.locator(path_field_username).fill("Стасян")
        with step('Ввести в поле "Телефон" буквенные символы'):
            page.locator(path_field_telephone).fill("Стасян")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title(
        'Негативная проверка поля "Телефон". Номер с запрещенными спецсимволами'
    )
    def test_valid_phone_forbidden_symbol(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести корректное имя на кириллице"):
            page.locator(path_field_username).fill("Стасян")
        with step("Ввести номер телефона 8900500080$"):
            page.locator(path_field_telephone).fill("8900500080$")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title(
        'Негативная проверка поля "Телефон". Номер с несуществующим кодом страны'
    )
    def test_valid_phone_error_code(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести корректное имя на кириллице"):
            page.locator(path_field_username).fill("Стасян")
        with step("Ввести номер с несуществующим кодом страны"):
            page.locator(path_field_telephone).fill("+999123456789")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title(
        'Негативная проверка поля "Телефон". Номер с пробелами без разделения цифр'
    )
    def test_valid_name_bad_separation(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести корректное имя на кириллице"):
            page.locator(path_field_username).fill("Стасян")
        with step("Ввести номер с пробелами без разделения цифр"):
            page.locator(path_field_telephone).fill("89 0 0500 0800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title('Негативная проверка поля "Телефон". XSS-инъекция')
    def test_valid_phone_xss(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести корректное имя на кириллице"):
            page.locator(path_field_username).fill("Стасян")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("<script>alert(1)</script>")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title('Негативная проверка поля "Телефон". SQL-инъекция')
    def test_valid_phone_sql(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести корректное имя на кириллице"):
            page.locator(path_field_username).fill("Стасян")
        with step("Ввести корректный номер телефона добавив в конце апостроф"):
            page.locator(path_field_telephone).fill("89005000800'")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)
