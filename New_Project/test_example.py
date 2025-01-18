from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestExample:
   def test_example(self):
       driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
       driver.get("http://skillbox.ru")
       assert "Skillbox – образовательная платформа с онлайн-курсами." == driver.title
       driver.quit()