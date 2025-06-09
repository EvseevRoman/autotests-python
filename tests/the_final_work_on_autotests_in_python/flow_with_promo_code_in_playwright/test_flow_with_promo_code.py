import allure
from allure_commons._allure import step
from playwright.sync_api import Page
from src.actions.callback.go_to_url import go_to_url
from src.actions.helper.checking_active_coupon import checking_active_coupon
from src.actions.helper.filling_shopping_cart_goods import filling_shopping_cart_goods
from src.actions.helper.input_coupon import input_coupon
from src.actions.helper.login import login_user
from src.actions.helper.making_order import making_order
from src.actions.helper.registration_user import registration_user


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature('Тестирование функционала сайта Pizzeria')
@allure.story('Флоу с промокодом на фреймворке playwright')
class TestFlowPromoCode:

    @allure.title('Проверка работы валидного купона')
    def test_valid_coupon_verification(self, go_to_url, page: Page):
        """
        Сценарий №1
        1. Заполните корзину любыми товарами.
        2. Перейдите в окно оформления товаров.
        3. Примените промокод GIVEMEHALYAVA.
        4. Убедитесь, что конечная сумма заказа уменьшилась на 10%.

        Шаги:
            1. Перейти на главную страницу
            2. Навести курсор на любую пиццу в слайдере
            3. Сделать клик по кнопке "В корзину"
            4. Навести курсор на другую пиццу в слайдере
            5. Сделать клик по кнопке "В корзину"
            6. Перейти на страницу "Оформление заказа"
            7. Проверить что нет активного купона, если есть удалить
            9. Сделать клик по ссылке "Нажмите для ввода купона"
            10. Ввести в поле купон
            11. Нажать на кнопку "Применить купон"
            12. Проверить, что сумма заказа уменьшилась на 10%

        Предусловие: пользователь зарегистрирован и авторизован на сайте https://pizzeria.skillbox.cc/

        Тестовые данные:
             Username = zlo
             Password = qwe123!@#
             Coupon = GIVEMEHALYAVA
        """
        path_order_subtotal = "//tr[@class='cart-subtotal']//bdi"
        path_order_total = "//tr[@class='order-total']//bdi"
        coupon = "GIVEMEHALYAVA"
        username = "zlo"
        password = "qwe123!@#"

        go_to_url("https://pizzeria.skillbox.cc/")
        login_user(page, username, password)
        page.wait_for_timeout(1000)
        filling_shopping_cart_goods(page)
        page.wait_for_timeout(1000)
        checking_active_coupon(page)
        page.wait_for_timeout(1000)
        input_coupon(page, coupon)

        with step('Проверить, что сумма заказа уменьшилась на 10%'):
            page.wait_for_timeout(1000)
            page.locator(path_order_total).scroll_into_view_if_needed()
            order_subtotal = float(page.locator(path_order_subtotal).inner_text()[:-1].replace(',', '.'))
            order_total = float(page.locator(path_order_total).inner_text()[:-1].replace(',', '.'))
            assert order_subtotal * 0.9 == order_total, f"Купон {coupon} не применился!"
        pass

    @allure.title('Проверка не валидного купона')
    def test_checking_invalid_coupon(self, go_to_url, page: Page):
        """
        Сценарий №2
        1. Заполните корзину любыми товарами.
        2. Перейдите в окно оформления товаров.
        3. Примените промокод DC120.
        4. Убедитесь, что конечная сумма заказа НЕ уменьшилась на 10% и промокод не
        применился.

        Шаги:
            1. Перейти на главную страницу
            2. Навести курсор на любую пиццу в слайдере
            3. Сделать клик по кнопке "В корзину"
            4. Навести курсор на другую пиццу в слайдере
            5. Сделать клик по кнопке "В корзину"
            6. Перейти на страницу "Оформление заказа"
            7. Проверить что нет активного купона, если есть удалить
            9. Сделать клик по ссылке "Нажмите для ввода купона"
            10. Ввести в поле купон
            11. Нажать на кнопку "Применить купон"
            12. Проверить, что сумма заказа не изменилась

        Предусловие: пользователь зарегистрирован и авторизован на сайте https://pizzeria.skillbox.cc/

        Тестовые данные:
             Username = zlo
             Password = qwe123!@#
             Coupon = DC120
        """
        path_order_subtotal = "//tr[@class='cart-subtotal']//bdi"
        path_order_total = "//tr[@class='order-total']//bdi"
        coupon = "DC120"
        username = "zlo"
        password = "qwe123!@#"

        go_to_url("https://pizzeria.skillbox.cc/")
        login_user(page, username, password)
        page.wait_for_timeout(1000)
        filling_shopping_cart_goods(page)
        page.wait_for_timeout(1000)
        checking_active_coupon(page)
        page.wait_for_timeout(1000)
        input_coupon(page, coupon)

        with step('Проверить, что сумма заказа не изменилась'):
            page.wait_for_timeout(1000)
            page.locator(path_order_total).scroll_into_view_if_needed()
            order_subtotal = float(page.locator(path_order_subtotal).inner_text()[:-1].replace(',', '.'))
            order_total = float(page.locator(path_order_total).inner_text()[:-1].replace(',', '.'))
            assert order_subtotal == order_total, f"Купон {coupon} был успешно применён!"
        pass

    @allure.title('Проверка работы купона, при не работающем сервере')
    def test_coupon_application_wthen_server_down(self, go_to_url, page: Page):
        """
        Сценарий №3
        1. Заполните корзину любыми товарами.
        2. Перейдите в окно оформления товаров.
        3. Примените промокод GIVEMEHALYAVA.
        4. Перехватите запрос, уходящий с веба на сервер, и заблокируйте его. Не
        возвращайте ответ или верните с ошибкой (500, например).
        5. Убедитесь, что конечная сумма заказа НЕ уменьшилась на 10% и промокод не
        применился.
        6. Как думаете, как сайт должен отреагировать на такую ситуацию? Ожидаем ли
        мы какого-нибудь сообщения для пользователя?

        Шаги:
            1. Перейти на главную страницу
            2. Навести курсор на любую пиццу в слайдере
            3. Сделать клик по кнопке "В корзину"
            4. Навести курсор на другую пиццу в слайдере
            5. Сделать клик по кнопке "В корзину"
            6. Перейти на страницу "Оформление заказа"
            7. Проверить что нет активного купона, если есть удалить
            8. Сделать клик по ссылке "Нажмите для ввода купона"
            9. Ввести в поле купон
            10. Нажать на кнопку "Применить купон"
            11. Перехватить запрос и изменить сообщение

        Предусловие: пользователь зарегистрирован и авторизован на сайте https://pizzeria.skillbox.cc/

        Тестовые данные:
             Username = zlo
             Password = qwe123!@#
             Coupon = GIVEMEHALYAVA
        """
        path_order_subtotal = "//tr[@class='cart-subtotal']//bdi"
        path_order_total = "//tr[@class='order-total']//bdi"
        coupon = "GIVEMEHALYAVA"
        username = "zlo"
        password = "qwe123!@#"

        def handle(route):
            route.fulfill(
                status=500,
            )
        page.route("**/?wc-ajax=apply_coupon", handle)

        go_to_url("https://pizzeria.skillbox.cc/")
        login_user(page, username, password)
        page.wait_for_timeout(1000)
        filling_shopping_cart_goods(page)
        page.wait_for_timeout(1000)
        checking_active_coupon(page)
        page.wait_for_timeout(1000)
        input_coupon(page, coupon)

        with step('Проверить, что сумма заказа не изменилась'):
            page.wait_for_timeout(1000)
            page.locator(path_order_total).scroll_into_view_if_needed()
            order_subtotal = float(page.locator(path_order_subtotal).inner_text()[:-1].replace(',', '.'))
            order_total = float(page.locator(path_order_total).inner_text()[:-1].replace(',', '.'))
            assert order_subtotal == order_total, f"Купон {coupon} был успешно применён!"
        pass

    @allure.title('Проверка повторного использования купона')
    def test_coupon_reuse_check(self, go_to_url, page: Page):
        """
        Сценарий №4
        1. зарегистрируйте одного пользователя;
        2. сделайте любой заказ;
        3. примените промокод GIVEMEHALYAVA;
        4. оформите заказ;
        5. попробуйте оформить второй заказ с этим же промокодом;
        6. убедитесь, что второй раз промокод уже не срабатывает для пользователя.

        Шаги:
            1. Перейти на страницу "Мой аккаунт"
            2. Сделать клик по кнопке "Зарегистрироваться"
            3. Заполнить обязательные поля валидными значениями
            4. Нажать на кнопку "Зарегистрироваться"
            5. Перейти на главную страницу
            6. Навести курсор на любую пиццу в слайдере
            7. Сделать клик по кнопке "В корзину"
            8. Навести курсор на другую пиццу в слайдере
            9. Сделать клик по кнопке "В корзину"
            10. Проверить что нет активного купона, если есть удалить
            11. Перейти на страницу "Оформление заказа"
            12. Сделать клик по ссылке "Нажмите для ввода купона"
            13. Ввести в поле купон
            14. Нажать на кнопку "Применить купон"
            15. Заполнить все обязательные поля формы "Детали заказа"
            16. Нажать на кнопку "Оформить заказ"
            17. Перейти на главную страницу
            18. Навести курсор на любую пиццу в слайдере
            19. Сделать клик по кнопке "В корзину"
            20. Навести курсор на другую пиццу в слайдере
            21. Сделать клик по кнопке "В корзину"
            22. Перейти на страницу "Оформление заказа"
            23. Сделать клик по ссылке "Нажмите для ввода купона"
            24. Ввести в поле купон
            25. Нажать на кнопку "Применить купон"
            26. Заполнить все обязательные поля формы "Детали заказа"
            27. Нажать на кнопку "Оформить заказ"
            28. Проверить, что купон при втором заказе не применился

        Предусловие: пользователь не зарегистрирован и не авторизован на сайте https://pizzeria.skillbox.cc/

        Тестовые данные:
             Username = zlo1
             Password = qwe123!@#
             Coupon = GIVEMEHALYAVA
        """
        path_order_subtotal = "//th[contains(text(), 'Subtotal')]/following-sibling::td/span"
        path_order_total = "//th[contains(text(), 'Total')]/following-sibling::td/span"
        coupon = "GIVEMEHALYAVA"
        username = "po15"
        email = "po15@mail.ru"
        password = "qwe123!@#"
        value_telephone = "89005008000"

        go_to_url("https://pizzeria.skillbox.cc/")
        registration_user(page, username, email, password)
        page.wait_for_timeout(1000)
        filling_shopping_cart_goods(page)
        page.wait_for_timeout(1000)
        checking_active_coupon(page)
        page.wait_for_timeout(1000)
        input_coupon(page, coupon)
        page.wait_for_timeout(1000)
        making_order(page, value_telephone)
        page.wait_for_timeout(1000)
        filling_shopping_cart_goods(page)
        page.wait_for_timeout(1000)
        input_coupon(page, coupon)
        page.wait_for_timeout(1000)
        making_order(page, value_telephone)

        with step('Проверить, что купон при втором заказе не применился'):
            page.wait_for_timeout(1000)
            page.locator(path_order_total).scroll_into_view_if_needed()
            order_subtotal = float(page.locator(path_order_subtotal).inner_text()[:-1].replace(',', '.'))
            order_total = float(page.locator(path_order_total).inner_text()[:-1].replace(',', '.'))
            assert order_subtotal == order_total, f"Повторное использование купона {coupon} прошло успешно!"
        pass
