import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestInteraction:
    def test_field_search(self, selenium):
        wait = WebDriverWait(selenium, timeout=10)

        selenium.get("https://github.com/microsoft/vscode/issues")
        field_search = wait.until(EC.visibility_of_element_located((By.ID, "repository-input")))
        field_search.click()
        text = "in:title bug"
        field_search.send_keys(text + Keys.ENTER)
        pass

    def test_drop_down(self, selenium):
        wait = WebDriverWait(selenium, timeout=10)

        selenium.get("https://github.com/microsoft/vscode/issues")
        check_button = wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "[data-testid='authors-anchor-button']")))
        check_button.click()
        field_filter_authors = selenium.find_element(
            By.XPATH, "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div/span/input")
        field_filter_authors.click()
        text = "bpasero"
        field_filter_authors.send_keys(text)
        choice_author = selenium.find_element(By.XPATH, "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div[2]")
        choice_author.click()
        pass

    def test_multiple_input_fields(self, selenium):
        wait = WebDriverWait(selenium, timeout=10)

        selenium.get("https://github.com/search/advanced")
        check_select = wait.until(EC.visibility_of_element_located((By.ID, "search_language")))
        action_chains = ActionChains(selenium)
        action_chains.click_and_hold(check_select)\
            .pause(1)\
            .perform()
        choice_language = selenium.find_element(By.XPATH, "//option[contains(text(), 'Python')]")
        choice_language.click()
        search_stars = selenium.find_element(By.ID, "search_stars")
        action_chains.send_keys_to_element(search_stars, ">20000")\
            .perform()
        field_filename = selenium.find_element(By.ID, "search_filename")
        action_chains.send_keys_to_element(field_filename, "environment.yml")\
            .perform()
        button_search = selenium.find_element(
            By.XPATH, "//div[@class='d-flex d-md-block']/child::button[contains(text(), 'Search')]")
        action_chains.click(button_search)\
            .perform()
        pass

    def test_slider_checkbox_radiobutton(self, selenium):
        wait = WebDriverWait(selenium, timeout=10)

        selenium.get("https://skillbox.ru/code/")
        selenium.maximize_window()
        radio_button = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//label/child::span[contains(text(), 'Профессия')]")))
        action_chains = ActionChains(selenium)
        action_chains.click(radio_button)\
            .perform()
        filter_left_slider = selenium.find_element(
            By.XPATH, "//div[@class='ui-range vue-slider vue-slider-ltr']/div/div[2]/button")
        action_chains.scroll_to_element(filter_left_slider)\
            .click_and_hold(filter_left_slider)\
            .move_by_offset(xoffset=50, yoffset=0)\
            .perform()
        action_chains.release()\
            .pause(3)\
            .perform()
        filter_right_slider = selenium.find_element(
            By.XPATH, '//div[@class="ui-range vue-slider vue-slider-ltr"]/div/div[3]/button')
        action_chains.click_and_hold(filter_right_slider)\
            .move_by_offset(xoffset=-50, yoffset=0)\
            .perform()
        action_chains.release()\
            .pause(3)\
            .perform()
        filter_checkboxes = selenium.find_element(
            By.XPATH, '//button[@class="ui-expand-button filter-checkboxes__button ui-expand-button--small"]')
        filter_checkboxes.click()
        topic = selenium.find_element(By.XPATH, '//span/child::span[contains(text(), "Python")]')
        topic.click()
        pass

    def test_chart(self, selenium):
        selenium.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        selenium.maximize_window()
        time.sleep(2)
        chart = selenium.find_element(By.XPATH, "//*[contains(@class, 'viz')]")
        action_chains = ActionChains(selenium)
        action_chains.move_to_element(chart)\
            .perform()
        elem_chart = selenium.find_element(By.XPATH, "//*[contains(@class, 'viz')]//*[contains(@class, 'bar')][28]")
        action_chains.move_to_element(elem_chart)\
            .perform()
        time.sleep(60)
        pass
