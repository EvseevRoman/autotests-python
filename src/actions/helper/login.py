import allure
from allure_commons._allure import step
from playwright.sync_api import Page
import logging


@allure.step("Авторизация пользователя")
def login_user(page: Page, username, password):
    path_link_show_login = "(//a[contains(text(),'Мой аккаунт')])[1]"
    path_field_username = "//input[@id='username']"
    path_field_password = "//input[@id='password']"
    path_button_login = "//button[@name='login']"
    logging.info("Start mode user authorization")
    with step('Нажать на вкладку "Мой аккаунт"'):
        page.locator(path_link_show_login).click()
        page.wait_for_load_state(state="load")
    with step('Ввести в поле "Имя или почта": zlo'):
        page.locator(path_field_username).fill(username)
    with step("Ввести в поле пароль: qwe123!@#"):
        page.locator(path_field_password).fill(password)
    with step('Нажать на кнопку "Войти"'):
        page.locator(path_button_login).click()
    logging.info("Finish mode user authorization")
