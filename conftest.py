import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Language")

    
@pytest.fixture()
def browser(request):
    browser_language = request.config.getoption("language")
    options = Options()
    
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)
    
    yield browser
    time.sleep(1)
    browser.quit()