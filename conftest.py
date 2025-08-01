import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Detectar versión de Selenium
selenium_version = tuple(int(x) for x in selenium.__version__.split('.') if x.isdigit())
HAS_SERVICE = selenium_version[0] >= 4

if HAS_SERVICE:
    from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")  # Si querés modo headless

    driver_path = r"C:\Users\PC\Downloads\alkemy\chromedriver.exe"

    if HAS_SERVICE:
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    yield driver
    driver.quit()
