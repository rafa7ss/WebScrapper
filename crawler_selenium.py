import time
import dados
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = 'chromedriver'
options = Options()
options.headless = False
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--window-size=1400,800")
driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get(dados.url)

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
        listarCategorias()

def listarCategorias():
    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "toa-panel-content edtree"))
        )
    finally:
        div = driver.find_elements_by_class_name("edt-root")
        for divs in div:
            if (divs.text).find("BHZ-INFRAREDES") and divs.text != "":
                index = div.index(divs)
                div = driver.find_elements_by_class_name("edt-root")[div.index(divs)]
                exportar(index, div)
                break
        driver.quit()
        raise SystemExit
        '''exportar()'''

def exportar():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "toa-twopanel-first-panel ui-droppable"))
        )
    finally:
        button = driver.find_element_by_class_name('toa-button toa-view-control-button-menu')
        button.click()
        time.sleep(1)
        button = driver.find_element_by_name('export_queue')
        button.click()
        time.sleep(1)

login1()