"""
Programación Funcional Python

Funciones de Primera Clase,
Lambda y Orden Superior

El Paradigma de Programación Funcional ha tomado fuerza en los últimos años,
antes un enfoque académico, ahora una herramienta de desarrollo que disminuye
las asignaciones o estados de las variables (facilita el debugging o depuración).

• Python es multiparadigma y se pueden combinar las comodidades del paradigma
imperativo, con lo compacto del paradigma de programación funcional.

• En resumen, empalma la inmutabilidad de las funciones del paradigma funcional
con los efectos colaterales de los paradigmas imperativos (procedural y orientado a
objetos) para desarrollar soluciones de software.


*** Paradigmas de Programación ***


Podemos desarrollar software utilizando cualquiera de los
siguientes paradigmas:

• Paradigma Imperativo (cómo se hacen las cosas paso a paso)
    Spaghetti (Nombre despectivo para código no modular)
    Procedural/Estructurado
    Orientado a Objetos
• Paradigma Declarativo (qué se debe hacer)
    Lenguajes para bases de datos
    Programación Lógica
    Programación Funcional 


*** Conceptos Programación Funcional ***


• Se dice que en un lenguaje (como es el caso de Python) las funciones son de
primera clase (o que son "objetos de primera clase"), cuando se pueden tratar
como cualquier otro valor del lenguaje, es decir, cuando se pueden almacenar en
variables, pasar como parámetro y devolver desde funciones, sin ningún
tratamiento especial.

• Cuando una función no recibe otras funciones como parámetro, se la denomina
de primer orden.

• En el caso en el que sí las reciba, se llama de orden superior.


*** Funciones para Colecciones de Datos***


• Python ofrece unas funciones híbridas entre ambos paradigmas, muy versátiles
para trabajar con grandes colecciones de datos, que son funciones de orden
superior.

• Las funciones más utilizadas de este tipo, para realizar operaciones sobre listas
principalmente, sin utilizar ciclos, al estilo del paradigma funcional, son las
siguientes:

    Map
    Reduce
    Filter
    Zip


*** Envoltura de Funciones en Python ***


• Algo interesante de las funciones en Python es que estas pueden ser
asignadas a variables.
• Las funciones pueden ser utilizadas como argumento de otras funciones.
• Las funciones pueden retornar otras funciones

"""
def suma(val1=0, val2=0):
    return val1 + val2

def operacion(funcion,val1=0, val2=0):
    return funcion(val1,val2)

functionSuma = suma
resultado = operacion(functionSuma, 10, 20)
print('El resultado de la suma de la suma es = ',resultado)

"""
• Con esto nuestra función operacion puede ser utilizada para ejecutar
sumas, restas, multiplicaciones o cualquier tipo de operación que
necesitemos. Esta función puede actuar como un wrapper.
"""

def crearFuncion(operador):
    if operador == '+':
        def suma(val1=0, val2=0):
            return val1 + val2
        return suma
def operacion(funcion,val1=0, val2=0):
    return funcion(val1,val2)
functionSuma = suma
resultado = operacion(functionSuma, 10, 20)
print('\nEl resultado de la suma de la suma es = ',resultado)

"""
• Habrá ocasiones en las cuales necesitemos crear
funciones de manera rápida, en tiempo de
ejecución.
• Funciones las cuales realizan una tarea en
concreto, regularmente pequeña.
• En estos casos haremos uso de funciones lambda.
"""

# lambda argumentos: cuerpo de la función

sum = lambda x, y : x + y
sum(3,4)

# lambda usando map
# map: función que toma dos argumentos
# map (funcion, secuencia), donde secuencia puede ser cualquier estructura

suma = lambda val1=0, val2=0 : val1+val2
operador = lambda operacion, val1=0, val2=0 : operacion(val1, val2)
resultado = operador(suma, 10, 20)
print('\nEl resultado de la suma de la suma es = ',resultado)

C = [39.2, 36.5, 37.3, 38, 37.8] 
F = list(map(lambda x: (float(9)/5)*x + 32, C)) #Calculo de grados celsius a fahrenheit
print('\nGrados celsius: ', C)
print('Conversión a grados fahrenheit', F)

F = [39.2, 36.5, 37.3, 38, 37.8]
C = list(map(lambda x: (float(5)/9)*(x-32), F)) #Calculo de grados fahrenheit a celsius
print('\nGrados fahrenheit: ', F)
print('Conversión a grados celsius', C)

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
resultado = list(map(lambda x, y, z : x+y+z, a, b, c)) #Suma de tres listas
print('\nEl resultado de la sumas de las tres variables es: ', resultado)

resultado = list(map(lambda x, y : x+y, a, b)) #Suma de dos listas
print('\nEl resultado de la sumas de las dos variables es: ', resultado)

resultado = list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c)) #Resultado de una función
print('\nEl resultado de la función desarrollada en base a los valores de 3 listas es: ', resultado)

#Si una lista tiene menos elementos que las demás, el mapa se detendrá cuando se haya consumido la lista más corta:

a = [1, 2, 3]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
resultado = list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))
print('\nEl resultado de la función desarrollada en base a los valores de 3 listas es: ', resultado)