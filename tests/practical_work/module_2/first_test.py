import allure


@allure.step("Проверка заголовка страницы")
def check_title(driver, title):
    assert title == driver.title


class TestExample:
    def test_example_1(self, selenium):
        selenium.get("https://lipetsk.hh.ru/")
        check_title(driver=selenium, title="Работа в Липецке, поиск персонала и публикация вакансий - lipetsk.hh.ru")

    def test_example_2(self, selenium):
        selenium.get("http://skillbox.ru")
        check_title(driver=selenium, title="Skillbox – образовательная платформа  онлайн-курсами.")
