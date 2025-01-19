from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def run_script():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Включаем headless режим
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get("http://skillbox.ru")
    driver.quit()

if __name__ == '__main__':
    run_script()