# Ejemplo 1
def suma(a, b):
    return a + b

print(suma(30, 10))

# Ejemplo 2
def suma2(a, b):
    return a + b

b = 30
a = 10
print(suma2(a, b))

# Ejemplo 3
def suma3(numero1, numero2):
    print(numero1 + numero2)
    print("\n")

resultado = suma3(30,10)

print(resultado)

# Ejemplo 4
def suma4(numero1,numero2):
    print(numero1 + numero2)
    print("\n")
    return numero1 + numero2

suma4(30, 10)

# Ejemplo 5
def mi_funcion(nombre, apellido):
    miNombre = nombre + apellido
    return(miNombre)
print(mi_funcion("Luis ", "Molero"))

# Ejemplo 6
def saludar(nombre, mensaje='Hola'):
    print(mensaje, nombre)
saludar('Pepe Grillo')

# Ejemplo 7
def mensaje():
    print("Ingrese por favor un valor")

def sumarDosnumeros():
    mensaje()
    num1 = float(input())
    mensaje()
    num2 = float(input())
    return print("la suma de ",num1, " + ", num2, " es igual a: ", num1 + num2)

sumarDosnumeros()

# Ejemplo 8
def mensaje2():
    print("Por favor, Introduzca un numero a calcaluar su raiz cuadrada: ")

def raizCuadrada():
    mensaje2()
    valor = int(input())
    raiz = valor ** 0.5
    return print("La raiz cuadrada de : ", valor, " es ", valor ** 0.5)

raizCuadrada()