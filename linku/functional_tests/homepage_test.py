import sys
import os
from selenium import webdriver
import pytest


@pytest.fixture(scope="module")
def browser():
    if sys.platform == 'darwin':
        project_root = os.path.dirname(os.path.dirname(
            os.path.realpath(__file__)))
        repo_root = os.path.dirname(project_root)
        sys.path.append(os.path.join(repo_root, 'dev'))
        import download_chromedriver
        download_chromedriver.download()
        chrome_path = download_chromedriver.get_chromedriver_path()
        if chrome_path is False:
            raise SystemExit
        driver = webdriver.Chrome(chrome_path)
    else:
        driver = webdriver.Firefox()
    yield driver
    driver.close()


def test_checking_prepared_environment_with_selenium(browser):
    browser.get("http://localhost:8000")
    assert '돈까스 모임' in browser.page_source


def test_2checking_prepared_environment_with_selenium(browser):
    browser.get("http://localhost:8000")
    assert '돈까스 모임' in browser.page_source
