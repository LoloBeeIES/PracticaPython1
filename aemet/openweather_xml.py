import lxml,time, requests, pdb
from datetime import datetime
from lxml import html

#Usaremos estas cabeceras para hacernos pasar por un navegador normal
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

def main():
    #Openweathermap no podemos usarlo con este metodo, porque no compila JS, para hacer scrapping de una web con JS, usaremos selenium
    #URL obtenida por el navegador
    url = "https://weather.com/es-ES/tiempo/hoy/l/682990b6fea8c813446623b964f09ceafdadc3fd7f2ccdbeddfc7700ab426fde"

    # Obtenemos la fecha y hora como un objeto
    now = datetime.now()
    while True:
        try:
            # Hacemos la peticion, pasandole la url y las cabeceras
            response = requests.request("GET", url, headers=headers)
            # Comprobamos si se ha hecho bien, con el codigo de respuesta http
            if (response.status_code != 200):
                print("Error obteniendo la prediccion")
                exit(1)

            #Convierto el codigo fuente de la pagina en un XML
            xSource = html.fromstring(response.content)
            #uso la jerarquia xml para buscar el dato que me interesa, haciendo referencia al elemento que lo contiene
            # Para localizarlo, puedo revisar el codigo fuente de la web, o usar la extension "XPATH HELPER" del navegador chrome
            currTemp = xSource.xpath("//div/div/div/span[@class='CurrentConditions--tempValue--3KcTQ']/text()")
            #Si he obtenido resultados
            if currTemp:
                # Presentamos
                print("Temperatura " + now.strftime("%Y/%m/%d %H:%M:%S") + ": " + currTemp[0])

            # Dormimos
            time.sleep(60*60)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()
