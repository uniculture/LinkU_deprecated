from selenium import webdriver
#from pyvirtualdisplay import Display

def test_selenium():

    #driver = webdriver.Chrome('/usr/local/chromedriver')
    driver = webdriver.Firefox()

    driver.get("http://localhost:8000")
    
    assert driver.title == 'Directory listing for /'
    
    driver.close()
    #display.stop()

