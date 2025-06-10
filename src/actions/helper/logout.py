import logging
import allure

from allure_commons._allure import step
from src.actions.waits.wait_visible_element import wait_visible_element


@allure.step("Запуск функции проверки и выхода из аккаунта")
def logout(wait, action_chains, go_to_element):
    path_button_authoriz = "//div[@class='login-woocommerce']"
    logging.info("Start wait mode checking and logout")
    with step("Проверка авторизации пользователя"):
        button_authoriz = wait_visible_element(wait, path_button_authoriz).text
        if button_authoriz == "Выйти":
            with step("Выход из аккаунта"):
                go_to_element(wait, action_chains, path_button_authoriz)
                action_chains.click().perform()
    logging.info("Finish wait mode checking and logout")
