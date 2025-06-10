import allure
from playwright.sync_api import Page
from src.actions.callback.go_to_url import go_to_url
from src.actions.checks.check_elements import check_results_search
from src.actions.checks.check_elements import check_count_stars
from src.actions.checks.check_elements import check_count_months


@allure.testcase("Практическая работа по модулю 7")
@allure.feature("Научиться писать тесты с использованием нового инструмента Playwright")
@allure.story("Валидация состояний элементов с помощью Playwright")
class TestValidation:

    @allure.title(
        "Проверка фильтрации страницы issues на сайте github по ключевым словам в заголовке"
    )
    def test_validation_search(self, go_to_url, page: Page):
        head = "in:title"
        search_text = "BUG"
        path = "//h3/span/a"

        go_to_url("https://github.com/microsoft/vscode/issues")
        with allure.step("Сделать клик по полю поиска"):
            page.locator("//input[@id='repository-input']").click(button="left")
        with allure.step(f"Ввести в поле поиска, сортировку по {head}"):
            page.locator("//input[@id='repository-input']").type(head)
            page.keyboard.press("Space")
        with allure.step(
            f"Ввести в поле поиска, сортировку по ключевому слову {search_text}"
        ):
            page.locator("//input[@id='repository-input']").type(search_text)
        with allure.step("Сделать клик по кнопке поиска"):
            page.locator("//div[@id='repository']/div/div/button").click()
            page.wait_for_timeout(timeout=1000)
        with allure.step(
            f"Выполнение проверки на наличие ключевого слова {search_text} в заголовках"
        ):
            check_results_search(page, path, search_text)

    @allure.title(
        "Проверка фильтрации страницы issues на сайте github по выбранному значению из выпадающего списка"
    )
    def test_validation_search_drop_down(self, go_to_url, page: Page):
        search_text = "bpasero"
        path = '//a[contains(text(), "bpasero")]'

        go_to_url("https://github.com/microsoft/vscode/issues")
        with allure.step("Сделать клик по кнопке Author на странице"):
            page.locator("[data-testid='authors-anchor-button']").click()
        with allure.step("Сделать клик по полю поиска в выпадающем списке"):
            page.locator(
                "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div/span/input"
            ).click()
        with allure.step('Ввести текст "bpasero" в поле поиска'):
            page.locator(
                "//div[@id='__primerPortalRoot__']/div/div/div/div[2]/div/span/input"
            ).type(search_text)
        with allure.step(
            "Найти искомого автора в обновлённом выпадающем списке и сделать по нему клик"
        ):
            page.get_by_text(search_text).first.click()
        with allure.step(
            f"Выполнение проверки на наличие ключевого слова {search_text} в заголовках"
        ):
            check_results_search(page, path, search_text)

    @allure.title(
        'Валидация страницы "Расширенного поиска" на сайте gitgub по нескольким параметрам'
    )
    def test_validation_search_multiple_input_fields(self, go_to_url, page: Page):
        language = "Python"
        count_stars = ">20000"
        name_file = "environment.yml"
        path_language = '//span[@aria-label="Python language"]'
        path_count_stars = '//div[@class="Box-sc-g0xbh4-0 gPrlij"]/ul/li[2]/a/span'

        go_to_url("https://github.com/search/advanced")
        with allure.step(
            f"Выбрать язык {language} в поле языка, на котором написан код"
        ):
            page.locator("//select[@id='search_language']").select_option(language)
        with allure.step(f"Ввести в поле количество звёзд у репозитория {count_stars}"):
            page.locator('//input[@data-search-prefix="stars:"]').type(count_stars)
        with allure.step(f"Ввести в поле с названием файла текст {name_file}"):
            page.locator('//input[@id="search_filename"]').type(name_file)
        with allure.step('Найти кнопку "Поиск"'):
            page.locator('(//button[contains(text(), "Search")])[2]').click()

        with allure.step(
            f"Выполнить проверку того, что найденные результаты написаны на языке {language}"
        ):
            check_results_search(page, path_language, language)
        with allure.step(
            f"Выполнить проверку того, что найденные результаты c количеством звёзд {count_stars}"
        ):
            check_count_stars(page, path_count_stars, count_stars)

    @allure.title(
        "Валидация фильтра курсов при помощи радиокнопки, слайдера и чекбокса сайта SkillBox"
    )
    def test_validation_slider_checkbox_radiobutton(self, go_to_url, page: Page):
        type_training = "Профессия"
        topic = "Python"
        path_type_training = '//div/span[@class ="ui-product-card-main__label f f--12"]'
        path_count_month = '//b[@class="card__count f f--12 f--m"]'

        go_to_url("https://skillbox.ru/code/")
        with allure.step(
            f"Выберать радиобаттон с названием {type_training} в разделе «Тип обучения на платформе»"
            " в DOM-дереве страницы"
        ):
            page.locator(
                f"//label/child::span[contains(text(), '{type_training}')]"
            ).click()
        with allure.step("Указать в поле «Длительность» диапазон от 6 месяцев"):
            left_slider = page.locator("(//button[@aria-label='Изменить диапозон'])[1]")
            x_coord_left = left_slider.bounding_box()
            left_slider.hover()
            page.mouse.down()
            page.mouse.move(x_coord_left["x"] + 70, x_coord_left["y"])
            page.mouse.up()
        with allure.step("Указать в поле «Длительность» диапазон до 12 месяцев"):
            right_slider = page.locator(
                "(//button[@aria-label='Изменить диапозон'])[2]"
            )
            x_coord_right = right_slider.bounding_box()
            right_slider.hover()
            page.mouse.down()
            page.mouse.move(x_coord_right["x"] - 50, x_coord_right["y"])
            page.mouse.up()
        with allure.step("Найти кнопку раскрывающегося списка Тематик"):
            page.locator(
                '//button[@class="ui-expand-button filter-checkboxes__button ui-expand-button--small"]'
            ).click()
        with allure.step(f"Выбрать в Тематике чекбокс {topic}"):
            page.locator(f"//span/child::span[contains(text(), '{topic}')]").click()

        with allure.step(
            "Выполнить проверку того, что карточки курсов содержат выбранные параметры фильтров"
        ):
            check_results_search(page, path_type_training, type_training)
            check_count_months(page, path_count_month)

    @allure.title(
        "Валидация отображаемого тултипа графика сайтf github на ожидаемые значения"
    )
    def test_validation_chart(self, go_to_url, page: Page):
        go_to_url("https://github.com/microsoft/vscode/graphs/commit-activity")
        with allure.step("Переместить курсор мыши на искомый элемент графика"):
            page.wait_for_selector(
                "//*[contains(@class, 'viz')]//*[contains(@class, 'bar')][27]"
            ).hover()

        with allure.step(
            'Проверка тултипа на соответствии ожидаемому значению ("238 commits the week of Nov 3")'
        ):
            assert (
                page.locator("//div[@class='svg-tip n']").inner_text()
                == "238 commits the week of Nov 3"
            )
