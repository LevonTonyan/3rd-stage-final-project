import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--page_language', action='store', default=None,
                     help="Choose language: en, ru, fr or es")



options = Options()


@pytest.fixture(scope="function")
def browser(request):
    page_language = request.config.getoption("page_language")
    browser = None
    if page_language == "es":
        options.add_experimental_option('prefs', {'intl.accept_languages': page_language})
        browser = webdriver.Chrome(options=options)
    elif page_language == "ru":
        options.add_experimental_option('prefs', {'intl.accept_languages': page_language})
        browser = webdriver.Chrome(options=options)
    elif page_language == "fr":
        options.add_experimental_option('prefs', {'intl.accept_languages': page_language})
        browser = webdriver.Chrome(options=options)
    elif page_language == "en":
        options.add_experimental_option('prefs', {'intl.accept_languages': page_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--page language should be en, fr, ru or es")
    yield browser
    print("\nquit browser..")
    browser.quit()