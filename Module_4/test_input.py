import time

import selenium.webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class TestInteraction:
    def test_case_1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/issues")
        field_search = driver.find_element(By.ID, "repository-input")
        field_search.click()
        text = "in:title bug"
        field_search.send_keys(text + Keys.ENTER)
        pass

    def test_case_2(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/issues")
        check_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='authors-anchor-button']")
        check_button.click()
        field_filter_authors = driver.find_element(By.XPATH, "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div/span/input")
        field_filter_authors.click()
        text = "bpasero"
        field_filter_authors.send_keys(text)
        choice_author = driver.find_element(By.XPATH, "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div[2]")
        choice_author.click()
        pass

    def test_case_3(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/search/advanced")
        check_select = driver.find_element(By.ID, "search_language")
        action_chains = selenium.webdriver.ActionChains(driver)
        action_chains.click_and_hold(check_select)\
            .pause(1)\
            .perform()
        choice_language = driver.find_element(By.XPATH, "//option[contains(text(), 'Python')]")
        choice_language.click()
        search_stars = driver.find_element(By.ID, "search_stars")
        action_chains.send_keys_to_element(search_stars, ">20000")\
            .perform()
        field_filename = driver.find_element(By.ID, "search_filename")
        action_chains.send_keys_to_element(field_filename, "environment.yml")\
            .perform()
        button_search = driver.find_element(By.XPATH, "//div[@class='d-flex d-md-block']/child::button[contains(text(), 'Search')]")
        action_chains.click(button_search)\
            .perform()
        pass

    def test_case_4(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru/code/")
        driver.maximize_window()
        radio_button = driver.find_element(By.XPATH, "//label/child::span[contains(text(), 'Профессия')]")
        action_chains = selenium.webdriver.ActionChains(driver)
        action_chains.click(radio_button)\
            .perform()
        filter_left_slider = driver.find_element(By.XPATH, "//div[@class='ui-range vue-slider vue-slider-ltr']/div/div[2]/button")
        action_chains.scroll_to_element(filter_left_slider)\
            .click_and_hold(filter_left_slider)\
            .move_by_offset(xoffset=50, yoffset=0)\
            .perform()
        action_chains.release()\
            .pause(3)\
            .perform()
        filter_right_slider = driver.find_element(By.XPATH, '//div[@class="ui-range vue-slider vue-slider-ltr"]/div/div[3]/button')
        action_chains.click_and_hold(filter_right_slider)\
            .move_by_offset(xoffset=-50, yoffset=0)\
            .perform()
        action_chains.release()\
            .pause(3)\
            .perform()
        filter_checkboxes = driver.find_element(By.XPATH, '//button[@class="ui-expand-button filter-checkboxes__button ui-expand-button--small"]')
        filter_checkboxes.click()
        topic = driver.find_element(By.XPATH, '//span/child::span[contains(text(), "Python")]')
        topic.click()
        pass

    def test_case_5(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        driver.maximize_window()
        time.sleep(2)
        chart = driver.find_element(By.XPATH, "//*[contains(@class, 'viz')]")
        action_chains = selenium.webdriver.ActionChains(driver)
        action_chains.move_to_element(chart)\
            .perform()
        elem_chart = driver.find_element(By.XPATH, "//*[contains(@class, 'viz')]//*[contains(@class, 'bar')][28]")
        action_chains.move_to_element(elem_chart)\
            .perform()
        time.sleep(60)
        pass