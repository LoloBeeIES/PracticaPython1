import requests, pdb, time
from pprint import pprint
from datetime import datetime

#Usaremos estas cabeceras para hacernos pasar por un navegador normal
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

def main():

    #Endpoint para obtener las estaciones
    url = "https://openweathermap.org/data/2.5/weather?id=2518207&units=metric&appid=439d4b804bc8187953eb36d2a8c26a02"

    while True:
        try:
            #Obtenemos la fecha y hora como un objeto
            now = datetime.now()
            #Hacemos la peticion, pasandole la url y las cabeceras
            response = requests.request("GET", url, headers=headers)
            #Comprobamos si se ha hecho bien, con el codigo de respuesta http
            if (response.status_code != 200):
                print("Error obteniendo la prediccion")
                exit(1)

            #Requests ya tiene un metodo para convertir la respuesta a JSON (si tiene formato de JSON)
            datos = response.json()
            #Presentamos
            print("Temperatura " + now.strftime("%Y/%m/%d %H:%M:%S") + ": " + str(datos['main']['temp']))
            #Dormimos
            time.sleep(60*60)
        except KeyboardInterrupt:
            break

    print("Exit")

if __name__ == '__main__':
    main()

