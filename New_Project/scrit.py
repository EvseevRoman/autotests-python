from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def run_script():
#    options.headless = True
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://skillbox.ru")
    assert "Sillbox" == driver.title
    driver.quit()

if __name__ == '__main__':
    run_script()