import sys
import os
from selenium import webdriver
import pytest


@pytest.fixture(scope="module")
def browser():
    print("loading browser")
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
    return driver


def test_first_page_card_title(browser):
    # 평소 여자들에 환장하는 짱구는 요새 외로워서 누구 하나 낚아보고자 우리 서비스에 접속했다.
    # 서비스에 접속하니 첫 화면에는 규카츠 먹을래?라는 글이 보였다.

    browser.get("http://localhost:8000")
    assert '규카츠 먹을래?' in browser.page_source
