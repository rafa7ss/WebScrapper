#Cheers to Orem Nahum, creator of this script
#His website with the script -> https://blog.testproject.io/2018/02/20/chrome-headless-selenium-python-linux-servers/
#All the comments are made by me, Rafael Martins

#Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

#Variables
DOWNLOAD_URL = "YOUR_URL"
download_dir = "YOUR_DOWNLOAD_PATH"
driver_path = "YOUR_DRIVER_PATH"

#Ensures that the driver can handle downloads on headless mode
def enable_download(driver):
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    driver.execute("send_command", params)

#Add to the driver all the necessary chrome options
def setting_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    return chrome_options

#Checks every 1 second if the file exists inside of the download path
def isFileDownloaded():
    file_path = download_dir+"\\python_samples-master.zip"
    while not os.path.exists(file_path):
        time.sleep(1)
    if os.path.isfile(file_path):
        print("File Downloaded successfully..")

#Calls all the main functions and initializes the driver with the driver path and chrome options 
if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=driver_path,options=setting_chrome_options())
    enable_download(driver)
    driver.get(DOWNLOAD_URL)
    isFileDownloaded()