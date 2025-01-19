from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

class TestExample:
   def test_example(self):
       chrome_options = Options()
       chrome_options.add_argument("--headless")  # Включаем headless режим
       driver = Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
       driver.get("http://skillbox.ru")
       assert "Skillbox – образовательная платформа с онлайн-курсами." == driver.title
       driver.quit()