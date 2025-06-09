import allure
from allure_commons._allure import step
from playwright.sync_api import Page, expect
from src.actions.callback.go_to_url import go_to_url
from src.actions.helper.filling_shopping_cart_goods import filling_shopping_cart_goods
from src.actions.helper.login import login_user
from src.actions.helper.making_order import making_order


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature('Тестирование функционала сайта Pizzeria')
@allure.story('Флоу с бонусной системой на фреймворке playwright')
class TestFlowBonusSystem:

    @allure.title('Проверка успешной работы бонусной системы')
    def test_flow_bonus_system(self, go_to_url, page: Page):
        """
        Сценарий №5
        1. Перейдите на страницу бонусной программы.
        2. Введите нужные данные.
        3. Дождитесь активации данных.
        4. Убедитесь, что она прошла успешно.
        5. Проверить валидацию полей при заполнении формы.


        Шаги:
            1. Перейти на вкладку "Бонусная программа"
            2. Ввести в поле "Имя" валидное значение
            3. Ввести в поле "Телефон" валидный номер
            4. Нажать кнопку "Оформить карту"
            5. Нажать кнопку "Закрыть" в появившемся pop-up
            6. Перейти на главную страницу
            7. Добавить товар в корзину
            8. Перейти на страницу "Оформить заказ"
            9. В поле "Комментарии к заказу" ввести номер телефона указанный при оформлении бонусной карты
            10. Заполнить валидными значениями все обязательные поля формы "Детали заказа"
            11. Нажать кнопку "Оформить заказ"
            12. Проверить применение скидки в 15%

        Предусловие: пользователь зарегистрирован и авторизован на сайте https://pizzeria.skillbox.cc/

        Тестовые данные:
             Username = zlo
             Password = qwe123!@#
        """
        path_order_subtotal = "//th[contains(text(), 'Subtotal')]/following-sibling::td/span"
        path_order_total = "//th[contains(text(), 'Total')]/following-sibling::td/span"
        path_note = "//th[contains(text(), 'Note')]/following-sibling::td"
        path_page_bonus_system = "(//a[contains(text(), 'Бонусная программа')])[1]"
        path_field_username = "//input[@name='username']"
        path_field_telephone = "//input[@name='billing_phone']"
        path_button_bonus = "//button[@name='bonus']"
        path_message_success = "//h3[contains(text(), 'Ваша карта оформлена')]"
        username = "po14"
        password = "qwe123!@#"
        bonus_telephone = "89005000800"

        go_to_url("https://pizzeria.skillbox.cc/")
        login_user(page, username, password)
        with step('Перейти на вкладку "Бонусная программа"'):
            page.locator(path_page_bonus_system).click()
        with step('Ввести в поле "Имя" валидное значение'):
            page.locator(path_field_username).clear()
            page.locator(path_field_username).fill(username)
        with step('Ввести в поле "Телефон" валидный номер'):
            page.locator(path_field_telephone).clear()
            page.locator(path_field_telephone).fill(bonus_telephone)
        with step('Нажать кнопку "Оформить карту"'):
            page.on("dialog", lambda dialog: dialog.accept())
            page.locator(path_button_bonus).click()
            expect(page.locator(path_message_success)).to_be_visible(timeout=15000)
        page.wait_for_timeout(1000)
        filling_shopping_cart_goods(page)
        page.wait_for_timeout(1000)
        making_order(page, bonus_telephone)

        with step(f'Проверить, что к телефону: {bonus_telephone}, применилась скидка 15%'):
            page.wait_for_timeout(1000)
            page.locator(path_order_total).scroll_into_view_if_needed()
            note = page.locator(path_note).inner_text()
            order_subtotal = float(page.locator(path_order_subtotal).inner_text()[:-1].replace(',', '.'))
            order_total = float(page.locator(path_order_total).inner_text()[:-1].replace(',', '.'))
            assert note == bonus_telephone
            assert order_subtotal * 0.85 == order_total
