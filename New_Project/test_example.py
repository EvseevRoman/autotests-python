from selenium.webdriver import Chrome
<<<<<<< HEAD
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
=======
>>>>>>> 1a4b0ab80a3ace91abc11851569b44b4617ffd93

class TestExample:
   def test_example(self):
       driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
       driver.get("http://skillbox.ru")
<<<<<<< HEAD
       assert "Skillbox – образовательная платформа с онлайн-курсами." == driver.title
=======
       assert "Sillbox" == driver.title
>>>>>>> 1a4b0ab80a3ace91abc11851569b44b4617ffd93
       driver.quit()