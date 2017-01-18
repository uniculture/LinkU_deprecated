from selenium import webdriver


def test_checking_prepared_environment_with_selenium():
    driver = webdriver.Firefox()
    driver.get("http://localhost:8000")
    assert driver.title == 'Welcome to Django'
    driver.close()
