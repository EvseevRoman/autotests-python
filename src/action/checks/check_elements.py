import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging


@allure.step('Выполнение проверки того, что каждая из задач содержит в названии слово "bug" или "Bug" на странице')
def check_elements_search(wait, path, cnt_elements, search_text):
    logging.info('Start checking the required items')
    for element_search in range(1, cnt_elements + 1):
        title = wait.until(EC.presence_of_element_located((By.XPATH, path)))
        with allure.step(f"Проверка {element_search}-й задачи, на наличие в заголовке слова 'Bug' или 'bug'"):
            assert search_text in title.text.lower()
    logging.info('Finish checking the required items')
