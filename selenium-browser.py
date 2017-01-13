from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome('/usr/local/chromedriver')
    driver.get("http://localhost:8000")
    
    assert driver.title == 'Directory listing for /'
    driver.close()


