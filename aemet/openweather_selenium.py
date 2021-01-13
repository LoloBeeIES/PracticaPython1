#Descargar el driver de firefox de https://github.com/mozilla/geckodriver/releases

import time, pdb
from datetime import datetime
import lxml.html as lh
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = None

def wait4ElementID(elementID):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, elementID)))

def wait4ElementClass(elementClass):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, elementClass)))

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver

def main():
    global driver

    #Inicializamos el driver que se va a encargar de manejar el navegador
    driver = init_driver()
    #URL obtenida por el navegador
    url = "https://openweathermap.org/city/2518207"

    # Obtenemos la fecha y hora como un objeto
    now = datetime.now()
    while True:
        try:
            # Hacemos la peticion
            driver.get(url)

            #Esperamos al elemento async
            wait4ElementClass("heading")

            #Hacemos lo mismo que en el otro ejercicio, lo convertimos a xml
            xSource = lh.fromstring(driver.page_source)

            #Obtenemos la temperatura
            currTemp = xSource.xpath("//span[@class='heading']/text()")

            #Si he obtenido resultados
            if currTemp:
                # Presentamos
                print("Temperatura " + now.strftime("%Y/%m/%d %H:%M:%S") + ": " + currTemp[0])

            # Dormimos
            time.sleep(60*60)
        except KeyboardInterrupt:
            break

    driver.close()

if __name__ == '__main__':
    main()
