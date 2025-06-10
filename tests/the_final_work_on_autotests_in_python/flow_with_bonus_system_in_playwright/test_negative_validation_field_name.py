import allure
from allure_commons._allure import step
from playwright.sync_api import Page, expect
from src.actions.callback.go_to_url import go_to_url


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story('Негативные проверки поля "Имя" в форме бонусной программы')
class TestNegativeValidationFieldName:

    @allure.title('Негативная проверка поля "Имя" пустым полем')
    def test_valid_name_empty(self, go_to_url, page: Page):
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title('Негативная проверка поля "Имя". Слишком короткое имя')
    def test_valid_name_very_short(self, go_to_url, page: Page):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести имя из одной буквы"):
            page.locator(path_field_username).fill("Я")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title('Негативная проверка поля "Имя" слишком длинным именем')
    def test_valid_name_very_long(self, go_to_url, page: Page):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести 200 символов на кириллице"):
            page.locator(path_field_username).fill("M" * 200)
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title('Негативная проверка поля "Имя". Имя из цифр')
    def test_valid_name_number(self, go_to_url, page: Page):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести имя состоящее из одних цифр"):
            page.locator(path_field_username).fill("1234567890")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title('Негативная проверка поля "Имя". Имя со спецсимволами (@#$')
    def test_valid_name_special_symbol(self, go_to_url, page: Page):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести имя со спецсимволом $"):
            page.locator(path_field_username).fill("Buks$")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title('Негативная проверка поля "Имя". Только пробелы')
    def test_valid_name_only_space(self, go_to_url, page: Page):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести имя из 5 пробелов"):
            page.locator(path_field_username).fill("     ")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title('Негативная проверка поля "Имя". Проверка на XSS-уязвимость')
    def test_valid_name_xxs(self, go_to_url, page: Page):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_error = "//div[@id='bonus_content']"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step('Ввести в поле "Имя" <script>alert(1)</script>'):
            page.locator(path_field_username).fill("<script>alert(1)</script>")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_error)).to_be_visible(timeout=1000)

    @allure.title('Негативная проверка поля "Имя". SQL-инъекция')
    def test_valid_name_sql(self, go_to_url, page: Page):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step('Ввести в поле "Имя" имя с апострофом в конце'):
            page.locator(path_field_username).fill("ИмЯ'")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step("Проверка того, что появилось сообщение об ошибке"):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)
