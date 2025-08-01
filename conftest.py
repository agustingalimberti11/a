import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import selenium

@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar sin GUI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--start-maximized")

    # Detectar versión de Selenium
    selenium_version = tuple(int(x) for x in selenium.__version__.split('.') if x.isdigit())
    HAS_SERVICE = selenium_version[0] >= 4 and selenium_version[1] >= 6

    if HAS_SERVICE:
        # Selenium 4.6+ usa selenium-manager
        driver = webdriver.Chrome(options=chrome_options)
    else:
        # Selenium < 4.6 requiere ruta manual al chromedriver
        driver_path = os.environ.get("CHROMEDRIVER_PATH", r"C:\Users\PC\Downloads\alkemy\chromedriver.exe")
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()

