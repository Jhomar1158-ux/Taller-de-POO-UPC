import time
import pyautogui
from dataclasses import dataclass
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

website='https://carnetvacunacion.minsa.gob.pe/#/verify-qr/enable'

options = Options()
#options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(website)
driver.maximize_window()
# ========= PYAUTOGUI ACTION ===========
# obs.: Tener en cuenta las dimensiones de su pantalla (1366,768)
time.sleep(4)
pyautogui.click(292, 179) 
time.sleep(2)
pyautogui.click(984, 405)
time.sleep(2)
pyautogui.click(984, 321) 

print("---MUESTRE EL QR DE SU CARNET DE VACUNACIÓN---")
time.sleep(10)
nombre=driver.find_element(by='xpath',value="/html/body/app-root/app-verify-qr/div/div/app-result/div/div/div[2]/div/div/div[1]/div[1]/div[3]/span")
# print("--")
# print(type(nombre.text))
print(nombre.text)
dosis=driver.find_element(by='xpath',value="/html/body/app-root/app-verify-qr/div/div/app-result/div/div/div[2]/div/div/div[1]/div[1]/div[5]/h3[2]")
# print(type(dosis.text))
print(dosis.text)
edad=driver.find_element(by='xpath', value="/html/body/app-root/app-verify-qr/div/div/app-result/div/div/div[2]/div/div/div[1]/div[1]/div[4]/span[2]")
lista_edad=edad.text.split(' ')
probar_edad=int(lista_edad[1])

print(int(probar_edad))
    
data=[nombre.text,dosis.text,probar_edad]