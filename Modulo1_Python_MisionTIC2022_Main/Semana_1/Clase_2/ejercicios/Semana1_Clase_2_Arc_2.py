def bievenida():
    print('bienvenidos')

def sumarDosnumeros():
    bievenida()
    num1 = float(input("Ingrese el numero 1: "))
    num2 = float(input("Ingrese el numero 2: "))
    print ("la suma de", num1, " + ", num2, " es igual a: ", num1 + num2)

sumarDosnumeros()