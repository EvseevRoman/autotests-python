import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from src.actions.checks.check_elements import check_elements_search
from src.actions.waits.wait_element_in_dom_tree import wait_element_in_dom_tree
from src.actions.waits.wait_visible_element import wait_visible_element


@allure.testcase("Практическая работа по модулю 6")
@allure.feature(
    "Финальная настройка тестового репозитория для полноценной работы над тестами"
)
@allure.story("Валидация состояния элементов с помощью Selenium")
class TestValidation:

    @allure.title(
        "Проверка фильтрации страницы issues на сайте github по ключевым словам в заголовке"
    )
    def test_validation_search(self, selenium):
        wait = WebDriverWait(selenium, timeout=10)
        head = "in:title "
        search_text = "bug"
        element_search = 1
        cnt_elements = 25
        path = f"(//h3/a/span)[{element_search}]"

        with allure.step("Открыть страницу https://github.com/microsoft/vscode/issues"):
            selenium.get("https://github.com/microsoft/vscode/issues")
        with allure.step(
            'Дождаться того, что элемент "Поле поиска" присутствует в DOM страницы и виден'
        ):
            field_search = wait_visible_element(wait, "//input[@id='repository-input']")
        with allure.step("Сделать клик по полю поиска"):
            field_search.click()
        with allure.step(
            'Ввести в поле поиска, сортировку по "in:title " и нажать ENTER'
        ):
            field_search.send_keys(head + Keys.ENTER)
        with allure.step(
            'Дождаться того, что элемент "Поля поиска" присутствует в DOM страницы и виден'
        ):
            field_search = wait_visible_element(wait, "//input[@id='repository-input']")
        with allure.step("Сделать клик по полю поиска"):
            field_search.click()
        with allure.step(
            'Ввести в поле поиска текст "bug", по которому будет проводиться сортировка и нажать ENTER'
        ):
            field_search.send_keys(search_text + Keys.ENTER)
        with allure.step('Дождаться наличия текста "Bug" в найденной задаче'):
            wait.until(
                EC.text_to_be_present_in_element((By.XPATH, "//h3/a/span"), "bug")
            )

        check_elements_search(wait, path, cnt_elements, search_text)

    @allure.title(
        "Проверка фильтрации страницы issues на сайте github по выбранному значению из выпадающего списка"
    )
    def test_validation_search_drop_down(self, selenium):
        wait = WebDriverWait(selenium, timeout=10)
        search_text = "bpasero"
        element_search = 1
        cnt_elements = 25
        path = f'(//a[contains(text(), "bpasero")])[{element_search}]'

        with allure.step("Открыть страницу https://github.com/microsoft/vscode/issues"):
            selenium.get("https://github.com/microsoft/vscode/issues")
        with allure.step("Дождаться видимости и доступности кнопки Author на странице"):
            check_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-testid='authors-anchor-button']")
                )
            )
        with allure.step("Сделать клик по кнопке Author"):
            check_button.click()
        with allure.step("Найти поле поиска в выпадающем списке"):
            field_filter_authors = selenium.find_element(
                By.XPATH,
                "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div/span/input",
            )
        with allure.step("Сделать клик по полю поиска"):
            field_filter_authors.click()
        with allure.step('Ввести текст "bpasero" в поле поиска'):
            field_filter_authors.send_keys(search_text)
        with allure.step("Найти искомого автора в обновлённом выпадающем списке"):
            choice_author = selenium.find_element(
                By.XPATH, "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div[2]"
            )
        with allure.step("Сделать клик по полю с искомым автором"):
            choice_author.click()
        with allure.step(
            "Дождаться того, что все элементы присутствуют в DOM страницы и видны"
        ):
            wait_visible_element(wait, '//a[contains(text(), "bpasero")]')

        with allure.step(
            'Выполнить проверку того, что автор каждой из задач на странице, "bpasero"'
        ):
            check_elements_search(wait, path, cnt_elements, search_text)

    @allure.title(
        'Валидация страницы "Расширенного поиска" на сайте github по нескольким параметрам'
    )
    def test_validation_search_multiple_input_fields(self, selenium):
        wait = WebDriverWait(selenium, timeout=10)
        action_chains = ActionChains(selenium)

        with allure.step("Открыть страницу https://github.com/search/advanced"):
            selenium.get("https://github.com/search/advanced")
        with allure.step(
            "Дождаться того, что элемент поля для выбора языка присутствуют в DOM страницы и виден"
        ):
            check_select = wait.until(
                EC.visibility_of_element_located((By.ID, "search_language"))
            )
        with allure.step("Сделать клик по полю выбора языка"):
            action_chains.click_and_hold(check_select).perform()
        with allure.step('Найти в выпадающем списке язык "Python"'):
            choice_language = selenium.find_element(
                By.XPATH, "//option[contains(text(), 'Python')]"
            )
        with allure.step('Сделать клик по полю "Python"'):
            choice_language.click()
        with allure.step("Найти поле с выбором количества звёзд"):
            search_stars = selenium.find_element(By.ID, "search_stars")
        with allure.step('Ввести в поле с выбором количества звёзд текст ">20000"'):
            action_chains.send_keys_to_element(search_stars, ">20000").perform()
        with allure.step("Найти поле с названием файла"):
            field_filename = selenium.find_element(By.ID, "search_filename")
        with allure.step('Ввести в поле с названием файла текст "environment.yml"'):
            action_chains.send_keys_to_element(
                field_filename, "environment.yml"
            ).perform()
        with allure.step('Найти кнопку "Поиск"'):
            button_search = selenium.find_element(
                By.XPATH,
                "//div[@class='d-flex d-md-block']/child::button[contains(text(), 'Search')]",
            )
        with allure.step('Сделать клик по кнопке "Поиск"'):
            action_chains.click(button_search).perform()

        with allure.step(
            "Выполнить проверку того, что найденные результаты поиска соответствуют заданным параметрам"
        ):
            for i in range(1, 11):
                path_language = f"(//*[contains( @class, 'Box-sc-g0xbh4-0 eCfCAC')]/div/following-sibling::span)[{i}]"
                path_stars = f"(//*[contains(@class, 'Box-sc-g0xbh4-0 iPuHRc prc-Link-Link-85e08')]/span)[{i}]"
                with allure.step(
                    "Дождаться элемента отображающего язык программирования в DOM-дереве страницы"
                ):
                    language = wait_element_in_dom_tree(wait, path_language).text
                with allure.step(
                    'Дождаться элемента отображающего количество звёзд в DOM-дереве страницы"'
                ):
                    stars = wait_element_in_dom_tree(wait, path_stars).text
                with allure.step(
                    f"Проверка того, что {i}-й репозиторий на языке Python и имеет более 20000 звёзд'"
                ):
                    assert int(stars[:-1]) > 20 and language == "Python"

    @allure.title(
        "Валидация фильтра курсов при помощи радиокнопки, слайдера и чекбокса сайта SkillBox"
    )
    def test_validation_slider_checkbox_radiobutton(self, selenium):
        wait = WebDriverWait(selenium, timeout=15)
        action_chains = ActionChains(selenium)

        with allure.step("Открыть страницу https://skillbox.ru/code/"):
            selenium.get("https://skillbox.ru/code/")
        with allure.step("Развернуть окно браузера на весь экран"):
            selenium.maximize_window()
        with allure.step(
            "Дождаться наличия элемента радиокнопки 'Профессия' раздела 'Тип обучения на платформе'"
            " в DOM-дереве страницы"
        ):
            radio_button = wait_element_in_dom_tree(
                wait, "//label/child::span[contains(text(), 'Профессия')]"
            )
        with allure.step('Сделать клик по радиокнопке Профессия"'):
            action_chains.click(radio_button).perform()
        with allure.step('Найти левый ползунок поля слайдера "Длительность"'):
            filter_left_slider = selenium.find_element(
                By.XPATH,
                "//div[@class='ui-range vue-slider vue-slider-ltr']/div/div[2]/button",
            )
        with allure.step(
            'Сделать скролл страницы до слайдера "Длительность",'
            "зажать левую кнопку мыши на левом ползунке "
            "и переместить ползунок вправо до значения 6 месяцев"
        ):
            action_chains.scroll_to_element(filter_left_slider).click_and_hold(
                filter_left_slider
            ).move_by_offset(xoffset=50, yoffset=0).perform()
        with allure.step("Отпустить левую кнопку мыши"):
            action_chains.release().pause(3).perform()
        with allure.step('Найти правый ползунок поля слайдера "Длительность"'):
            filter_right_slider = selenium.find_element(
                By.XPATH,
                '//div[@class="ui-range vue-slider vue-slider-ltr"]/div/div[3]/button',
            )
        with allure.step(
            "Зажать левую кнопку мыши на правом ползунке"
            "и переместить ползунок влево до значения 12 месяцев"
        ):
            action_chains.click_and_hold(filter_right_slider).move_by_offset(
                xoffset=-50, yoffset=0
            ).perform()
        with allure.step("Отпустить левую кнопку мыши"):
            action_chains.release().pause(3).perform()
        with allure.step("Найти кнопку раскрывающегося списка Тематик"):
            filter_checkboxes = selenium.find_element(
                By.XPATH,
                '//button[@class="ui-expand-button filter-checkboxes__button ui-expand-button--small"]',
            )
        with allure.step("Сделать клик по кнопке раскрывающегося списка Тематик"):
            filter_checkboxes.click()
        with allure.step('Найти чекбокс "Python"'):
            topic = selenium.find_element(
                By.XPATH, '//span/child::span[contains(text(), "Python")]'
            )
        with allure.step('Отметить чекбокс "Python"'):
            topic.click()

        with allure.step(
            "Выполнить проверку того, что карточки курсов содержат выбранные параметры фильтров"
        ):
            for i in range(1, 9):
                path_type = (
                    f'(//div/span[@class ="ui-product-card-main__label f f--12"])[{i}]'
                )
                type_training = selenium.find_element(By.XPATH, path_type).text
                path_duration = f'(//b[@class="card__count f f--12 f--m"])[{i}]'
                duration = int(selenium.find_element(By.XPATH, path_duration).text)
                with allure.step(
                    f"Проверка {i}-й карточки на тип обучения 'Профессия',"
                    "с длительностью обучения от 6 до 12 месяцев"
                ):
                    assert type_training == "Профессия" and 6 <= duration <= 12

    @allure.title(
        "Валидация отображаемого тултипа графика сайта github на ожидаемые значения"
    )
    def test_validation_chart(self, selenium):
        wait = WebDriverWait(selenium, timeout=30)
        action_chains = ActionChains(selenium)

        with allure.step(
            "Открыть страницу https://github.com/microsoft/vscode/graphs/commit-activity"
        ):
            selenium.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        with allure.step("Развернуть окно браузера на весь экран"):
            selenium.maximize_window()
        with allure.step(
            "Дождаться наличия искомого элемента графика в DOM-дереве страницы"
        ):
            elem_chart = wait_element_in_dom_tree(
                wait, "//*[contains(@class, 'viz')]//*[contains(@class, 'bar')][27]"
            )
        with allure.step("Переместить курсор мыши на искомый элемент графика"):
            action_chains.move_to_element(elem_chart).perform()
        with allure.step(
            "Дождаться наличия тултипа искомого элемента графика в DOM-дереве страницы"
        ):
            text_elem_tooltip = wait_element_in_dom_tree(
                wait, "//div[@class='svg-tip n']"
            )
        text_tooltip = text_elem_tooltip.get_attribute("innerHTML")

        with allure.step(
            'Проверка на соответствии тултипа ожидаемому значению ("138 commits the week of Oct 6")'
        ):
            assert text_tooltip == "<strong>138</strong> commits the week of Oct 6"
