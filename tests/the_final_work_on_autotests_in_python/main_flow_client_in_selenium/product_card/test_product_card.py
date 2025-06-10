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
@allure.story("Функциональное тестирование карточки товара")
class TestProductCard:

    @allure.title("Переход на страницу описания пиццы при клике на изображение")
    def test_open_product_card(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор любую понравившуюся картинку с пиццей
        2. Сделать клик по картинке с пиццей
        3. Проверка того, что открылась карточка товара
        """
        wait = WebDriverWait(selenium, timeout=5)
        action_chains = ActionChains(selenium)
        path_pizza = "//li[contains(@class, 'slick-active')]"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step("Навести курсор любую понравившуюся картинку с пиццей"):
            go_to_element(wait, action_chains, path_pizza)
        with step("Сделать клик по картинке с пиццей"):
            action_chains.click().perform()
        with step("Проверка того, что открылась карточка товара"):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG,
            )
            assert wait.until(EC.url_contains("product"))

    @allure.title("Проверка соответствия названия пиццы в слайдере и карточке товара")
    def test_pizza_names_slider_and_product_card(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор любую понравившуюся картинку с пиццей
        2. Запомнить название пиццы и сделать клик по картинке товара
        3. Сравнить название пиццы в карточке товара с названием на картинке в слайдере
        """
        wait = WebDriverWait(selenium, timeout=5)
        action_chains = ActionChains(selenium)
        path_pizza = "//li[contains(@class, 'slick-active')]"
        path_title_pizza_in_slider = "//li[contains(@class, 'slick-active')]//h3"
        path_title_pizza_in_card = "//h1[@class='product_title entry-title']"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step("Навести курсор любую понравившуюся картинку с пиццей"):
            go_to_element(wait, action_chains, path_pizza)
        with step("Запомнить название пиццы и сделать клик по картинке товара"):
            title_pizza_in_slider = wait_visible_element(
                wait, path_title_pizza_in_slider
            ).text.lower()
            action_chains.click().perform()
        with step(
            "Сравнение название пиццы в карточке товара с названием на картинке в слайдере"
        ):
            title_pizza_in_card = wait_visible_element(
                wait, path_title_pizza_in_card
            ).text.lower()
            assert title_pizza_in_slider == title_pizza_in_card

    @allure.title("Проверка наличия дополнительных опций (сырный/колбасный борт)")
    def test_availability_of_additional_options(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор любую понравившуюся картинку с пиццей
        2. Сделать клик по картинке с пиццей
        3. Навести курсор на селектор с выбором борта для пиццы
        4. Сделать клик по селектору с выбором борта для пиццы
        5. Проверить наличие сырного и колбасного борта для пиццы
        """
        wait = WebDriverWait(selenium, timeout=5)
        action_chains = ActionChains(selenium)
        path_pizza = "//li[contains(@class, 'slick-active')]"
        path_selector = "//select"
        path_option = "//select/option"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step("Навести курсор любую понравившуюся картинку с пиццей"):
            go_to_element(wait, action_chains, path_pizza)
        with step("Сделать клик по картинке с пиццей"):
            action_chains.click().perform()
        with step("Навести курсор на селектор с выбором борта для пиццы"):
            go_to_element(wait, action_chains, path_selector)
        with step("Сделать клик по селектору с выбором борта для пиццы"):
            action_chains.click().perform()
        with step("Проверка наличие сырного и колбасного борта для пиццы"):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="screenshot_fail",
                attachment_type=allure.attachment_type.PNG,
            )
            options = wait.until(
                EC.visibility_of_all_elements_located((By.XPATH, path_option))
            )
            assert "Сырный" in options[1].text and "Колбасный" in options[2].text

    @allure.title("Выбор дополнительных опций (сырный/колбасный борт)")
    def test_selection_of_additional_options(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор любую понравившуюся картинку с пиццей
        2. Сделать клик по картинке с пиццей
        3. Навести курсор на селектор с выбором борта для пиццы
        4. Сделать клик по селектору с выбором борта для пиццы
        5. Сделать клик по любому виду борта пиццы
        6. Проверка того, что стоимость пиццы изменилась
        """
        wait = WebDriverWait(selenium, timeout=5)
        action_chains = ActionChains(selenium)
        path_pizza = "//li[contains(@class, 'slick-active')]"
        path_selector = "//select"
        path_price = "//p[@class='price']"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step("Навести курсор любую понравившуюся картинку с пиццей"):
            go_to_element(wait, action_chains, path_pizza)
        with step("Сделать клик по картинке с пиццей"):
            action_chains.click().perform()
            price = wait_visible_element(wait, path_price).text
        with step("Навести курсор на селектор с выбором борта для пиццы"):
            selector = go_to_element(wait, action_chains, path_selector)
        with step("Сделать клик по селектору с выбором борта для пиццы"):
            action_chains.click().perform()
            select = Select(selector)
        with step("Сделать клик по виду борта пиццы"):
            select.select_by_visible_text("Колбасный - 65.00 р.")
            price_with_option = wait_visible_element(wait, path_price).text
        with step("Проверка того, что стоимость пиццы изменилась"):
            assert price != price_with_option

    @allure.title("Добавление пиццы с доп. опциями в корзину")
    def test_adding_pizza_with_extras_add_options_to_cart(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор любую понравившуюся картинку с пиццей
        2. Сделать клик по картинке с пиццей
        3. Навести курсор на селектор с выбором борта для пиццы
        4. Сделать клик по селектору с выбором борта для пиццы
        5. Сделать клик по борту для пиццы "Сырный"
        6. Навести курсор на кнопку "В корзину"
        7. Сделать клик по кнопке "В корзину"
        8. Проверка того, что стоимость пиццы изменилась
        """
        wait = WebDriverWait(selenium, timeout=5)
        action_chains = ActionChains(selenium)
        path_pizza = "//li[contains(@class, 'slick-active')]"
        path_selector = "//select"
        path_button = "//button[contains(text(), 'В корзину')]"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step("Навести курсор любую понравившуюся картинку с пиццей"):
            go_to_element(wait, action_chains, path_pizza)
        with step("Сделать клик по картинке с пиццей"):
            action_chains.click().perform()
            price = wait_visible_element(wait, path_price_cart).text
        with step("Навести курсор на селектор с выбором борта для пиццы"):
            selector = go_to_element(wait, action_chains, path_selector)
        with step("Сделать клик по селектору с выбором борта для пиццы"):
            action_chains.click().perform()
            select = Select(selector)
        with step('Сделать клик по борту для пиццы "Сырный"'):
            select.select_by_visible_text("Сырный - 55.00 р.")
            selenium.execute_script("document.activeElement.blur()")
        with step('Навести курсор на кнопку "В корзину"'):
            go_to_element(wait, action_chains, path_button)
        with step('Сделать клик по кнопке "В корзину"'):
            action_chains.click().perform()
        with step("Проверка того, что стоимость пиццы изменилась"):
            price_with_option = wait_visible_element(wait, path_price_cart).text
            assert price != price_with_option
