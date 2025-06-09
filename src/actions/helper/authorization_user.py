import logging
from selenium.webdriver.support import expected_conditions as EC

import allure

from allure_commons._allure import step


@allure.title('Запуск процесса авторизации пользователя через кнопку "Войти" перехода на Главную страницу')
def authorization_user(wait, action_chains, go_to_element, username, password):
    logging.info('Starting the authorization process')
    path_my_account = "(//a[contains(text(), 'Мой аккаунт')])[1]"
    path_field_username = "//input[@id='username']"
    path_field_password = "//input[@id='password']"
    path_button_login = "//button[@name='login']"
    path_page_main = "//li[@id='menu-item-26']/a[contains(text(), 'Главная')]"

    with step('Навести курсор на ссылку "Мой аккаунт"'):
        go_to_element(wait, action_chains, path_my_account)
    with step('Сделать клик по ссылке "Мой аккаунт"'):
        action_chains.click().perform()
    with step('Дождаться загрузки страницы авторизации'):
        wait.until(EC.url_to_be('https://pizzeria.skillbox.cc/my-account/'))
    with step('Навести курсор на поле "Имя пользователя или почта"'):
        field_email = go_to_element(wait, action_chains, path_field_username)
    with step('Сделать клик по полю "Имя пользователя или почта"'):
        action_chains.click().perform()
    with step('Ввести в поле "Имя пользователя или почта" существующие данные'):
        field_email.clear()
        field_email.send_keys(username)
    with step('Навести курсор на поле "Пароль"'):
        field_password = go_to_element(wait, action_chains, path_field_password)
    with step('Сделать клик по полю "Пароль"'):
        action_chains.click().perform()
    with step('Ввести в поле "Пароль" пароль от аккаунта'):
        field_password.clear()
        field_password.send_keys(password)
    with step('Навести курсор на кнопку "Войти"'):
        go_to_element(wait, action_chains, path_button_login)
    with step('Сделать клик по кнопке "Войти"'):
        action_chains.click().perform()
    with step('Навести курсор на ссылку "Главная"'):
        go_to_element(wait, action_chains, path_page_main)
    with step('Сделать клик по ссылке "Главная"'):
        action_chains.click().perform()
    logging.info('End of the authorization process')
