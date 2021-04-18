import time
import dados
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = 'drivers/chromedriver'
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
        exportar()

def exportar():
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'toa-panel-content')][contains(@class, 'edtree')]"))
        )
    finally:
        pai = driver.find_elements_by_class_name("edt-root")
        for filho in pai:
            if (filho.text).find("BHZ-INFRAREDES") != -1:
                index = pai.index(filho)
                pai = driver.find_elements_by_xpath("//div[contains(@class,'edt-root')]")[index]
                i = 0
                while (driver.find_elements_by_xpath("//div[contains(@class,'edt-root')][contains(., 'BHZ-INFRAREDES')]/div[contains(@class,'edt-item')]")[i]).text != "":
                    categoria = driver.find_elements_by_xpath("//div[contains(@class,'edt-root')][contains(., 'BHZ-INFRAREDES')]/div[contains(@class,'edt-item')]")[i]
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