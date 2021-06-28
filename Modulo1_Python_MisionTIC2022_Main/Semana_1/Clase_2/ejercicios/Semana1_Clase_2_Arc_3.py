#Usar de ejemplo 5 y 231

#Primera solución
def raizCuadrada():
    valor = float(input("Por favor, introduzca un numero a calcaluar su raiz cuadrada: "))
    raiz = valor ** 0.5
    return print("La raiz cuadrada de : ", valor, " es ", raiz)

raizCuadrada()

#Segunda solución
def raizCuadrada2():
    valor = int(input("Por favor, introduzca un numero a calcular su raiz cuadrada: "))
    raiz = valor ** 0.5
    return 'La raiz cuadrada de :' + str(valor) + ' es ' + str(raiz)

print(raizCuadrada2())

#Tercera solución
def raizCuadrada3():
    valor = float(input("Por favor, introduzca un numero a calcular su raiz cuadrada: "))
    raiz = valor ** 0.5
    print("La raiz cuadrada de : ", valor, " es ", round(raiz, 2))

raizCuadrada3()

#Cuarta solución
def raizCuadrada4(x):
    raiz = x ** 0.5
    return 'La raiz cuadrada de :' + str(x) + ' es ' + str(raiz)

print(raizCuadrada4(5))

#Quinta solución
def Ejercicio():
    print('Bienvenida')
    valor = int(input("Por favor, introduzca un numero a calcaluar su raiz cuadrada: "))
    
    def raizCuadrada5(valor):
        raiz = round(valor ** 0.5, 3)
        return 'La raiz cuadrada de :' + str(valor) + ' es ' + str(raiz)
    
    #raizCuadrada5(valor)

    print(raizCuadrada5(valor))

Ejercicio()

#Sexta solución
def Bienvenida():
    print('Bienvenid@s a mi código!!!')

def Ejercicio():
    Bienvenida()
    valor = int(input("Por favor, introduzca un numero a calcaluar su raiz cuadrada: "))
    
    def raizCuadrada5(valor):
        raiz = round(valor ** 0.5, 2)
        return 'La raiz cuadrada de :' + str(valor) + ' es ' + str(raiz)
    
    #raizCuadrada5(valor)

    print(raizCuadrada5(valor))

Ejercicio()