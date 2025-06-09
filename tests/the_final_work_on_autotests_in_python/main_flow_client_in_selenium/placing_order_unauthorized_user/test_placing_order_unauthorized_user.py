import allure

from allure_commons._allure import step
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from src.actions.helper.go_to_element import go_to_element
from src.actions.helper.logout import logout
from src.actions.waits.wait_visible_element import wait_visible_element


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature('Тестирование функционала сайта Pizzeria')
@allure.story('Оформление заказа не авторизованным пользователем')
class TestPlacingOrderUnauthorizedUser:

    @allure.title('Отображение кнопки "Оформить заказ" в корзине при оформлении заказа не авторизованным пользователем')
    def test_displaying_place_order_button(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Убедиться в налии кнопки "ОФОРМИТЬ ЗАКАЗ"
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_first_pizza = "//li[contains(@class, 'slick-active')]"
        path_first_button = "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"
        path_button_place_order = "//a[contains(text(), 'ОФОРМИТЬ ЗАКАЗ')]"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на любую пиццу в слайдере'):
            go_to_element(wait, action_chains, path_first_pizza)
        with step('Навести курсор на кнопку "В корзину"'):
            go_to_element(wait, action_chains, path_first_button)
        with step('Сделать клик по кнопке "В корзину"'):
            action_chains.click().perform()
        with step('Навести курсор на иконку корзины'):
            go_to_element(wait, action_chains, path_price_cart)
        with step('Сделать клик по иконке корзины'):
            action_chains.click().perform()

        with step('Убедиться в налии кнопки "ОФОРМИТЬ ЗАКАЗ"'):
            wait.until(EC.url_contains("https://pizzeria.skillbox.cc/cart/"))
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="Кнопка 'ОФОРМИТЬ ЗАКАЗ' не найдена",
                attachment_type=allure.attachment_type.PNG
            )
            assert wait_visible_element(wait, path_button_place_order), "Кнопка 'ОФОРМИТЬ ЗАКАЗ' не найдена"

    @allure.title('Оформление заказа не авторизованным пользователем при нажатии кнопки "Перейти к оплате"')
    def test_placing_order_unauthorized_user(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Навести курсор на кнопку "Перейти к оплате"
        7. Убедиться в наличии ссылок авторизации и купон
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        path_first_pizza = "//li[contains(@class, 'slick-active')]"
        path_first_button = "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"
        path_button_proceed_payment = "//a[contains(@class, 'checkout-button')]"
        path_link_authorization = "//a[@class='showlogin']"
        path_link_coupon = "//a[@class='showcoupon']"

        open_page("https://pizzeria.skillbox.cc/")
        logout(wait, action_chains, go_to_element)

        with step('Навести курсор на любую пиццу в слайдере'):
            go_to_element(wait, action_chains, path_first_pizza)
        with step('Навести курсор на кнопку "В корзину"'):
            go_to_element(wait, action_chains, path_first_button)
        with step('Сделать клик по кнопке "В корзину"'):
            action_chains.click().perform()
        with step('Навести курсор на иконку корзины'):
            go_to_element(wait, action_chains, path_price_cart)
        with step('Сделать клик по иконке корзины'):
            action_chains.click().perform()
        with step('Навести курсор на кнопку "Перейти к оплате"'):
            go_to_element(wait, action_chains, path_button_proceed_payment)
        with step('Сделать клик по кнопке "Перейти к оплате"'):
            action_chains.click().perform()

        with step('Убедиться в наличии ссылок авторизации и купон'):
            wait.until(EC.url_contains("https://pizzeria.skillbox.cc/checkout/"))
            allure.attach(
                selenium.get_screenshot_as_png(),
                name='Cтраница "Оформление Заказа"',
                attachment_type=allure.attachment_type.PNG
            )
            link_authorization = wait_visible_element(wait, path_link_authorization).text
            link_coupon = wait_visible_element(wait, path_link_coupon).text
            assert link_authorization == "Авторизуйтесь" and link_coupon == "Нажмите для ввода купона"
