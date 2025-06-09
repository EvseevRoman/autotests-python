from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from src.actions.checks.check_elements import check_elements_search
from src.actions.waits.wait_element_in_dom_tree import wait_element_in_dom_tree
from src.actions.waits.wait_visible_element import wait_visible_element


class TestValidation:

    def test_validation_search(self, selenium):
        wait = WebDriverWait(selenium, timeout=10)
        head = "in:title "
        search_text = "bug"
        element_search = 1
        cnt_elements = 25
        path = f'(//h3/a/span)[{element_search}]'

        selenium.get("https://github.com/microsoft/vscode/issues")
        field_search = wait_visible_element(wait, "//input[@id='repository-input']")
        field_search.click()
        field_search.send_keys(head + Keys.ENTER)
        field_search = wait_visible_element(wait, "//input[@id='repository-input']")
        field_search.click()
        field_search.send_keys(search_text + Keys.ENTER)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h3/a/span"), "bug"))

        check_elements_search(wait, path, cnt_elements, search_text)

    def test_validation_search_drop_down(self, selenium):
        wait = WebDriverWait(selenium, timeout=10)
        search_text = "bpasero"
        element_search = 1
        cnt_elements = 25
        path = f'(//a[contains(text(), "bpasero")])[{element_search}]'

        selenium.get("https://github.com/microsoft/vscode/issues")
        check_button = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "[data-testid='authors-anchor-button']")))
        check_button.click()
        field_filter_authors = selenium.find_element(
            By.XPATH, "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div/span/input")
        field_filter_authors.click()
        field_filter_authors.send_keys(search_text)
        choice_author = selenium.find_element(By.XPATH, "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div[2]")
        choice_author.click()
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//a[contains(text(), "bpasero")]')))

        check_elements_search(wait, path, cnt_elements, search_text)

    def test_validation_search_multiple_input_fields(self, selenium):
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)

        selenium.get("https://github.com/search/advanced")
        check_select = wait.until(EC.visibility_of_element_located((By.ID, "search_language")))
        action_chains.click_and_hold(check_select) \
            .perform()
        choice_language = selenium.find_element(By.XPATH, "//option[contains(text(), 'Python')]")
        choice_language.click()
        search_stars = selenium.find_element(By.ID, "search_stars")
        action_chains.send_keys_to_element(search_stars, ">20000") \
            .perform()
        field_filename = selenium.find_element(By.ID, "search_filename")
        action_chains.send_keys_to_element(field_filename, "environment.yml") \
            .perform()
        button_search = selenium.find_element(
            By.XPATH, "//div[@class='d-flex d-md-block']/child::button[contains(text(), 'Search')]")
        action_chains.click(button_search) \
            .perform()

        for i in range(1, 11):
            path = f"(//*[contains(@class, 'Box-sc-g0xbh4-0 iPuHRc prc-Link-Link-85e08')]/span)[{i}]"
            stars = wait_element_in_dom_tree(wait, path).text
            assert int(stars[:-1]) > 20

    def test_validation_slider_checkbox_radiobutton(self, selenium):
        wait = WebDriverWait(selenium, timeout=15)
        action_chains = ActionChains(selenium)

        selenium.get("https://skillbox.ru/code/")
        radio_button = wait_element_in_dom_tree(wait, "//label/child::span[contains(text(), 'Профессия')]")
        action_chains.click(radio_button) \
            .perform()
        filter_left_slider = selenium.find_element(
            By.XPATH, "//div[@class='ui-range vue-slider vue-slider-ltr']/div/div[2]/button")
        action_chains.scroll_to_element(filter_left_slider) \
            .click_and_hold(filter_left_slider) \
            .move_by_offset(xoffset=50, yoffset=0) \
            .perform()
        action_chains.release() \
            .pause(3) \
            .perform()
        filter_right_slider = selenium.find_element(
            By.XPATH, '//div[@class="ui-range vue-slider vue-slider-ltr"]/div/div[3]/button')
        action_chains.click_and_hold(filter_right_slider) \
            .move_by_offset(xoffset=-50, yoffset=0) \
            .perform()
        action_chains.release() \
            .pause(3) \
            .perform()
        filter_checkboxes = selenium.find_element(
            By.XPATH, '//button[@class="ui-expand-button filter-checkboxes__button ui-expand-button--small"]')
        filter_checkboxes.click()
        topic = selenium.find_element(By.XPATH, '//span/child::span[contains(text(), "Python")]')
        topic.click()

        for i in range(1, 9):
            path_type = f'(//div/span[@class ="ui-product-card-main__label f f--12"])[{i}]'
            type_training = selenium.find_element(By.XPATH, path_type).text
            path_duration = f'(//b[@class="card__count f f--12 f--m"])[{i}]'
            duration = int(selenium.find_element(By.XPATH, path_duration).text)
            assert type_training == "Профессия" and 6 <= duration <= 12

    def test_validation_chart(self, selenium):
        wait = WebDriverWait(selenium, timeout=30)
        action_chains = ActionChains(selenium)

        selenium.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        selenium.maximize_window()
        elem_chart = wait_element_in_dom_tree(wait, "//*[contains(@class, 'viz')]//*[contains(@class, 'bar')][27]")
        action_chains.move_to_element(elem_chart) \
            .perform()
        text_elem_tooltip = wait_element_in_dom_tree(wait, "//div[@class='svg-tip n']")
        text_tooltip = text_elem_tooltip.get_attribute('innerHTML')

        assert text_tooltip == '<strong>138</strong> commits the week of Oct 6'
