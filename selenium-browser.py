from selenium import webdriver
from pyvirtualdisplay import Display

def test_selenium():
    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = webdriver.Firefox()
    driver.get("http://localhost:4444/wd/hub")
    
    # assert driver.title == 'Directory listing for /'
    
    driver.close()
    display.stop()


