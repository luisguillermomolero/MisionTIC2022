"""
Manipulación de Colecciones
Map, Filter, Zip y Reduce

Introducción
Una vez presentadas las funciones de primer orden, funciones lambda y
funciones de orden superior, se desarrollan a continuación a través de
ejemplos los procedimientos para manipular grandes colecciones de datos:
    Map
    Filter
    Reduce
    Zip


La función map nos permite aplicar una
función sobre cada uno de los elementos de
un colección (listas, tuplas, etc, ...).

• Haremos uso de esta función siempre que
tengamos la necesidad de transformar el
valor de cada elemento en otro.


• La estructura de la función es la siguiente:

map: función que toma dos argumentos
map (funcion, secuencia), donde secuencia puede ser cualquier estructura

• La función a aplicar debe retornar un nuevo valor. Es apartir de estos
nuevos valores que obtendremos una nueva colección.
"""

def cuadrado(elemento=0):
    return elemento*elemento

lista = list(range(0,10))
print('\nLos valores de la lista son: ', lista)
resultado = list(map(cuadrado, lista))
print('El resultado de los cuadrado de la lista son: ', resultado)

#Desarrollado unicamente con lambda
resultado = list(map(lambda lista : lista*lista, lista))
print('\nEl resultado de los cuadrado de la lista son: ', resultado)

#Importando librerias
from math import pow
#Pow tiene 2 argumentos: valor, potencia, es decir, eleva a el "valor" a la "potencia"
numero = list(range(2,14,2))
potencia = list(range(1,12,2))
potenciados = list(map(pow, numero, potencia))
print('\nEl resultado de las potencias son: ', potenciados)

valores = list(range(24998, 25005))
print('\nLista de Valores a calcular incremento de 5000 pesos si son menores a 25000: ', valores)
minimo = 25000
valorIncrementado = list(map(lambda x: x if x >= minimo else (x + 5000), valores))
print('Los valores con incremento son :', valorIncrementado)

#Imprimir pares
print('\n')
elementos = list(range(2,10))
pares = list(map(lambda x: x if x % 2 != 0 else print('Par de una lista de números', x), elementos))

#Imprimir impares
print('\n')
elementos = list(range(2,10))
pares = list(map(lambda x: x if x % 2 == 0 else print('Impar de una lista de números', x), elementos))



"""
Función Filter
• La función filter, es quizás, una de las funciones más utilizadas 
al momento de trabajar con colecciones.
• Como su nombre lo indica, esta función nos permite realizar un 
filtro sobre los elementos de la colección.

üLa función a aplicar será aplicada a cada uno de los
elementos de la colección.
üEsta función siempre deberá retornar un valor
booleano.
üTodos aquellos elementos que tengan como resultado
True después de aplicar dicha función, serán los
elementos que pasen el filtro.
üA partir de estos elementos se creará una nueva
colección.
"""

#filter(funcion, secuencia)

#A continuación, filtramos primero los elementos impares y luego los pares de la 
# secuencia de los primeros 11 números de Fibonacci:

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
print('\nLista fibonacci: ', fibonacci)
odd_numbers = list(filter(lambda x: x % 2, fibonacci)) #filtramos los impares
print('Lista impares:   ', odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci)) #filtramos los pares
print('Lista pares      ', even_numbers)

even_numbers = list(filter(lambda x: x % 2 - 1, fibonacci)) #filtramos los pares
print('Lista pares      ', even_numbers)

#Obtener los elementos mayores a 5 de la siguiente tupla
def mayorCinco(elementos):
    return elementos>5

elementos = tuple(range(0,15))
print('\nTupla completa es: ', elementos)
resultado = tuple(filter(mayorCinco, elementos))
print('Tupla filtrada es: ', resultado)

#Con lambda

elementos = tuple(range(0,15))
print('\nTupla completa es: ', elementos)
resultado = tuple(filter(lambda x: x > 5, elementos))
print('Tupla filtrada es: ', resultado)

"""
Función Reduce
• Usaremos la función reduce cuando poseamos
una colección de elementos y necesitemos
generar un único resultado.
• reduce nos permitirá reducir los elementos de la
colección.
• Podemos ver a esta función como un acumulador.

• Aquí lo importante es detallar la función a aplicar. Esta función debe poseer,
obligatoriamente, dos parámetros.
• El primer parámetro hará referencia al acumulador, un variable que irá
modificando su valor por cada uno de los elementos en la colección.
• Por otro lado, el segundo parámetro hará referencia a cada elemento de la
colección. La función debe retornar un nuevo valor, será este nuevo valor el
que será asignado al acumulador.
"""

#Importar el método reduce de la libreria functools
from functools import reduce as r

lista = list(range(10,30))
print('\nLa lista de todos los valores a sumar es: ', lista)

def funcionAcumulador(acumulador=0, elemento=0):
    return acumulador+elemento
resultado = r(funcionAcumulador, lista)
print('La suma de todos los valores de la lista es: ', resultado)

#Con lambda

resultado = r(lambda acumulador = 0, elementos = 0: acumulador + elementos, lista )
print('\nLa suma de todos los valores de la lista es: ', resultado)

masrapido = r(lambda x,y: x+y, list(range(1000, 2000)))
print('\nTotal',masrapido)

#Determinar el máximo de una lista de valores numéricos usando reduce:

from functools import reduce
f = lambda a,b: a if (a > b) else b
print('El mayor valor de las lista es: ',r(f, {47,11,42,102,13}))

#Posibilidades de ganar un sorteo de loteria (6 / 49)

Winner = reduce(lambda x, y: x*y, range(44,50))/reduce(lambda x, y: x*y, range(1,7))
print('\nPosibilidad de ganar la loteria: ',Winner)

"""
Función Zip
• Zip es una función para reorganizar listas.
• Como parámetros admite un conjunto de listas.
• Lo que hace es tomar el elemento i-ésimo de
cada lista y unirlos en una tupla, después une
todas las tuplas en una sola lista.

"""

a = ["a", "b", "c", "d", "e", "f"]
b = [5, 3, 7, 9, 11, 2]
print('\n')
for t in zip(a,b):
    print(t)



location = {"Helgoland", "Kiel",            #Conjunto
            "Berlin-Tegel", "Konstanz", 
            "Hohenpeißenberg"}
air_pressure = [1021.2, 1019.9, 1023.7, 1023.1, 1027.7] #Lista
temperatures = (6.0, 4.3, 2.7, -1.4, -4.4)  #Tupla
altitude = (4, 27, 37, 443, 977)    #Tupla
                
print('\n')
for t in zip(location, air_pressure, temperatures, altitude):
    print(t, end = ' ')
