import logging
import allure

from allure_commons._allure import step
from src.actions.waits.wait_visible_element import wait_visible_element


@allure.step("Запуск функции ожидание видимости элемента и наведение на него курсора")
def go_to_element(wait, action_chains, path_element):
    logging.info("Start wait mode and hovering cursor")
    with step("Ожидание видимости элемента"):
        element = wait_visible_element(wait, path_element)
    with step("Навести курсор на элемент"):
        action_chains.move_to_element(element).perform()
    return element
    logging.info("Finish wait mode and hovering cursor")
