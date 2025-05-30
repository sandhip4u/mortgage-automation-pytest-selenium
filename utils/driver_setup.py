
from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    return driver
