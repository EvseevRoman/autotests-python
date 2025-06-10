import time
import allure

from allure_commons._allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from src.actions.helper.go_to_element import go_to_element
from src.actions.helper.logout import logout
from src.actions.waits.wait_visible_element import wait_visible_element


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story("Регистрация и авторизация")
class TestRegistrationAuthorization:

    @allure.title("Переход к регистрации через «Мой аккаунт»")
    def test_registration_through_my_account(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на вкладку "Мой аккаунт"
        2. Сделать клик по вкладке "Мой аккаунт"
        3. Навести курсор на кнопку "Зарегистрироваться"
        4. Сделать клик по кнопке "Зарегистрироваться"
        5. Проверка того, что открылась страница Регистрации
        """
        wait = WebDriverWait(selenium, timeout=5)
        action_chains = ActionChains(selenium)
        path_page_my_account = "(//a[contains(text(), 'Мой аккаунт')])[1]"
        path_button_registration = "//button[contains(text(), 'Зарегистрироваться')]"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на вкладку "Мой аккаунт"'):
            go_to_element(wait, action_chains, path_page_my_account)
        with step('Сделать клик по вкладке "Мой аккаунт"'):
            action_chains.click().perform()
        with step('Навести курсор на кнопку "Зарегистрироваться"'):
            go_to_element(wait, action_chains, path_button_registration)
        with step('Сделать клик по кнопке "Зарегистрироваться"'):
            action_chains.click().perform()

        with step("Проверка того, что открылась страница Регистрации"):
            assert wait.until(EC.url_contains("register"))

    pass

    @allure.title("Регистрация пользователя")
    def test_user_registration(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на поле "Имя пользователя"
        2. Сделать клик по полю "Имя пользователя"
        3. Ввести в поле "Имя пользователя" валидное значение
        4. Навести курсор на поле "Адрес почты"
        5. Сделать клик по полю "Адрес почты"
        6. Ввести в поле "Адрес почты" валидный email
        7. Навести курсор на поле "Пароль"
        8. Сделать клик по полю "Пароль"
        9. Ввести в поле "Пароль" валидный пароль
        10. Навести курсор на кнопку "Зарегистрироваться"
        11. Сделать клик по кнопке "Зарегистрироваться"
        12. Проверка того, что ссылка "Войти" изменилась на "Выйти"
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_field_username = "//input[@id='reg_username']"
        path_field_email = "//input[@id='reg_email']"
        path_field_password = "//input[@id='reg_password']"
        path_button_register = "//button[@name='register']"
        value_username = "Zu9"
        value_email = "zu9@mail.ru"
        value_password = "qwe123!@#"
        path_invitation = "//div[@class='login-woocommerce']"

        open_page("https://pizzeria.skillbox.cc/register/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на поле "Имя пользователя"'):
            field_username = go_to_element(wait, action_chains, path_field_username)
        with step('Сделать клик по полю "Имя пользователя"'):
            action_chains.click().perform()
        with step('Ввести в поле "Имя пользователя" валидное значение'):
            field_username.send_keys(value_username)
        with step('Навести курсор на поле "Адрес почты"'):
            field_email = go_to_element(wait, action_chains, path_field_email)
        with step('Сделать клик по полю "Адрес почты"'):
            action_chains.click().perform()
        with step('Ввести в поле "Адрес почты" валидный email'):
            field_email.send_keys(value_email)
        with step('Навести курсор на поле "Пароль"'):
            field_password = go_to_element(wait, action_chains, path_field_password)
        with step('Сделать клик по полю "Пароль"'):
            action_chains.click().perform()
        with step('Ввести в поле "Пароль" валидный пароль'):
            field_password.send_keys(value_password)
        with step('Навести курсор на кнопку "Зарегистрироваться"'):
            go_to_element(wait, action_chains, path_button_register)
        with step('Сделать клик по кнопке "Зарегистрироваться"'):
            action_chains.click().perform()

        with step('Проверка того, что ссылка "Войти" изменилась на "Выйти"'):
            invitation = wait_visible_element(wait, path_invitation).text
            assert invitation == "Выйти", allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG,
            )
        pass

    @allure.title("Проверка успешной авторизации после регистрации")
    def test_verification_after_registration(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на поле "Имя пользователя"
        2. Сделать клик по полю "Имя пользователя"
        3. Ввести в поле "Имя пользователя" валидное значение на кириллице
        4. Навести курсор на поле "Адрес почты"
        5. Сделать клик по полю "Адрес почты"
        6. Ввести в поле "Адрес почты" валидный email
        7. Навести курсор на поле "Пароль"
        8. Сделать клик по полю "Пароль"
        9. Ввести в поле "Пароль" валидный пароль
        10. Навести курсор на кнопку "Зарегистрироваться"
        11. Сделать клик по кнопке "Зарегистрироваться"
        12. Навести курсор на вкладку "Мой аккаунт"
        13. Сделать клик по вкладке "Мой аккаунт"
        14. Навести курсор на вкладку "Данные аккаунта"
        15. Сделать клик по вкладке "Данные аккаунта"
        16. Проверка того, что введённые данные отображаются корректно
        """
        wait = WebDriverWait(selenium, timeout=30)
        action_chains = ActionChains(selenium)
        path_field_username = "//input[@id='reg_username']"
        path_field_email = "//input[@id='reg_email']"
        path_field_password = "//input[@id='reg_password']"
        path_button_register = "//button[@name='register']"
        username = "Zu10"
        email = "zu10@mail.ru"
        password = "qwe123!@#"
        path_page_my_account = "(//a[contains(text(), 'Мой аккаунт')])[1]"
        path_account_information = "//a[contains(text(), 'Данные аккаунта')]"
        path_field_name = "//input[@id='account_display_name']"
        path_adress_email = "//input[@id='account_email']"

        open_page("https://pizzeria.skillbox.cc/register/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на поле "Имя пользователя"'):
            field_username = go_to_element(wait, action_chains, path_field_username)
        with step('Сделать клик по полю "Имя пользователя"'):
            action_chains.click().perform()
        with step('Ввести в поле "Имя пользователя" валидное значение'):
            field_username.send_keys(username)
        with step('Навести курсор на поле "Адрес почты"'):
            field_email = go_to_element(wait, action_chains, path_field_email)
        with step('Сделать клик по полю "Адрес почты"'):
            action_chains.click().perform()
        with step('Ввести в поле "Адрес почты" валидный email'):
            field_email.send_keys(email)
        with step('Навести курсор на поле "Пароль"'):
            field_password = go_to_element(wait, action_chains, path_field_password)
        with step('Сделать клик по полю "Пароль"'):
            action_chains.click().perform()
        with step('Ввести в поле "Пароль" валидный пароль'):
            field_password.send_keys(password)
        with step('Навести курсор на кнопку "Зарегистрироваться"'):
            go_to_element(wait, action_chains, path_button_register)
        with step('Сделать клик по кнопке "Зарегистрироваться"'):
            action_chains.click().perform()
        with step('Навести курсор на вкладку "Мой аккаунт"'):
            go_to_element(wait, action_chains, path_page_my_account)
        with step('Сделать клик по вкладке "Мой аккаунт"'):
            action_chains.click().perform()
        with step('Навести курсор на вкладку "Данные аккаунта"'):
            go_to_element(wait, action_chains, path_account_information)
        with step('Сделать клик по вкладке "Данные аккаунта"'):
            action_chains.click().perform()

        with step("Проверка того, что введённые данные отображаются корректно"):
            value_name = wait_visible_element(wait, path_field_name).get_attribute(
                "value"
            )
            value_email = wait_visible_element(wait, path_adress_email).get_attribute(
                "value"
            )
            assert username == value_name and email == value_email, allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG,
            )
        pass

    @allure.title('Авторизация пользователя через кнопку "Войти"')
    def test_authorization_through_login_button(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на ссылку "Войти"
        2. Сделать клик по ссылке "Войти"
        3. Навести курсор на поле "Имя пользователя или почта"
        4. Сделать клик по полю "Имя пользователя или почта"
        5. Ввести в поле "Имя пользователя или почта" существующие данные
        6. Навести курсор на поле "Пароль"
        7. Сделать клик по полю "Пароль"
        8. Ввести в поле "Пароль" пароль от аккаунта
        9. Навести курсор на кнопку "Войти"
        10. Сделать клик по кнопке "Войти"
        11. Проверка того, что появилось сообщение об успешной авторизации
        """
        wait = WebDriverWait(selenium, timeout=30)
        action_chains = ActionChains(selenium)
        path_invitation = "//div[@class='login-woocommerce']"
        path_field_username = "//input[@id='username']"
        path_field_password = "//input[@id='password']"
        path_button_login = "//button[@name='login']"
        value_username = "zlo"
        value_password = "qwe123!@#"
        path_welcome = "//div[@class='welcome-user']"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на ссылку "Войти"'):
            go_to_element(wait, action_chains, path_invitation)
        with step('Сделать клик по ссылке "Войти"'):
            action_chains.click().perform()
        with step('Навести курсор на поле "Имя пользователя или почта"'):
            field_email = go_to_element(wait, action_chains, path_field_username)
        with step('Сделать клик по полю "Имя пользователя или почта"'):
            action_chains.click().perform()
        with step('Ввести в поле "Имя пользователя или почта" существующие данные'):
            field_email.send_keys(value_username)
        with step('Навести курсор на поле "Пароль"'):
            field_password = go_to_element(wait, action_chains, path_field_password)
        with step('Сделать клик по полю "Пароль"'):
            action_chains.click().perform()
        with step('Ввести в поле "Пароль" пароль от аккаунта'):
            field_password.send_keys(value_password)
        with step('Навести курсор на кнопку "Войти"'):
            go_to_element(wait, action_chains, path_button_login)
        with step('Сделать клик по кнопке "Войти"'):
            action_chains.click().perform()

        with step("Проверка того, что появилось сообщение об успешной авторизации"):
            welcome = wait_visible_element(wait, path_welcome).text
            assert welcome == f"| Привет {value_username} !", allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG,
            )
        pass
