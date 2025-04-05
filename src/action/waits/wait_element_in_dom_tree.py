import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@allure.step("Запуск функции ожидания элемента в DOM дереве страницы")
def wait_element_in_dom_tree(wait, path):
    logging.info('Start wait mode')
    with allure.step("Ожидание того, что искомый элемент находится в DOM дереве страницы"):
        wait_element_in_dom_tree = wait.until(EC.presence_of_element_located((By.XPATH, path)))
    logging.info('Finish wait mode')
    return wait_element_in_dom_tree
