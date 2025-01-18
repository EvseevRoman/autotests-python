from selenium.webdriver import Chrome

class TestExample:
   def test_example(self):
       driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
       driver.get("http://skillbox.ru")
       assert "Sillbox" == driver.title
       driver.quit()