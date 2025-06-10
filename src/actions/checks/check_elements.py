import allure
from playwright.sync_api import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging


@allure.step('Выполнение проверки на наличие ключевого слова "bug" в заголовках')
def check_elements_search(wait, path, cnt_elements, search_text):
    logging.info("Start checking the required items")
    for element_search in range(1, cnt_elements + 1):
        title = wait.until(EC.presence_of_element_located((By.XPATH, path)))
        with allure.step(
            f"Проверка {element_search}-й задачи, на наличие в заголовке слова 'Bug' или 'bug'"
        ):
            assert search_text in title.text.lower()
    logging.info("Finish checking the required items")


@allure.step("Выполнение проверки на соответствие текста")
def check_results_search(page: Page, path, search_text):
    logging.info("Start checking the required items")
    page.wait_for_load_state(state="domcontentloaded")
    page.wait_for_timeout(1000)
    page.wait_for_selector(path)
    all_links = page.locator(path).all()
    for link in range(len(all_links)):
        with allure.step(
            f"Проверка {link+1}-го элемента, на наличие ключевого слова {search_text}"
        ):
            assert search_text.lower() in all_links[link].inner_text().lower()
    logging.info("Finish checking the required items")


@allure.step("Выполнение проверки на количество звёзд")
def check_count_stars(page: Page, path_count_stars, count_stars):
    logging.info("The beginning of checking the number of stars")
    page.wait_for_load_state(state="domcontentloaded")
    page.wait_for_timeout(1000)
    page.wait_for_selector(path_count_stars)
    all_stars = page.locator(path_count_stars).all()
    for star in range(len(all_stars)):
        with allure.step(
            f"Проверка {star+1}-го элемента, на количество звёзд {count_stars}"
        ):
            assert int(all_stars[star].inner_text()[:-1]) > 20
    logging.info("End of checking the number of stars")


@allure.step("Выполнение проверки на количество месяцев")
def check_count_months(page: Page, path_count_month):
    logging.info("The beginning of checking the number of months")
    page.wait_for_load_state(state="domcontentloaded")
    page.wait_for_timeout(1000)
    page.wait_for_selector(path_count_month)
    all_month = page.locator(path_count_month).all()
    for month in range(len(all_month)):
        with allure.step(f"Проверка {month+1}-го элемента, на количество месяцев"):
            assert 6 <= int(all_month[month].inner_text()) <= 12
    logging.info("End of checking the number of stars")
