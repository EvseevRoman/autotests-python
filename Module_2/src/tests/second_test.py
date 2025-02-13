class TestExample:
   def test_example_5(self, set_up_browser):
       driver = set_up_browser
       driver.get("http://skillbox.ru")
       assert "Skillbox – образовательная платформа  онлайн-курсами." == driver.title

   def test_example_6(self, set_up_browser):
       driver = set_up_browser
       driver.get("http://skillbox.ru")
       assert "Skillbox – образовательная платформа  онлайн-курсами." == driver.title