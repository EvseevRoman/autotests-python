import allure

from allure_commons._allure import step
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from src.actions.helper.go_to_element import go_to_element
from src.actions.waits.wait_visible_element import wait_visible_element
from src.actions.helper.authorization_user import authorization_user


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature('Тестирование функционала сайта Pizzeria')
@allure.story('Оформление заказа авторизованным пользователем')
class TestPlacingOrderAuthorizedUser:

    @allure.title('Отображение кнопки "Перейти к оплате" на странице корзины')
    def test_displaying_button_proceed_payment(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Убедиться в налии кнопки "Перейти к оплате"
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        username = "zlo"
        password = "qwe123!@#"
        path_first_pizza = "//li[contains(@class, 'slick-active')]"
        path_first_button = "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"
        path_button_proceed_payment = "//a[contains(@class, 'checkout-button')]"
        path_button_authoriz = "//div[@class='login-woocommerce']"

        open_page("https://pizzeria.skillbox.cc/")
        with step('Проверка авторизации пользователя'):
            button_authoriz = wait_visible_element(wait, path_button_authoriz).text
            if button_authoriz == "Войти":
                authorization_user(wait, action_chains, go_to_element, username, password)

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

        with step('Убедиться в налии кнопки "ПЕРЕЙТИ К ОПЛАТЕ"'):
            wait.until(EC.url_contains("https://pizzeria.skillbox.cc/cart/"))
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="Кнопка 'ПЕРЕЙТИ К ОПЛАТЕ'",
                attachment_type=allure.attachment_type.PNG
            )
            assert wait_visible_element(wait, path_button_proceed_payment)
            pass

    @allure.title('Ввод данных в форме "Оформление заказа", авторизованным пользователем')
    def test_data_entry_checkout_form(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Навести курсор на кнопку "Перейти к оплате"
        7. Сделать клик по кнопке "Перейти к оплате"
        8. Навести курсор на поле "Имя"
        9. Сделать клик по полю "Имя"
        10. Ввести в поле имя валидное значение
        11. Навести курсор на поле "Фамилия"
        12. Сделать клик по полю "Фамилия"
        13. Ввести валидное значение в поле "Фамилия"
        14. Навести курсор на поле "Адрес"
        15. Сделать клик по полю "Адрес"
        16. Ввести валидный адрес доставки
        17. Навести курсор на поле "Город"
        18. Сделать клик по полю "Город"
        19. Ввести валидное название города
        20. Навести курсор на поле "Область"
        21. Сделать клик по полю "Область"
        22. Ввести корректное название области
        23. Навести курсор на поле "Почтовый индекс"
        24. Сделать клик по полю "Почтовый индекс"
        25. Ввести в поле "Почтовый индекс" валидный индекс
        26. Навести курсор на поле "Телефон"
        27. Сделать клик по полю "Телефон"
        28. Ввести в поле "Телефон" валидный номер телефона
        29. Убедиться, что все поля заполнены введёнными значениями
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        username = "zlo"
        password = "qwe123!@#"
        path_first_pizza = "//li[contains(@class, 'slick-active')]"
        path_first_button = "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"
        path_button_proceed_payment = "//a[contains(@class, 'checkout-button')]"
        path_field_name = "//input[@name='billing_first_name']"
        path_field_surname = "//input[@name='billing_last_name']"
        path_field_address = "//input[@name='billing_address_1']"
        path_field_city = "//input[@name='billing_city']"
        path_field_area = "//input[@name='billing_state']"
        path_field_index = "//input[@name='billing_postcode']"
        path_field_telephone = "//input[@name='billing_phone']"
        value_name = "Вася"
        value_surname = "Пупкин"
        value_address = "ул. Взлётная, д. 9"
        value_city = "Москва"
        value_area = "Московская область"
        value_index = "101000"
        value_telephone = "89005008000"
        path_button_authoriz = "//div[@class='login-woocommerce']"

        open_page("https://pizzeria.skillbox.cc/")
        with step('Проверка авторизации пользователя'):
            button_authoriz = wait_visible_element(wait, path_button_authoriz).text
            if button_authoriz == "Войти":
                authorization_user(wait, action_chains, go_to_element, username, password)

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
        with step('Сделать клик по кнопке "Перейти к оплате'):
            action_chains.click().perform()
        with step('Навести курсор на поле "Имя"'):
            field_name = go_to_element(wait, action_chains, path_field_name)
        with step('Сделать клик по полю "Имя"'):
            action_chains.click().perform()
        with step('Ввести в поле имя валидное значение'):
            field_name.clear()
            field_name.send_keys(value_name)
        with step('Навести курсор на поле "Фамилия"'):
            field_surname = go_to_element(wait, action_chains, path_field_surname)
        with step('Сделать клик по полю "Фамилия"'):
            action_chains.click().perform()
        with step('Ввести валидное значение в поле "Фамилия"'):
            field_surname.clear()
            field_surname.send_keys(value_surname)
        with step('Навести курсор на поле "Адрес"'):
            field_address = go_to_element(wait, action_chains, path_field_address)
        with step('Сделать клик по полю "Адрес"'):
            action_chains.click().perform()
        with step('Ввести валидный адрес доставки'):
            field_address.clear()
            field_address.send_keys(value_address)
        with step('Навести курсор на поле "Город"'):
            field_city = go_to_element(wait, action_chains, path_field_city)
        with step('Сделать клик по полю "Город"'):
            action_chains.click().perform()
        with step('Ввести валидное название города'):
            field_city.clear()
            field_city.send_keys(value_city)
        with step('Навести курсор на поле "Область"'):
            field_area = go_to_element(wait, action_chains, path_field_area)
        with step('Сделать клик по полю "Область"'):
            action_chains.click().perform()
        with step('Ввести корректное название области'):
            field_area.clear()
            field_area.send_keys(value_area)
        with step('Навести курсор на поле "Почтовый индекс"'):
            field_index = go_to_element(wait, action_chains, path_field_index)
        with step('Сделать клик по полю "Почтовый индекс"'):
            action_chains.click().perform()
        with step('Ввести в поле "Почтовый индекс" валидный индекс'):
            field_index.clear()
            field_index.send_keys(value_index)
        with step('Навести курсор на поле "Телефон"'):
            field_telephone = go_to_element(wait, action_chains, path_field_telephone)
        with step('Сделать клик по полю "Телефон"'):
            action_chains.click().perform()
        with step('Ввести в поле "Телефон" валидный номер телефона'):
            field_telephone.clear()
            field_telephone.send_keys(value_telephone)

        with step('Убедиться, что все поля заполнены введёнными значениями'):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="Форма 'Детали заказа'",
                attachment_type=allure.attachment_type.PNG
            )
            assert field_name.get_attribute("value") == value_name
            assert field_surname.get_attribute("value") == value_surname
            assert field_address.get_attribute("value") == value_address
            assert field_city.get_attribute("value") == value_city
            assert field_area.get_attribute("value") == value_area
            assert field_index.get_attribute("value") == value_index
            assert field_telephone.get_attribute("value") == value_telephone
            pass

    @allure.title('Ввод даты оформления доставки на завтра, авторизованным пользователем')
    def test_entering_delivery_date(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Навести курсор на кнопку "Перейти к оплате"
        7. Сделать клик по кнопке "Перейти к оплате"
        8. Навести курсор на поле "Дата заказа"
        9. Сделать клик по полю "Дата заказа"
        10. Ввести завтрашнюю дату
        11. Убедиться, что поле принимает и корректно отображает введённую дату
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        username = "zlo"
        password = "qwe123!@#"
        path_first_pizza = "//li[contains(@class, 'slick-active')]"
        path_first_button = "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"
        path_button_proceed_payment = "//a[contains(@class, 'checkout-button')]"
        path_calendar = "//input[@name='order_date']"
        date = "04062025"
        path_button_authoriz = "//div[@class='login-woocommerce']"

        open_page("https://pizzeria.skillbox.cc/")
        with step('Проверка авторизации пользователя'):
            button_authoriz = wait_visible_element(wait, path_button_authoriz).text
            if button_authoriz == "Войти":
                authorization_user(wait, action_chains, go_to_element, username, password)

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
        with step('Сделать клик по кнопке "Перейти к оплате'):
            action_chains.click().perform()
        with step('Навести курсор на поле "Дата заказа"'):
            calendar = go_to_element(wait, action_chains, path_calendar)
        with step('Сделать клик по полю "Дата заказа"'):
            action_chains.click().perform()
        with step('Ввести завтрашнюю дату'):
            calendar.send_keys(date)

        with step('Убедиться. что поле принимает и корректно отображает введённую дату'):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="Дата доставки",
                attachment_type=allure.attachment_type.PNG
            )
            expect_date = ''.join(reversed(calendar.get_attribute("value").split("-")))
            assert expect_date == date
            pass

    @allure.title('Выбор формы оплаты "Оплата при доставке" ')
    def test_choosing_form_payment(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Навести курсор на кнопку "Перейти к оплате"
        7. Сделать клик по кнопке "Перейти к оплате"
        8. Навести курсор на радиокнопку "Оплата при доставке"
        9. Сделать клик по кнопке "Оплата при доставке"
        """
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)
        username = "zlo"
        password = "qwe123!@#"
        path_first_pizza = "//li[contains(@class, 'slick-active')]"
        path_first_button = "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"
        path_button_proceed_payment = "//a[contains(@class, 'checkout-button')]"
        path_radiobutton = "//input[@id='payment_method_cod']"
        message = 'Оплата наличными при доставке заказа.'
        path_message = "//div[contains(@class, 'payment_method_cod')]/p"
        path_button_authoriz = "//div[@class='login-woocommerce']"

        open_page("https://pizzeria.skillbox.cc/")
        with step('Проверка авторизации пользователя'):
            button_authoriz = wait_visible_element(wait, path_button_authoriz).text
            if button_authoriz == "Войти":
                authorization_user(wait, action_chains, go_to_element, username, password)

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
        with step('Сделать клик по кнопке "Перейти к оплате'):
            action_chains.click().perform()
        with step('Навести курсор на радиокнопку "Оплата при доставке"'):
            radiobutton = go_to_element(wait, action_chains, path_radiobutton)
        with step('Сделать клик по кнопке "Оплата при доставке"'):
            action_chains.click().perform()

        with step('Убедиться, что появилось сообщение и радиокнопка стала активна'):
            allure.attach(
                selenium.get_screenshot_as_png(),
                name="Дата доставки",
                attachment_type=allure.attachment_type.PNG
            )
            expect_message = wait_visible_element(wait, path_message).text
            assert expect_message == message
            assert radiobutton.is_selected() is True
            pass

    @allure.title('Подтверждение заказа нажатием на кнопку "Оформить заказ"')
    def test_order_confirmation(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Навести курсор на кнопку "Перейти к оплате"
        7. Сделать клик по кнопке "Перейти к оплате"
        8. Навести курсор на поле "Имя"
        9. Сделать клик по полю "Имя"
        10. Ввести в поле имя валидное значение
        11. Навести курсор на поле "Фамилия"
        12. Сделать клик по полю "Фамилия"
        13. Ввести валидное значение в поле "Фамилия"
        14. Навести курсор на поле "Адрес"
        15. Сделать клик по полю "Адрес"
        16. Ввести валидный адрес доставки
        17. Навести курсор на поле "Город"
        18. Сделать клик по полю "Город"
        19. Ввести валидное название города
        20. Навести курсор на поле "Область"
        21. Сделать клик по полю "Область"
        22. Ввести корректное название области
        23. Навести курсор на поле "Почтовый индекс"
        24. Сделать клик по полю "Почтовый индекс"
        25. Ввести в поле "Почтовый индекс" валидный индекс
        26. Навести курсор на поле "Телефон"
        27. Сделать клик по полю "Телефон"
        28. Ввести в поле "Телефон" валидный номер телефона
        29. Навести курсор на поле "Дата заказа"
        30. Сделать клик по полю "Дата заказа"
        31. Ввести в поле "Дата заказа", завтрашнюю дату
        32. Навести курсор на радиокнопку "Оплата при доставке"
        33. Сделать клик по кнопке "Оплата при доставке"
        34. Навести курсор на чек-бокс с согласием об использовании веб-сайта
        35. Сделать клик по чек-боксу
        36. Навести курсор на кнопку "Оформить заказ"
        37. Сделать клик по кнопке "Оформить заказ"
        38. Убедиться, что открылась страница с подтверждением полученного заказа
        """
        wait = WebDriverWait(selenium, timeout=30)
        action_chains = ActionChains(selenium)
        username = "zlo"
        password = "qwe123!@#"
        path_first_pizza = "//li[contains(@class, 'slick-active')]"
        path_first_button = "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"
        path_button_proceed_payment = "//a[contains(@class, 'checkout-button')]"
        path_field_name = "//input[@name='billing_first_name']"
        path_field_surname = "//input[@name='billing_last_name']"
        path_field_address = "//input[@name='billing_address_1']"
        path_field_city = "//input[@name='billing_city']"
        path_field_area = "//input[@name='billing_state']"
        path_field_index = "//input[@name='billing_postcode']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_calendar = "//input[@name='order_date']"
        path_radiobutton = "//input[@id='payment_method_cod']"
        path_checkbox = "//input[@type='checkbox']"
        path_place_order = "//button[@value='Оформить заказ']"
        date = "04062025"
        value_name = "Вася"
        value_surname = "Пупкин"
        value_address = "ул. Взлётная, д. 9"
        value_city = "Москва"
        value_area = "Московская область"
        value_index = "101000"
        value_telephone = "89005008000"
        path_button_authoriz = "//div[@class='login-woocommerce']"

        open_page("https://pizzeria.skillbox.cc/")
        with step('Проверка авторизации пользователя'):
            button_authoriz = wait_visible_element(wait, path_button_authoriz).text
            if button_authoriz == "Войти":
                authorization_user(wait, action_chains, go_to_element, username, password)

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
        with step('Сделать клик по кнопке "Перейти к оплате'):
            action_chains.click().perform()
        with step('Навести курсор на поле "Имя"'):
            ActionBuilder(selenium).clear_actions()
            field_name = go_to_element(wait, action_chains, path_field_name)
        with step('Сделать клик по полю "Имя"'):
            action_chains.click().perform()
        with step('Ввести в поле имя валидное значение'):
            field_name.clear()
            field_name.send_keys(value_name)
        with step('Навести курсор на поле "Фамилия"'):
            field_surname = go_to_element(wait, action_chains, path_field_surname)
        with step('Сделать клик по полю "Фамилия"'):
            action_chains.click().perform()
        with step('Ввести валидное значение в поле "Фамилия"'):
            field_surname.clear()
            field_surname.send_keys(value_surname)
        with step('Навести курсор на поле "Адрес"'):
            field_address = go_to_element(wait, action_chains, path_field_address)
        with step('Сделать клик по полю "Адрес"'):
            action_chains.click().perform()
        with step('Ввести валидный адрес доставки'):
            field_address.clear()
            field_address.send_keys(value_address)
        with step('Навести курсор на поле "Город"'):
            field_city = go_to_element(wait, action_chains, path_field_city)
        with step('Сделать клик по полю "Город"'):
            action_chains.click().perform()
        with step('Ввести валидное название города'):
            field_city.clear()
            field_city.send_keys(value_city)
        with step('Навести курсор на поле "Область"'):
            field_area = go_to_element(wait, action_chains, path_field_area)
        with step('Сделать клик по полю "Область"'):
            action_chains.click().perform()
        with step('Ввести корректное название области'):
            field_area.clear()
            field_area.send_keys(value_area)
        with step('Навести курсор на поле "Почтовый индекс"'):
            field_index = go_to_element(wait, action_chains, path_field_index)
        with step('Сделать клик по полю "Почтовый индекс"'):
            action_chains.click().perform()
        with step('Ввести в поле "Почтовый индекс" валидный индекс'):
            field_index.clear()
            field_index.send_keys(value_index)
        with step('Навести курсор на поле "Телефон"'):
            field_telephone = go_to_element(wait, action_chains, path_field_telephone)
        with step('Сделать клик по полю "Телефон"'):
            action_chains.click().perform()
        with step('Ввести в поле "Телефон" валидный номер телефона'):
            field_telephone.clear()
            field_telephone.send_keys(value_telephone)
        with step('Навести курсор на поле "Дата заказа"'):
            calendar = go_to_element(wait, action_chains, path_calendar)
        with step('Сделать клик по полю "Дата заказа"'):
            action_chains.click().perform()
        with step('Ввести в поле "Дата заказа", завтрашнюю дату'):
            calendar.send_keys(date)
        with step('Навести курсор на радиокнопку "Оплата при доставке"'):
            go_to_element(wait, action_chains, path_radiobutton)
        with step('Сделать клик по кнопке "Оплата при доставке"'):
            action_chains.click().perform()
        with step('Навести курсор на чек-бокс с согласием об использовании веб-сайта'):
            checkbox = go_to_element(wait, action_chains, path_checkbox)
        with step('Сделать клик по чек-боксу'):
            action_chains.click(checkbox).perform()
        with step('Навести курсор на кнопку "Оформить заказ"'):
            go_to_element(wait, action_chains, path_place_order)
        with step('Сделать клик по кнопке "Оформить заказ"'):
            action_chains.click().perform()

        with step('Убедиться, что открылась страница с подтверждением полученного заказа'):
            assert wait.until(EC.url_contains('order-received'))
            pass

    @allure.title('Проверка корректности введённых данных и суммы заказа при оформлении заказа')
    def test_checking_correctness_data_and_order(self, open_page, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Навести курсор на кнопку "Перейти к оплате"
        7. Сделать клик по кнопке "Перейти к оплате"
        8. Навести курсор на поле "Имя"
        9. Сделать клик по полю "Имя"
        10. Ввести в поле имя валидное значение
        11. Навести курсор на поле "Фамилия"
        12. Сделать клик по полю "Фамилия"
        13. Ввести валидное значение в поле "Фамилия"
        14. Навести курсор на поле "Адрес"
        15. Сделать клик по полю "Адрес"
        16. Ввести валидный адрес доставки
        17. Навести курсор на поле "Город"
        18. Сделать клик по полю "Город"
        19. Ввести валидное название города
        20. Навести курсор на поле "Область"
        21. Сделать клик по полю "Область"
        22. Ввести корректное название области
        23. Навести курсор на поле "Почтовый индекс"
        24. Сделать клик по полю "Почтовый индекс"
        25. Ввести в поле "Почтовый индекс" валидный индекс
        26. Навести курсор на поле "Телефон"
        27. Сделать клик по полю "Телефон"
        28. Ввести в поле "Телефон" валидный номер телефона
        29. Навести курсор на поле "Дата заказа"
        30. Сделать клик по полю "Дата заказа"
        31. Ввести в поле "Дата заказа", завтрашнюю дату
        32. Навести курсор на радиокнопку "Оплата при доставке"
        33. Сделать клик по кнопке "Оплата при доставке"
        34. Навести курсор на чек-бокс с согласием об использовании веб-сайта
        35. Сделать клик по чек-боксу
        36. Навести курсор на кнопку "Оформить заказ"
        37. Сделать клик по кнопке "Оформить заказ"
        38. Проверить корректность введённых данных и суммы заказа на странице подтверждения заказа
        """
        wait = WebDriverWait(selenium, timeout=30)
        action_chains = ActionChains(selenium)
        username = "zlo"
        password = "qwe123!@#"
        path_button_authoriz = "//div[@class='login-woocommerce']"
        path_first_pizza = "//li[contains(@class, 'slick-active')]"
        path_first_button = "//li[contains(@class, 'slick-active')]//a[contains(text(), 'В корзину')]"
        path_price_cart = "//a[contains(@class, 'cart-contents')]"
        path_button_proceed_payment = "//a[contains(@class, 'checkout-button')]"
        path_field_name = "//input[@name='billing_first_name']"
        path_field_surname = "//input[@name='billing_last_name']"
        path_field_address = "//input[@name='billing_address_1']"
        path_field_city = "//input[@name='billing_city']"
        path_field_area = "//input[@name='billing_state']"
        path_field_index = "//input[@name='billing_postcode']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_field_email = "//input[@name='billing_email']"
        path_calendar = "//input[@name='order_date']"
        path_radiobutton = "//input[@id='payment_method_cod']"
        path_checkbox = "//input[@type='checkbox']"
        path_button_place_order = "//button[@value='Оформить заказ']"
        path_expected_date = "//li[contains(text(), 'Дата:')]/strong"
        path_expected_amount_order = "//li[contains(text(), 'В сумме:')]//bdi"
        path_expected_method_payment = "//li[contains(text(), 'Метод оплаты:')]/strong"
        path_expected_address = "//address"
        value_date = "05062025"
        value_name = "Вася"
        value_surname = "Пупкин"
        value_address = "ул. Взлётная, д. 9"
        value_city = "Москва"
        value_area = "Московская область"
        value_index = "101000"
        value_telephone = "89005008000"

        open_page("https://pizzeria.skillbox.cc/")
        with step('Проверка авторизации пользователя'):
            button_authoriz = wait_visible_element(wait, path_button_authoriz).text
            if button_authoriz == "Войти":
                authorization_user(wait, action_chains, go_to_element, username, password)

        with step('Навести курсор на любую пиццу в слайдере'):
            go_to_element(wait, action_chains, path_first_pizza)
        with step('Навести курсор на кнопку "В корзину"'):
            go_to_element(wait, action_chains, path_first_button)
        with step('Сделать клик по кнопке "В корзину"'):
            action_chains.click().perform()
        with step('Навести курсор на иконку корзины'):
            go_to_element(wait, action_chains, path_price_cart)
            value_amount_order = wait_visible_element(wait, path_price_cart).text
        with step('Сделать клик по иконке корзины'):
            action_chains.click().perform()
        with step('Навести курсор на кнопку "Перейти к оплате"'):
            go_to_element(wait, action_chains, path_button_proceed_payment)
        with step('Сделать клик по кнопке "Перейти к оплате'):
            action_chains.click().perform()
        with step('Навести курсор на поле "Имя"'):
            field_name = go_to_element(wait, action_chains, path_field_name)
        with step('Сделать клик по полю "Имя"'):
            action_chains.click().perform()
        with step('Ввести в поле имя валидное значение'):
            field_name.clear()
            field_name.send_keys(value_name)
        with step('Навести курсор на поле "Фамилия"'):
            field_surname = go_to_element(wait, action_chains, path_field_surname)
        with step('Сделать клик по полю "Фамилия"'):
            action_chains.click().perform()
        with step('Ввести валидное значение в поле "Фамилия"'):
            field_surname.clear()
            field_surname.send_keys(value_surname)
        with step('Навести курсор на поле "Адрес"'):
            field_address = go_to_element(wait, action_chains, path_field_address)
        with step('Сделать клик по полю "Адрес"'):
            action_chains.click().perform()
        with step('Ввести валидный адрес доставки'):
            field_address.clear()
            field_address.send_keys(value_address)
        with step('Навести курсор на поле "Город"'):
            field_city = go_to_element(wait, action_chains, path_field_city)
        with step('Сделать клик по полю "Город"'):
            action_chains.click().perform()
        with step('Ввести валидное название города'):
            field_city.clear()
            field_city.send_keys(value_city)
        with step('Навести курсор на поле "Область"'):
            field_area = go_to_element(wait, action_chains, path_field_area)
        with step('Сделать клик по полю "Область"'):
            action_chains.click().perform()
        with step('Ввести корректное название области'):
            field_area.clear()
            field_area.send_keys(value_area)
        with step('Навести курсор на поле "Почтовый индекс"'):
            field_index = go_to_element(wait, action_chains, path_field_index)
        with step('Сделать клик по полю "Почтовый индекс"'):
            action_chains.click().perform()
        with step('Ввести в поле "Почтовый индекс" валидный индекс'):
            field_index.clear()
            field_index.send_keys(value_index)
        with step('Навести курсор на поле "Телефон"'):
            field_telephone = go_to_element(wait, action_chains, path_field_telephone)
        with step('Сделать клик по полю "Телефон"'):
            action_chains.click().perform()
        with step('Ввести в поле "Телефон" валидный номер телефона'):
            field_telephone.clear()
            field_telephone.send_keys(value_telephone)
            value_email = wait_visible_element(wait, path_field_email).get_attribute("value")
        with step('Навести курсор на поле "Дата заказа"'):
            calendar = go_to_element(wait, action_chains, path_calendar)
        with step('Сделать клик по полю "Дата заказа"'):
            action_chains.click().perform()
        with step('Ввести в поле "Дата заказа", завтрашнюю дату'):
            calendar.send_keys(value_date)
        with step('Навести курсор на радиокнопку "Оплата при доставке"'):
            go_to_element(wait, action_chains, path_radiobutton)
        with step('Сделать клик по кнопке "Оплата при доставке"'):
            action_chains.click().perform()
        with step('Навести курсор на чек-бокс с согласием об использовании веб-сайта'):
            go_to_element(wait, action_chains, path_checkbox)
        with step('Сделать клик по чек-боксу'):
            action_chains.click().perform()
        with step('Навести курсор на кнопку "Оформить заказ"'):
            go_to_element(wait, action_chains, path_button_place_order)
        with step('Сделать клик по кнопке "Оформить заказ"'):
            action_chains.click().perform()

        with step('Проверить корректность введённых данных и суммы заказа на странице подтверждения заказа'):
            expected_address = wait_visible_element(wait, path_expected_address).text.split('\n')
            full_name = ' '.join([value_name, value_surname])
            input_data = [full_name, value_address, value_city, value_area, value_index, value_telephone, value_email]
            expected_date = wait_visible_element(wait, path_expected_date).text.replace('.', '')
            expected_amount_order = wait_visible_element(wait, path_expected_amount_order).text.replace(',00', '')
            expected_method_payment = wait_visible_element(wait, path_expected_method_payment).text

            assert expected_address == input_data
            assert expected_amount_order[:-1] == value_amount_order[2:-6]
            assert expected_method_payment == "Оплата при доставке"
            assert expected_date == value_date, "Дата в заказе не соответствует введённой"
            pass
