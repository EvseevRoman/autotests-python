import time
import allure

from allure_commons._allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from src.actions.waits.wait_visible_element import wait_visible_element
from src.actions.helper.go_to_element import go_to_element
from src.actions.helper.logout import logout


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature('Тестирование функционала сайта Pizzeria')
@allure.story('Функциональное тестирование вкладки "Меню"')
class TestPageMenu:

    @allure.title('Открытие выпадающего списка при наведении курсора на вкладку "Меню" из корзины')
    def test_open_selector_page_menu(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на вкладку "Меню"
        2. Проверка того, что появляется выпадающий список
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_page_menu = "//a[contains(text(), 'Меню')]"
        path_submenu = "//ul[@class='sub-menu']"

        open_page("https://pizzeria.skillbox.cc/cart/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на вкладку "Меню"'):
            go_to_element(wait, action_chains, path_page_menu)
        with step('Проверка того, что появляется выпадающий список'):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG
            )
            assert wait_visible_element(wait, path_submenu)

    @allure.title('Переход в раздел «Десерты» из выпадающего списка вкладки "Меню"')
    def test_go_to_desserts(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на вкладку "Меню" в хэдере
        2. Навести курсор на раздел "Десерты"
        3. Сделать клик по разделу "Десерты"
        4. Проверка того, что открылась страница с десертом
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_page_menu = "//a[contains(text(), 'Меню')]"
        path_section_desserts = "//a[contains(text(), 'Десерты')]"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на вкладку "Меню" в хэдере'):
            go_to_element(wait, action_chains, path_page_menu)
        with step('Навести курсор на раздел "Десерты"'):
            go_to_element(wait, action_chains, path_section_desserts)
        with step('Сделать клик по разделу "Десерты"'):
            action_chains.click().perform()
        with step('Проверка того, что открылась страница с десертом'):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG
            )
            assert wait.until(EC.url_contains('deserts'))

    @allure.title('Фильтрация товаров по цене <= 135 рублей на страницы "Десерты"')
    def test_product_filtering(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на правый ползунок фильтра по цене
        2. Установить правый ползунок фильтра по цене товара, в диапазон до 135 рублей, включительно
        3. Навести курсор на кнопку "Применить"
        4. Сделать клик по кнопке "Применить"
        5. Проверка того, что отображается товар удовлетворяющий условиям установленного фильтра
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_right_button_slider = "(//span[contains(@class, 'ui-slider-handle ui')])[2]"
        path_button_apply = "//button[contains(text(), 'Применить')]"
        path_price_desserts = "//span[@class='price']/span[@class='woocommerce-Price-amount amount']//bdi"
        path_price_filter = "//span[@class='to']"
        distance = -1

        open_page("https://pizzeria.skillbox.cc/product-category/menu/deserts/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на правый ползунок фильтра по цене'):
            go_to_element(wait, action_chains, path_right_button_slider)
        with step('Установить правый ползунок фильтра по цене товара, в диапазон до 135 рублей, включительно'):
            price_filter = int(wait_visible_element(wait, path_price_filter).text[:3])
            while price_filter >= 135:
                action_chains.click_and_hold().move_by_offset(xoffset=distance, yoffset=0).release().perform()
                price_filter = int(wait_visible_element(wait, path_price_filter).text[:3])
                distance -= 1
        with step('Навести курсор на кнопку "Применить"'):
            go_to_element(wait, action_chains, path_button_apply)
        with step('Сделать клик по кнопке "Применить"'):
            action_chains.click().perform()
        with step('Проверка того, что отображается товар удовлетворяющий условиям установленного фильтра'):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG
            )
            prices_desserts = wait.until(EC.visibility_of_all_elements_located((By.XPATH, path_price_desserts)))
            for price in prices_desserts:
                price = int(price.text[:3])
                assert price <= 135

    @allure.title('Добавление десерта в корзину')
    def test_adding_dessert_to_the_cart(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на кнопку "В корзину" любого десерта
        2. Сделать клик по кнопке "В корзину"
        3. Проверка того, что сумма корзины изменилась
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_button_in_cart = "//a[contains(text(), 'В корзину')]"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"

        open_page("https://pizzeria.skillbox.cc/product-category/menu/deserts/")
        logout(wait, action_chains, go_to_element)
        price_cart_begin = wait_visible_element(wait, path_price_cart).text

        with step('Навести курсор на кнопку "В корзину" любого десерта'):
            go_to_element(wait, action_chains, path_button_in_cart)
        with step('Сделать клик по кнопке "В корзину"'):
            action_chains.click().perform()
        with step('Проверка того, что сумма корзины изменилась'):
            time.sleep(1)
            price_cart_finish = wait_visible_element(wait, path_price_cart).text
            assert price_cart_begin != price_cart_finish
