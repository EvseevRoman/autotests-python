import allure
from allure_commons._allure import step
from playwright.sync_api import Page
import logging


@allure.step("Заполнение корзины товаром")
def filling_shopping_cart_goods(page: Page):
    path_main_page = "(//a[contains(text(), 'Главная')])[1]"
    path_first_pizza = "(//li[contains(@class, 'slick-active')])[1]"
    path_first_button = (
        "(//li[contains(@class, 'slick-active')])[1]//a[contains(text(), 'В корзину')]"
    )
    path_second_pizza = "(//li[contains(@class, 'slick-active')])[4]"
    path_second_button = (
        "(//li[contains(@class, 'slick-active')])[4]//a[contains(text(), 'В корзину')]"
    )
    logging.info("Start mode filling the shopping cart with goods")
    with step("Перейти на главную страницу"):
        page.locator(path_main_page).click()
    with step("Навести курсор на любую пиццу в слайдере"):
        page.locator(path_first_pizza).hover()
    with step('Сделать клик по кнопке "В корзину"'):
        page.locator(path_first_button).click()
        page.wait_for_timeout(1000)
    with step("Навести курсор на другую пиццу в слайдере"):
        page.locator(path_second_pizza).hover()
    with step('Сделать клик по кнопке "В корзину"'):
        page.locator(path_second_button).click()
        page.wait_for_timeout(1000)
    logging.info("Finish mode filling the shopping cart with goods")
