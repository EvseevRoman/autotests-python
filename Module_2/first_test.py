import allure

@allure.step("Проверка заголовка страницы")
def check_title(driver, title):
    assert title == driver.title

class TestExample:
   def test_example_1(self, set_up_browser):
       driver = set_up_browser
       driver.get("http://skillbox.ru")
       check_title(driver = driver, title = "Skillbox – образовательная платформа с онлайн-курсами.")

   def test_example_2(self, set_up_browser):
       driver = set_up_browser
       driver.get("http://skillbox.ru")
       check_title(driver = driver, title = "Skillbox – образовательная платформа  онлайн-курсами.")
