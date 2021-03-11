import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    #параметр для выбора браузера оставлю, вдруг пригодится
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    #а это параметр для выбора языка. Дефолтный будет инглиш                 
    parser.addoption('--language', action='store', default='en',
                     help="Choose page language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language") #запрос параметра языка
    browser = None
    print('\n\nOpen browser...\n\n')
    if browser_name == "chrome":
        #вывод в консоль языка, с которым тест будет идти
        print(f"\n\nstart chrome browser for test with {user_language} language\n\n")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        #вывод в консоль языка, с которым тест будет идти
        print(f"\n\nstart firefox browser for test {user_language} language\n\n")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\n\nquit browser..\n\n")
    browser.quit()