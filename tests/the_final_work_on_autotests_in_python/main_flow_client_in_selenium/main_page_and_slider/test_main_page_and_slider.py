import time
import allure
from allure_commons._allure import step
from selenium.webdriver.common import action_chains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from src.actions.helper.go_to_element import go_to_element
from src.actions.helper.logout import logout
from src.actions.waits.wait_visible_element import wait_visible_element


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature('Тестирование функционала сайта Pizzeria')
@allure.story('Функциональное тестирование главной страницы и слайдера')
class TestMainPage:

    @allure.title('Отображение главной страницы сайта')
    def test_open_main_page(self, open_page, selenium):
        """
        Шаги:
        1. Открыть страницу https://pizzeria.skillbox.cc/
        2. Проверка того, что открылся нужный сайт
        """
        wait = WebDriverWait(selenium, timeout=5)
        website = "https://pizzeria.skillbox.cc/"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step('Проверка того, что открылся нужный сайт'):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG
            )
            assert wait.until(EC.url_contains(website))

    @allure.title("Отображение слайдера с пиццами на главной странице")
    def test_slider_visibility(self, open_page, selenium):
        """
        Шаги:
        1. Открыть страницу https://pizzeria.skillbox.cc/
        2. Проверка того, что на главной странице отображается слайдер с пиццами
        """
        wait = WebDriverWait(selenium, timeout=5)
        path_slider = "//aside[@id='accesspress_store_product-5']"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step('Проверка того, что на главной странице отображается слайдер с пиццами'):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG
            )
            assert wait_visible_element(wait, path_slider)

    @allure.title("Отображение кнопки «В корзину» при наведении на пиццу")
    def test_visibility_button_add_to_cart(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на картинку с пиццей
        2. Проверка того, что при наведении курсора на пиццу появляется кнопка "В корзину"
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_pizza = "//li[contains(@class, 'slick-active')]"
        path_button = "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на картинку с пиццей'):
            go_to_element(wait, action_chains, path_pizza)
        with step('Проверка того, что при наведении курсора на пиццу появляется кнопка "В корзину"'):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG
            )
            assert wait_visible_element(wait, path_button)

    @allure.title("Проверка работы левой кнопки прокрутки слайдера с пиццами")
    def test_left_btn_slider(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на слайдер
        2. Навести курсор на левую кнопку прокрутки слайдера
        3. Сделать клик по левой кнопке прокрутки слайдера
        4. Проверка того, что первая пицца сместилась вправо
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_slider = "//aside[@id='accesspress_store_product-5']"
        path_left_button_slider = "//a[@class='slick-prev']"
        path_title_first_pizza = "//li[contains(@class, 'slick-active')]/a"
        path_title_second_pizza = "(//li[contains(@class, 'slick-active')]/a)[2]"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на слайдер'):
            go_to_element(wait, action_chains, path_slider)
            title_first_pizza = wait_visible_element(wait, path_title_first_pizza).text
        with step('Навести курсор на левую кнопку прокрутки слайдера'):
            go_to_element(wait, action_chains, path_left_button_slider)
        with step('Сделать клик по левой кнопке слайдера'):
            action_chains.click().perform()
            title_second_pizza = wait_visible_element(wait, path_title_second_pizza).text
        with step('Проверка того, что первая пицца сместилась вправо'):
            assert title_first_pizza == title_second_pizza

    @allure.title("Проверка работы правой кнопки прокрутки слайдера с пиццами")
    def test_right_btn_slider(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на слайдер
        2. Навести курсор на правую кнопку прокрутки слайдера
        3. Сделать клик по правой кнопке прокрутки слайдера
        4. Проверка того, что последняя пицца сместилась влево
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_slider = "//aside[@id='accesspress_store_product-5']"
        path_right_button_slider = "//a[@class='slick-next']"
        path_title_end_pizza = "(//li[contains(@class, 'slick-active')]/a)[4]"
        path_title_third_pizza = "(//li[contains(@class, 'slick-active')]/a)[3]"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на слайдер'):
            go_to_element(wait, action_chains, path_slider)
            title_end_pizza = wait_visible_element(wait, path_title_end_pizza).text
        with step('Навести курсор на правую кнопку прокрутки слайдера'):
            go_to_element(wait, action_chains, path_right_button_slider)
        with step('Сделать клик по правой кнопке слайдера'):
            action_chains.click().perform()
            title_third_pizza = wait_visible_element(wait, path_title_third_pizza).text
        with step('Проверка того, что последняя пицца сместилась влево'):
            assert title_third_pizza == title_end_pizza

    @allure.title('Добавление нескольких пицц в корзину')
    def test_adding_pizza_cart(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на любую кнопку прокрутки слайдера
        5. Сделать клик по кнопке прокрутки слайдера
        6. Навести курсор на добавившуюся пиццу в слайдере
        7. Навести курсор на кнопку "В корзину"
        8. Сделать клик по кнопке "В корзину"
        9. Проверка того, что сумма корзины изменилась
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_first_pizza = "//li[contains(@class, 'slick-active')]"
        path_first_button = "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"
        path_left_button_slider = "//a[@class='slick-prev']"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)
        begin_price = wait_visible_element(wait, path_price_cart).text

        with step('Навести курсор на любую пиццу в слайдере'):
            go_to_element(wait, action_chains, path_first_pizza)
        with step('Навести курсор на кнопку "В корзину"'):
            go_to_element(wait, action_chains, path_first_button)
        with step('Сделать клик по кнопке "В корзину"'):
            action_chains.click().perform()
        with step('Навести курсор на левую кнопку прокрутки слайдера'):
            go_to_element(wait, action_chains, path_left_button_slider)
        with step('Сделать клик по левой кнопке слайдера'):
            action_chains.click().perform()
        with step('Навести курсор на добавившуюся пиццу в слайдере'):
            go_to_element(wait, action_chains, path_first_pizza)
        with step('Навести курсор на кнопку "В корзину"'):
            go_to_element(wait, action_chains, path_first_button)
        with step('Сделать клик по кнопке "В корзину"'):
            action_chains.click().perform()

        with step('Проверка того, что сумма корзины изменилась'):
            time.sleep(2)
            price = wait_visible_element(wait, path_price_cart).text
            assert begin_price != price
