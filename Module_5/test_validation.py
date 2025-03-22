import time
import selenium.webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestValidation:
    def test_case_1(self, set_up_browser):
        driver = set_up_browser
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://github.com/microsoft/vscode/issues")
        field_search = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='repository-input']")))
        field_search.click()
        text = "in:title bug"
        field_search.send_keys(text + Keys.ENTER)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h3/a/span"), "bug"))

        for i in range(1, 26):
            path = f'(//h3/a/span)[{i}]'
            title = wait.until(EC.presence_of_element_located((By.XPATH, path)))
            assert "bug" in title.text.lower()

    def test_case_2(self, set_up_browser):
        driver = set_up_browser
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://github.com/microsoft/vscode/issues")
        check_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='authors-anchor-button']")))
        check_button.click()
        field_filter_authors = driver.find_element(By.XPATH,
                                                   "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div/span/input")
        field_filter_authors.click()
        text = "bpasero"
        field_filter_authors.send_keys(text)
        choice_author = driver.find_element(By.XPATH, "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div[2]")
        choice_author.click()
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//a[contains(text(), "bpasero")]')))

        for i in range(1, 26):
            path = f'(//a[contains(text(), "bpasero")])[{i}]'
            title = wait.until(EC.presence_of_element_located((By.XPATH, path)))
            assert "bpasero" in title.text.lower()

    def test_case_3(self, set_up_browser):
        driver = set_up_browser
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://github.com/search/advanced")
        check_select = wait.until(EC.visibility_of_element_located((By.ID, "search_language")))
        action_chains = selenium.webdriver.ActionChains(driver)
        action_chains.click_and_hold(check_select) \
            .perform()
        choice_language = driver.find_element(By.XPATH, "//option[contains(text(), 'Python')]")
        choice_language.click()
        search_stars = driver.find_element(By.ID, "search_stars")
        action_chains.send_keys_to_element(search_stars, ">20000") \
            .perform()
        field_filename = driver.find_element(By.ID, "search_filename")
        action_chains.send_keys_to_element(field_filename, "environment.yml") \
            .perform()
        button_search = driver.find_element(By.XPATH,
                                            "//div[@class='d-flex d-md-block']/child::button[contains(text(), 'Search')]")
        action_chains.click(button_search) \
            .perform()

        for i in range(1, 11):
            path = f"(//*[contains(@class, 'Box-sc-g0xbh4-0 iPuHRc prc-Link-Link-85e08')]/span)[{i}]"
            stars = wait.until(EC.presence_of_element_located((By.XPATH, path))).text
            assert int(stars[:-1]) > 20

    def test_case_4(self, set_up_browser):
        driver = set_up_browser
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://skillbox.ru/code/")
        driver.maximize_window()
        radio_button = wait.until(EC.presence_of_element_located((By.XPATH, "//label/child::span[contains(text(), 'Профессия')]")))
        action_chains = selenium.webdriver.ActionChains(driver)
        action_chains.click(radio_button) \
            .perform()
        filter_left_slider = driver.find_element(By.XPATH,
                                                 "//div[@class='ui-range vue-slider vue-slider-ltr']/div/div[2]/button")
        action_chains.scroll_to_element(filter_left_slider) \
            .click_and_hold(filter_left_slider) \
            .move_by_offset(xoffset=50, yoffset=0) \
            .perform()
        action_chains.release() \
            .pause(3) \
            .perform()
        filter_right_slider = driver.find_element(By.XPATH,
                                                  '//div[@class="ui-range vue-slider vue-slider-ltr"]/div/div[3]/button')
        action_chains.click_and_hold(filter_right_slider) \
            .move_by_offset(xoffset=-50, yoffset=0) \
            .perform()
        action_chains.release() \
            .pause(3) \
            .perform()
        filter_checkboxes = driver.find_element(By.XPATH,
                                                '//button[@class="ui-expand-button filter-checkboxes__button ui-expand-button--small"]')
        filter_checkboxes.click()
        topic = driver.find_element(By.XPATH, '//span/child::span[contains(text(), "Python")]')
        topic.click()

        for i in range(1, 9):
            path_type = f'(//div/span[@class ="ui-product-card-main__label f f--12"])[{i}]'
            type_training = driver.find_element(By.XPATH, path_type).text
            path_duration = f'(//b[@class="card__count f f--12 f--m"])[{i}]'
            duration = int(driver.find_element(By.XPATH, path_duration).text)
            assert type_training == "Профессия" and 6 <= duration <= 12

    def test_case_5(self, set_up_browser):
        driver = set_up_browser
        wait = WebDriverWait(driver, timeout=30)

        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        driver.maximize_window()
        #time.sleep(2)
        #chart = driver.find_element(By.XPATH, "//*[contains(@class, 'viz')]")
        chart = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'viz')]")))
        action_chains = selenium.webdriver.ActionChains(driver)
        action_chains.move_to_element(chart) \
            .perform()
        elem_chart = driver.find_element(By.XPATH, "//*[contains(@class, 'viz')]//*[contains(@class, 'bar')][28]")
        action_chains.move_to_element(elem_chart) \
            .perform()
        time.sleep(2)
        #elem_tooltip = driver.find_element(By.XPATH, "//div[@class='svg-tip n']/strong")
        num_elem_tooltip = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='svg-tip n']/strong")))
        num_tooltip = num_elem_tooltip.text
        pass
        # #text_tooltip = driver.find_element(By.XPATH, "(By.XPATH, '//div[@class='svg-tip n']/strong')").text
        # text_elem_tooltip = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='svg-tip n']")))
        # text_tooltip = text_elem_tooltip.text
        #
        # assert num_tooltip == '274' and text_tooltip == ' commits the week of Sep 29'

        pass
