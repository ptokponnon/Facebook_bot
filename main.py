import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pyautogui

publicacion = input("¿Que publicacion?: ")
grupo = input("¿A que grupo?: ")
comentario = input("Que comentario: ")
mensaje = input("¿Que mensaje?: ")
#op = webdriver.ChromeOptions()
#op.add_argument('--headless')
#op.add_argument('--disable-dev-shm-usage')
#op.add_argument('--no-sandbox')

def session(cuenta, contraseña):
    browser.get('https://m.facebook.com/login/?next&ref=dbl&fl&refid=8')
    with open ('cuentas.csv', 'r') as cuentas:
        leer_cuentas = csv.reader(cuentas)
        for line in leer_cuentas:
                browser.find_element(By.ID, "m_login_email").send_keys(line[cuenta])
    passwd = browser.find_element(By.NAME, "pass")
    with open ('contraseñas.csv', 'r') as contraseñas:
        leer_contraseñas = csv.reader(contraseñas)
        for line in leer_contraseñas:
                passwd.send_keys(line[contraseña])
    passwd.send_keys(Keys.ENTER)
    sleep(2)



def cerrar_session():
    browser.get('https://m.facebook.com')
    browser.find_element(By.NAME, 'Más').click()
    sleep(2)
    #browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div[6]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[8]/a/div[1]/i').click()
    browser.find_element(By.CSS_SELECTOR, 'i.icon.img.sp_oU0yTVetBGF_2x.sx_98c899').click()
    sleep(0.5)
    browser.find_element(By.NAME, 'm_savepass').click()

def publicar_grupo():
    browser.get(grupo)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div').click()
    sleep(0.9)
    browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div[5]/div[3]/form/div[7]/div/button[1]/div/div/div[2]').click()
    pyautogui.press('enter')
    sleep(0.5)
    browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div[5]/div[3]/div/div/button').click()
    sleep(6)

def comentario():
    browser.get(publicacion)
    browser.find_element(By.ID, 'composerInput').send_keys('Diego Martin al congreso')
    sleep(0.3)
    browser.find_element(By.NAME, "submit").click()

def comentario_imagen():
    browser.get(publicacion)
    browser.find_element(By.CSS_SELECTOR, 'div._51sa').click()
    sleep(0.3)
    pyautogui.press('enter')
    sleep(3)
    browser.find_element(By.NAME, "submit").click()

def like():
    browser.get(publicacion)
    browser.find_element(By.CSS_SELECTOR ,'div._52jj._15kl._3hwk._4g34').click()

def compartir():
    browser.get(publicacion)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/footer/div/div/div/div[3]/a').click()
    browser.find_element(By.ID, 'share-one-click-button').click()

def compartir_mensaje():
    browser.get(publicacion)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/footer/div/div/div/div[3]/a').click()
    sleep(1)
    browser.find_element(By.ID, 'share-with-message-button').click()
    sleep(1)
    browser.find_element(By.ID, 'share_msg_input').send_keys(mensaje)
    browser.find_element(By.ID, 'share_submit').click()

def compartir_grupos():
    for c in ['CAP','Full','Region', 'Pasco']:
        browser.get(publicacion)
        sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/footer/div/div/div/div[3]/a').click()
        browser.find_element(By.ID, 'share-in-a-group-button').click()
        sleep(1)
        for i in ['tab','tab','tab','tab']:
            pyautogui.press(i)
        pyautogui.write(c, interval=0.25)
        sleep(0.5)
        pyautogui.press('down')
        pyautogui.press('enter')
        browser.find_element(By.ID, 'share_msg_input').send_keys(mensaje)
        browser.find_element(By.ID, 'share_submit').click()


if __name__ == '__main__':
    while 10 > 0:
        browser = webdriver.Firefox(executable_path="/home/pyero/Documentos/geckodriver")
        for a in [1,2,3,4]:
            session(a,a)
            sleep(3)
            compartir()
            sleep(1)
            compartir_mensaje()
            sleep(1)
            compartir_grupos()
            sleep(1)
            publicar_grupo()
            sleep(1)
            comentario()
            sleep(1)
            comentario_imagen()
            sleep(3)
            cerrar_session()
        browser.close()
