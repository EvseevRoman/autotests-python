import allure
from allure_commons._allure import step
from playwright.sync_api import Page
import logging


@allure.step('Проверка и удаление активного купона')
def making_order(page: Page, value_telephone):
    path_making_order = "(//a[contains(text(), 'Оформление заказа')])[1]"
    path_field_name = "//input[@name='billing_first_name']"
    path_field_surname = "//input[@name='billing_last_name']"
    path_field_address = "//input[@name='billing_address_1']"
    path_field_city = "//input[@name='billing_city']"
    path_field_area = "//input[@name='billing_state']"
    path_field_index = "//input[@name='billing_postcode']"
    path_field_telephone = "//input[@name='billing_phone']"
    path_calendar = "//input[@name='order_date']"
    path_textarea = "//textarea"
    path_radiobutton = "//input[@id='payment_method_cod']"
    path_checkbox = "//input[@type='checkbox']"
    path_button_place_order = "//button[@value='Оформить заказ']"
    value_date = "2025-06-06"
    value_name = "Вася"
    value_surname = "Пупкин"
    value_address = "ул. Взлётная, д. 9"
    value_city = "Москва"
    value_area = "Московская область"
    value_index = "101000"
    logging.info('Start mode making an order')
    with step('Перейти на страницу "Оформление заказа"'):
        page.locator(path_making_order).click()
    with step('Ввести в поле "Дата заказа", завтрашнюю дату'):
        page.locator(path_calendar).fill(value_date)
    with step(f'Ввести в поле "Комментарии к заказу": {value_telephone}'):
        page.locator(path_textarea).fill(value_telephone)
    with step('Ввести в поле имя валидное значение'):
        page.locator(path_field_name).clear()
        page.locator(path_field_name).fill(value_name)
    with step('Ввести валидное значение в поле "Фамилия"'):
        page.locator(path_field_surname).clear()
        page.locator(path_field_surname).fill(value_surname)
    with step('Ввести валидный адрес доставки'):
        page.locator(path_field_address).clear()
        page.locator(path_field_address).fill(value_address)
    with step('Ввести валидное название города'):
        page.locator(path_field_city).clear()
        page.locator(path_field_city).fill(value_city)
    with step('Ввести корректное название области'):
        page.locator(path_field_area).clear()
        page.locator(path_field_area).fill(value_area)
    with step('Ввести в поле "Почтовый индекс" валидный индекс'):
        page.locator(path_field_index).clear()
        page.locator(path_field_index).fill(value_index)
    with step('Ввести в поле "Телефон" валидный номер телефона'):
        page.locator(path_field_telephone).clear()
        page.locator(path_field_telephone).fill(value_telephone)
    with step('Сделать клик по кнопке "Оплата при доставке"'):
        page.locator(path_radiobutton).click()
    with step('Сделать клик по чек-боксу'):
        page.locator(path_checkbox).click()
    with step('Сделать клик по кнопке "Оформить заказ"'):
        page.locator(path_button_place_order).click()
    logging.info('Finish mode checking the active coupon')
