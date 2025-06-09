import allure
from allure_commons._allure import step
from playwright.sync_api import Page, expect
import logging


@allure.step('Ввод купона')
def input_coupon(page: Page, coupon):
    path_making_order = "(//a[contains(text(), 'Оформление заказа')])[1]"
    path_link_show_coupon = "//a[@class='showcoupon']"
    path_field_coupon = "//input[@id='coupon_code']"
    path_button_appply_coupon = "//button[@name='apply_coupon']"
    path_info_message_success = "//tr[@class='cart-subtotal']//bdi"
    path_info_message_error = "//ul[@role='alert']"
    logging.info('Start mode for input coupon')
    with step('Перейти на страницу "Оформление заказа"'):
        expect(page.locator(path_making_order)).to_be_visible()
        page.locator(path_making_order).click()
        page.wait_for_timeout(1000)
    with step('Сделать клик по ссылке "Нажмите для ввода купона"'):
        page.locator(path_link_show_coupon).click()
        page.wait_for_timeout(1000)
    with step('Ввести в поле для купона'):
        page.locator(path_field_coupon).type(coupon)
    with step('Нажать на кнопку "Применить купон"'):
        page.locator(path_button_appply_coupon).wait_for(state="visible")
        page.locator(path_button_appply_coupon).click()
        if coupon == "GIVEMEHALYAVA":
            expect(page.locator(path_info_message_success)).to_be_visible(timeout=1000)
        else:
            expect(page.locator(path_info_message_error)).to_be_visible(timeout=1000)
    logging.info('Finish mode for input coupon')
