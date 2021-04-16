import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_path = 'chromedriver'
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get("https://clarobrasil.etadirect.com/mobility/")

time.sleep(10)

i = 2448
AuthState = ""
while driver.page_source[i] != "'":
    AuthState += driver.page_source[i]
    i += 1

print(AuthState)
driver.quit()