import pdb

def calcFactorial(numero):
    res = 1
    for i in range(1, numero+1):
        res *= i
    return res

def checkPrimo(numero):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                return False
        else:
            return numero

def main():
    alumnos = []
    numPrimos = []

    numPares = 0
    _NUM_ALUMNOS = 25

    print("Introduce la edad de " + str(_NUM_ALUMNOS) + " alumnos")
    while (len(alumnos)<_NUM_ALUMNOS):
        try:
            numero = int(input())
        except:
            print("El la edad introducida no es valida")
            continue
        alumnos.append(numero)

    alumnosSorted = sorted(alumnos)

    for edad in alumnosSorted:
        if edad%2 == 0:
            numPares+=1
        if (checkPrimo(edad) != False):
            numPrimos.append(edad)


    numPrimos = sorted(numPrimos)
    print("El mayor tiene %d y el menor %d" %(alumnosSorted[-1], alumnosSorted[0]))
    print("Edades pares %d Edades impares %d" %(numPares, len(alumnos)-numPares))
    print("El factorial del mayor (%d) es: %d" %(numPrimos[-1], calcFactorial(numPrimos[-1])))

if __name__ == '__main__':
        main()