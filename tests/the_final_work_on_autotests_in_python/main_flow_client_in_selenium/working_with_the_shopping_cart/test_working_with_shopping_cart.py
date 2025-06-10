import time
import allure

from allure_commons._allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from src.actions.helper.go_to_element import go_to_element
from src.actions.helper.logout import logout
from src.actions.waits.wait_visible_element import wait_visible_element


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story("Функциональное тестирование корзины")
class TestWorkShoppingCart:

    @allure.title("Проверка содержимого корзины после добавления товаров")
    def test_contents_shopping_cart_after_adding_items(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую понравившуюся картинку с пиццей
        2. Сделать клик по картинке с пиццей
        3. Навести курсор на селектор с выбором борта для пиццы
        4. Сделать клик по селектору с выбором борта пиццы
        5. Навести курсор на любой борт для пиццы
        6. Сделать клик по виду борта пиццы
        7. Навести курсор на кнопку "В корзину"
        8. Сделать клик по кнопке "В корзину"
        9. Навести курсор на вкладку "Главная"
        10. Сделать клик по вкладке "Главная страница"
        11. Навести курсор на любую понравившуюся картинку с пиццей
        12. Сделать клик по картинке с пиццей
        13. Навести курсор на селектор с выбором борта для пиццы
        14. Сделать клик по селектору с выбором борта пиццы
        15. Навести курсор на любой борт для пиццы
        16. Сделать клик по виду борта пиццы
        17. Навести курсор на кнопку "В корзину"
        18. Сделать клик по кнопке "В корзину"
        19. Навести курсор на иконку корзины
        20. Сделать клик по иконке корзины
        21. Проверка того, что в корзине все добавленные пиццы, в нужном количестве и опциями.
        """
        wait = WebDriverWait(selenium, timeout=5)
        action_chains = ActionChains(selenium)
        path_first_pizza = "//li[contains(@class, 'slick-active')]"
        path_title_first_pizza_in_slider = "//li[contains(@class, 'slick-active')]//h3"
        path_second_pizza = "(//li[contains(@class, 'slick-active')])[2]"
        path_title_second_pizza_in_slider = (
            "(//li[contains(@class, 'slick-active')]//h3)[2]"
        )
        path_selector = "//select"
        path_button = "//button[contains(text(), 'В корзину')]"
        path_page_main = "//a[contains(text(), 'Главная')]"
        path_shopping_cart = "//a[@title='View your shopping cart']"
        path_title_first_pizza_in_cart = "//tr/td[3]/a"
        path_count_first_pizza_in_cart = "//input[@type='number']"
        path_option_first_pizza_in_cart = "//tr/td[3]/dl/dd"
        path_title_second_pizza_in_cart = "(//tr/td[3]/a)[2]"
        path_count_second_pizza_in_cart = "(//input[@type='number'])[2]"
        path_option_second_pizza_in_cart = "(//tr/td[3]/dl/dd)[2]"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step("Навести курсор любую понравившуюся картинку с пиццей"):
            title_first_pizza_in_slider = wait_visible_element(
                wait, path_title_first_pizza_in_slider
            ).text.lower()
            go_to_element(wait, action_chains, path_first_pizza)
        with step("Сделать клик по картинке с пиццей"):
            action_chains.click().perform()
        with step("Навести курсор на селектор с выбором борта для пиццы"):
            selector = go_to_element(wait, action_chains, path_selector)
        with step("Сделать клик по селектору с выбором борта для пиццы"):
            action_chains.click().perform()
            select = Select(selector)
        with step('Сделать клик по борту для пиццы "Сырный"'):
            select.select_by_visible_text("Сырный - 55.00 р.")
            selenium.execute_script("document.activeElement.blur()")
            count_first_pizza_in_card = wait_visible_element(
                wait, path_count_first_pizza_in_cart
            ).get_attribute("value")
        with step('Навести курсор на кнопку "В корзину"'):
            go_to_element(wait, action_chains, path_button)
        with step('Сделать клик по кнопке "В корзину"'):
            action_chains.click().perform()
        with step('Навести курсор на вкладку "Главная"'):
            go_to_element(wait, action_chains, path_page_main)
        with step('Сделать клик по вкладке "Главная страница"'):
            action_chains.click().perform()
        with step("Навести курсор любую понравившуюся картинку с пиццей"):
            title_second_pizza_in_slider = wait_visible_element(
                wait, path_title_second_pizza_in_slider
            ).text.lower()
            go_to_element(wait, action_chains, path_second_pizza)
        with step("Сделать клик по картинке с пиццей"):
            action_chains.click().perform()
        with step("Навести курсор на селектор с выбором борта для пиццы"):
            selector = go_to_element(wait, action_chains, path_selector)
        with step("Сделать клик по селектору с выбором борта для пиццы"):
            action_chains.click().perform()
            select = Select(selector)
        with step('Сделать клик по борту для пиццы "Колбасный"'):
            select.select_by_visible_text("Колбасный - 65.00 р.")
            selenium.execute_script("document.activeElement.blur()")
            count_second_pizza_in_card = wait_visible_element(
                wait, path_count_first_pizza_in_cart
            ).get_attribute("value")
        with step('Навести курсор на кнопку "В корзину"'):
            go_to_element(wait, action_chains, path_button)
        with step('Сделать клик по кнопке "В корзину"'):
            action_chains.click().perform()
        with step("Навести курсор на иконку корзины"):
            go_to_element(wait, action_chains, path_shopping_cart)
        with step("Сделать клик по иконке корзины"):
            action_chains.click().perform()
        with step(
            "Проверка того, что в корзине все добавленные пиццы, в нужном количестве и опциями."
        ):
            title_first_pizza_in_cart = wait_visible_element(
                wait, path_title_first_pizza_in_cart
            ).text.lower()
            title_second_pizza_in_cart = wait_visible_element(
                wait, path_title_second_pizza_in_cart
            ).text.lower()
            count_first_pizza_in_cart = wait_visible_element(
                wait, path_count_first_pizza_in_cart
            ).get_attribute("value")
            count_second_pizza_in_cart = wait_visible_element(
                wait, path_count_second_pizza_in_cart
            ).get_attribute("value")
            option_first_pizza_in_cart = wait_visible_element(
                wait, path_option_first_pizza_in_cart
            ).text
            option_second_pizza_in_cart = wait_visible_element(
                wait, path_option_second_pizza_in_cart
            ).text
            assert (
                title_first_pizza_in_slider.replace("«", '"').replace("»", '"')
                == title_first_pizza_in_cart
                and count_first_pizza_in_card == count_first_pizza_in_cart
                and "Сырный" in option_first_pizza_in_cart
                and title_second_pizza_in_slider.replace("«", '"').replace("»", '"')
                == title_second_pizza_in_cart
                and count_second_pizza_in_card == count_second_pizza_in_cart
                and "Колбасный" in option_second_pizza_in_cart
            )
        pass

    @allure.title("Изменение количества пицц в корзине")
    def test_changing_number_pizzas_in_basket(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Навести курсор на поле количество товара
        7. Сделать клик по полю количество
        8. Удалить существующее значение
        9. Ввести нужное количество >1
        10. Навести курсор на кнопку "Обновить корзину"
        11. Нажать кнопку "Обновить корзину"
        12. Проверка того, что сумма общей стоимости изменилась
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_pizza = "//li[contains(@class, 'slick-active')]"
        path_button_basket = (
            "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"
        )
        path_field_count = "//input[@title='Кол-во']"
        count = 5
        path_button_update_cart = "//button[@name='update_cart']"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"
        path_subtotal = "//td[@class='product-subtotal']"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step("Навести курсор на любую пиццу в слайдере"):
            go_to_element(wait, action_chains, path_pizza)
        with step('Навести курсор на кнопку "В корзину"'):
            go_to_element(wait, action_chains, path_button_basket)
        with step('Сделать клик по кнопке "В корзину"'):
            action_chains.click().perform()
        with step("Навести курсор на иконку корзины"):
            go_to_element(wait, action_chains, path_price_cart)
        with step("Сделать клик по иконке корзины"):
            action_chains.click().perform()
            subtotal_begin = wait_visible_element(wait, path_subtotal).text
        with step("Навести курсор на поле количество товара"):
            field_count = go_to_element(wait, action_chains, path_field_count)
        with step("Сделать клик по полю количество"):
            action_chains.click().perform()
        with step("Удалить существующее значение"):
            field_count.clear()
        with step("Ввести нужное количество >1"):
            field_count.send_keys(count)
        with step('Навести курсор на кнопку "Обновить корзину"'):
            button_update_cart = wait.until(
                EC.element_to_be_clickable((By.XPATH, path_button_update_cart))
            )
            action_chains.move_to_element(button_update_cart).perform()
        with step('Нажать кнопку "Обновить корзину"'):
            action_chains.click(button_update_cart).perform()
            time.sleep(1)
            subtotal_finish = wait_visible_element(wait, path_subtotal).text

        with step("Проверка того, что сумма общей стоимости изменилась"):
            assert subtotal_begin != subtotal_finish

    @allure.title("Удаление позиции из корзины")
    def test_deleting_item_from_cart(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Навести курсор на иконку "Удаление"
        7. Сделать клик по иконке "Удаление"
        8. Проверка того, что сумма корзины изменилась"
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_pizza = "//li[contains(@class, 'slick-active')]"
        path_button_basket = (
            "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"
        )
        path_button_delete = "//a[@class='remove']"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step("Навести курсор на любую пиццу в слайдере"):
            go_to_element(wait, action_chains, path_pizza)
        with step('Навести курсор на кнопку "В корзину"'):
            go_to_element(wait, action_chains, path_button_basket)
        with step('Сделать клик по кнопке "В корзину"'):
            action_chains.click().perform()
        with step("Навести курсор на иконку корзины"):
            go_to_element(wait, action_chains, path_price_cart)
        with step("Сделать клик по иконке корзины"):
            action_chains.click().perform()
            begin_price = wait_visible_element(wait, path_price_cart).text
        with step('Навести курсор на иконку "Удаление"'):
            go_to_element(wait, action_chains, path_button_delete)
        with step('Сделать клик по иконке "Удаление"'):
            action_chains.click().perform()
            time.sleep(2)
            end_price = wait_visible_element(wait, path_price_cart).text

        with step("Проверка того, что сумма корзины изменилась"):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG,
            )
            assert begin_price != end_price
