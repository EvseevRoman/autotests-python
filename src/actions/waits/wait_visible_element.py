import logging
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@allure.step("Запуск функции ожидания того, что элемент находиться в DOM дереве страницы и виден")
def wait_visible_element(wait, path):
    logging.info('Start wait mode')
    with allure.step("Ожидание того, что искомый элемент находится в DOM дереве страницы и виден"):
        visible_element = wait.until(EC.visibility_of_element_located((By.XPATH, path)))
    logging.info('Finish wait mode')
    return visible_element
