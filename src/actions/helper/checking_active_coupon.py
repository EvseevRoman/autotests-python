import allure
from allure_commons._allure import step
from playwright.sync_api import Page, expect
import logging


@allure.step('Проверка и удаление активного купона')
def checking_active_coupon(page: Page):
    path_making_order = "(//a[contains(text(), 'Оформление заказа')])[1]"
    path_order_total = "//tr[@class='order-total']//bdi"
    path_delete_coupon = "//a[@class='woocommerce-remove-coupon']"
    logging.info('Start mode checking the active coupon')
    with step('Перейти на страницу "Оформление заказа"'):
        page.locator(path_making_order).click()
    with step('Сделать скролл к сумме заказа"'):
        expect(page.locator(path_order_total)).to_be_visible()
        page.locator(path_order_total).scroll_into_view_if_needed()
    with step('Проверка и удаление активного купона'):
        if page.locator(path_delete_coupon).is_visible():
            page.locator(path_delete_coupon).click()
            expect(page.locator(path_delete_coupon)).to_be_hidden(timeout=1000)
    logging.info('Finish mode checking the active coupon')
