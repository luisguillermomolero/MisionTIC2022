def primeraFuncion(): # función externa
    print ("\n \"Hola desde la función externa\" \n ")

    def segundaFuncion(): # función interna
        print ("\n \"Hola desde la función interna\" \n")
    
    segundaFuncion()

primeraFuncion()


def sumaNumeros():
    a = 6
    b = 7
    suma = a + b
    return "la suma de " + str(a) + " + " + str(b) + " es igual a: " + str(suma)

print(sumaNumeros())

def sumaNumeros(a, b):
    suma = a + b
    return "El resultado de la suma de " + str(a) + " + " + str(b) + ' es igual a: ' + str(suma)

print(sumaNumeros(5, 6))