from selenium import webdriver

def test_selenium():
    driver = webdriver.Firefox()
    driver.get("http://localhost:8000")
    
    assert driver.title == 'Directory listing for /'
    driver.close()


