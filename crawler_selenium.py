#Import of file that contains all the variables needed
import dados
#Imports
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#Variables
driver_path = 'drivers/chromedriver'
download_dir = "D:\\selenium"
options = Options()
#options.add_argument("--headless")
options.add_argument('--no-sandbox')
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--window-size=1400,800")
driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get(dados.url)


#Waits until element presence is located, fills the form with the credencials and submit the form
def login1():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
    finally:
        text = driver.find_element_by_xpath('//input[@id="username"]')
        text.send_keys(dados.usuario)
        text = driver.find_element_by_xpath('//input[@id="password"]')
        text.send_keys(dados.senha)
        button = driver.find_element_by_name('user_submitted_login_form')
        time.sleep(6)
        button.click()
        login2()

#Similar as the function above, but with diferent methods to find the elements on the DOM
def login2():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
    finally:
        text = driver.find_element_by_name('username')
        text.send_keys(dados.usuario)
        text = driver.find_element_by_name('password')
        text.send_keys(dados.senha)
        button = driver.find_element_by_class_name('campo-buttom')
        time.sleep(6)
        button.click()
        abrirConfig()

def abrirConfig():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='top-right']"))
        )
    finally:
        perfil = driver.find_element_by_xpath("//div[@class='top-right']//div[@class='user-menu']")
        perfil.click()
        time.sleep(2)
        config = driver.find_elements_by_class_name("item-caption")[0]
        config.click()
        
        configurar()

def configurar():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "form-item"))
        )
    finally:
        select = driver.find_elements_by_class_name("form-item")[6]
        select.click()
        time.sleep(1)
        select.send_keys(Keys.UP)
        time.sleep(0.5)
        select.send_keys(Keys.UP)
        time.sleep(0.5)
        select.send_keys(Keys.UP)
        time.sleep(1)
        select.send_keys(Keys.ENTER)
        time.sleep(0.4)
        button = driver.find_elements_by_class_name("submit")[5]
        time.sleep(1)
        button.click()
        time.sleep(1)

        exportar()

#Finds the parent element, lists all the childrem of the selected parent and clicks on them
#After all of this, the function closes the driver and the script
def exportar():
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'toa-panel-content')][contains(@class, 'edtree')]"))
        )
    finally:
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        driver.execute("send_command", params)
        pai = driver.find_elements_by_class_name("edt-root")
        for filho in pai:
            if (filho.text).find(("{0}-{1}").format(dados.area, dados.empresa)) != -1:
                index = pai.index(filho)
                pai = driver.find_elements_by_xpath("//div[contains(@class,'edt-root')]")[index]
                i = 0
                while (driver.find_elements_by_xpath(("//div[contains(@class,'edt-root')][contains(., '{0}-{1}')]/div[contains(@class,'edt-item')]").format(dados.area, dados.empresa))[i]).text != "":
                    categoria = driver.find_elements_by_xpath(("//div[contains(@class,'edt-root')][contains(., '{0}-{1}')]/div[contains(@class,'edt-item')]").format(dados.area, dados.empresa))[i]
                    categoria.click()
                    time.sleep(1)
                    acao = driver.find_element_by_name("-82130")
                    acao.click()
                    try:
                        element = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.NAME, "export_queue"))
                        )
                    finally:
                        export = driver.find_element_by_name("export_queue")
                        export.click()
                        i += 1
                    time.sleep(1)
                break
        driver.quit()
        raise SystemExit

login1()

#Note: Some variables may have been named in Brazilian portuguese,
#so var filho = child and var pai = parent and so on 😁
