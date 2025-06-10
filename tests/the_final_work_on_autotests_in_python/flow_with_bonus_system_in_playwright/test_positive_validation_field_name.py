import allure
from allure_commons._allure import step
from playwright.sync_api import Page, expect
from src.actions.callback.go_to_url import go_to_url
from src.actions.callback.info_error import error_field_telephone


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story('Позитивные проверки поля "Имя" в форме бонусной программы')
class TestPositiveValidationFieldName:

    @allure.title('Позитивная проверка поля "Имя" написанное кириллицей')
    def test_valid_name_rus(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести корректное имя на кириллице"):
            page.locator(path_field_username).fill("Стасян")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Имя" написанное латиницей')
    def test_valid_name_lat(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести корректное имя на латинице"):
            page.locator(path_field_username).fill("Donald")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Имя" длинным именем')
    def test_valid_name_long(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести 50 символов на кириллице"):
            page.locator(path_field_username).fill("M" * 50)
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Имя" коротким именем')
    def test_valid_name_short(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести ия из 2 символов"):
            page.locator(path_field_username).fill("Ян")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Имя". Имя с дефисом')
    def test_valid_name_dash(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести имя с дефисом"):
            page.locator(path_field_username).fill("Ян-бабаян")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Имя". Двойное имя')
    def test_valid_name_dabble(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести имя с пробелом"):
            page.locator(path_field_username).fill("Ян Бабаян")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Имя". Иия с апострофом')
    def test_valid_name_apostrophe(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести имя с апострофом"):
            page.locator(path_field_username).fill("Д'артаньян")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Имя". Иия с разными регистрами букв')
    def test_valid_name_register(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести имя с разными регистрами букв"):
            page.locator(path_field_username).fill("ИмЯ")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Имя". Иия с точкой')
    def test_valid_name_point(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести имя с точкой"):
            page.locator(path_field_username).fill("А.С. Пушкин")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)

    @allure.title('Позитивная проверка поля "Имя". Имя с Unicode-символами')
    def test_valid_name_unicode(
        self, go_to_url, page: Page, error_field_telephone, error_field_username
    ):
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button = "//button[contains(text(), 'Оформить карту')]"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"

        go_to_url("https://pizzeria.skillbox.cc/bonus/")

        with step("Ввести имя с Unicode-символами"):
            page.locator(path_field_username).fill("坂本")
        with step("Ввести корректный номер телефона"):
            page.locator(path_field_telephone).fill("89005000800")
        with step('Сделать клик по кнопке "Оформить карту"'):
            page.locator(path_button).click()

        with step('Проверка того, что появилось сообщение "Ваша карта оформлена!"'):
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)
