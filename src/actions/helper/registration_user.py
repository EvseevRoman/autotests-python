import allure
from allure_commons._allure import step
from playwright.sync_api import Page, expect
import logging


@allure.step("Регистрация нового пользователя")
def registration_user(page: Page, username, email, password):
    path_page_my_account = "(//a[contains(text(), 'Мой аккаунт')])[1]"
    path_button_registration = "//button[contains(text(),'Зарегистрироваться')]"
    path_field_username = "//input[@id='reg_username']"
    path_field_email = "//input[@id='reg_email']"
    path_field_password = "//input[@id='reg_password']"
    path_info_message = "//div[contains(text(), 'Регистрация завершена')]"
    logging.info("Start mode registration user")
    with step('Перейти на страницу "Мой аккаунт"'):
        page.locator(path_page_my_account).click()
    with step('Нажать на кнопку "Зарегистрироваться"'):
        page.locator(path_button_registration).click()
    with step('Ввести в поле "Имя пользователя" валидное значение'):
        page.locator(path_field_username).type(username)
    with step('Ввести в поле "Адрес почты" валидный email'):
        page.locator(path_field_email).type(email)
    with step('Ввести в поле "Пароль" валидный пароль'):
        page.locator(path_field_password).type(password)
    with step('Сделать клик по кнопке "Зарегистрироваться"'):
        page.locator(path_button_registration).click()
        expect(page.locator(path_info_message)).to_be_visible(timeout=5000)
    logging.info("Finish mode registration user")
