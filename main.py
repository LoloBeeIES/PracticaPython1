# Importamos el pythonDebugger
import pdb

# Esta funcion calcula el factorial de un numero dado y devuelve el resultado
def calcFactorial(numero):
    res = 1
    for i in range(1, numero+1):
        res *= i
    return res

# Esta funcion comprueba si un numero es primo, 
# si no lo es, devuelve false y si si lo es devuelve 
# el numero, porque sera introducido en un array
def checkPrimo(numero):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                return False
        else:
            return numero

def main():
    #Definimos las variables locales a la funcion main
    #Esta variable almacenara las edades de los alumnos
    alumnos = []
    #Esta variable almacenara el total de los numeros primos, para despues poderlos ordenar como array
    numPrimos = []

    #El total de numeros pares
    numPares = 0
    # El numero de iteraciones
    _NUM_ALUMNOS = 25

    print("Introduce la edad de " + str(_NUM_ALUMNOS) + " alumnos")
    # Mientras no haya introducido _NUM_ALUMNOS numeros, continuo pidiendolos
    while (len(alumnos)<_NUM_ALUMNOS):
        #Lo convierto a entero y controlo la excepcion
        try:
            numero = int(input())
        except:
            print("El la edad introducida no es valida")
            continue
        # Si sale de la excepcion es que el numero es valido
        alumnos.append(numero)
    #Ordeno el resultado
    alumnosSorted = sorted(alumnos)
    #Recorro todas las edades ya ordenadas
    for edad in alumnosSorted:
        #Si el numero es par, incremento el contador
        if edad%2 == 0:
            numPares+=1
        #Si  es primo, lo agrego a un array
        if (checkPrimo(edad) != False):
            numPrimos.append(edad)

    #Ordeno el array de los primos
    numPrimos = sorted(numPrimos)

    #Presento los resultados
    print("El mayor tiene %d y el menor %d" %(alumnosSorted[-1], alumnosSorted[0]))
    print("Edades pares %d Edades impares %d" %(numPares, len(alumnos)-numPares))
    print("El factorial del mayor (%d) es: %d" %(numPrimos[-1], calcFactorial(numPrimos[-1])))

if __name__ == '__main__':
        main()
