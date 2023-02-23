import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default='chrome', help="choose browser")
    parser.addoption("--language", action="store", default='en', help="chrome by default, firefox is available")


@pytest.fixture(scope='function')
def driver(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        chrome_obj = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=chrome_obj, options=chrome_options)
    elif browser_name == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("intl.accept_languages", user_language)
        firefox_obj = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=firefox_obj, options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()