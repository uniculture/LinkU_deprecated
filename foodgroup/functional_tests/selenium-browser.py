import sys
import os
from selenium import webdriver


def test_checking_prepared_environment_with_selenium():
    if sys.platform == 'darwin':
        project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
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
    driver.get("http://localhost:8000")
    assert driver.title == 'Welcome to Django'
    driver.close()
