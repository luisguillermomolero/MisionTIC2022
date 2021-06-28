"""
Introducción
• En la Unidad 3, hemos trabajado con varios contenedores, además hemos
aprendido a diferenciar cuándo pueden ajustarse mejor a nuestras
necesidades.
• Una de las grandes fortalezas del lenguaje Python, es la gran flexibilidad que
presentan los contenedores para su creación y actualización.
• Adicionalmente, en Python es posible transformar un contenedor cargado
de información, a otro tipo de contenedor en caso de que necesitemos
cambiar la forma como manipulamos la información que alojan
"""

Cadena1 = 'hola '    #Secuencial inmutable
Cadena2 = 'mundo'   #Secuencial inmutable
numero = 15
Tupla = (1,2,3,4,5) #Secuencial inmutable
Lista = [1,2,3,4,5] #Secuencial mutable
Diccionario = {'01': 1, '02': 2, '03': 4}   #No secuencial mutable
Conjunto = {1,2,3,4,5}  #No secuencial inmmutable

#Conversion de cadena a lista

print('Conversion de cadena a lista: ', Cadena1,Cadena2)
lista = list(Cadena1+Cadena2)
print('Conversion de cadena a lista: ',lista)
union = ''.join(lista)
print('uso de join: ', union)

#Conversion de cadena a tuplas

tupla1 = tuple(Cadena2)
print('\nConversion de cadena a tuplas: ', tupla1)
tuplaGral = (tupla1, numero, tuple(Cadena2) )
print('Conversion de cadena a tuplas: ', tuplaGral)

#Conversion de cadena a set() (conjunto)

print('\nConversion de cadena a conjunto: ', Cadena1, Cadena2)
print('Conversion de cadena a conjunto: ', set(Cadena1+Cadena2))

#Conversion de lista a tuplas

lista = list(Cadena2)
print('\nConversion de lista a tuplas: ', lista)
tupla = tuple(lista)
print('Conversion de lista a tuplas: ', tupla)

#Conversion de lista a set()

print('\nConversion de lista a set(): ', list(Cadena2))
Conjunto = set(Cadena2)
print('Conversion de lista a set(): ', Conjunto)

#Conversion de tupla a cadena

tupla = tuple(Cadena2)
print('\nConversion de tupla a cadena: ', tupla)
cadena = ''.join(tupla)
print('Conversion de tupla a cadena: ', cadena)

#Conversion de tuplas a lista

tupla = tuple(Cadena1+Cadena2)
print('\nConversion de tuplas a lista: ', tupla)
lista = list(tupla)
print('Conversion de tuplas a lista: ', lista)

#Conversion de tuplas a conjunto

tupla = tuple(Cadena1+Cadena2)
print('\nConversion de tuplas a conjunto: ', tupla)
conjunto = set(tupla)
conjunto.add(2546)
print('Conversion de tuplas a conjunto: ',conjunto)

#Conversion de conjunto a cadena
conjunto = set(Cadena1+Cadena2)
print('\nConversion de conjunto a cadena: ',conjunto)
cadena = ''.join(conjunto)
print('Conversion de conjunto a cadena: ',cadena)

#Conversion de conjunto a tupla
conjunto = set(Cadena2)
print('\nConversion de conjunto a tupla: ', conjunto)
tupla = tuple(conjunto)
print('Conversion de conjunto a tupla: ', tupla)

#Conversion de conjunto a lista
conjunto = set(cadena)
print('\nConversion de conjunto a lista: ', conjunto)
lista = list(conjunto)
print('Conversion de conjunto a lista: ', lista)

"""
Conversión a Diccionarios
• Los diccionarios mezclan características de los conjuntos al no permitir
repeticiones de sus etiquetas, conservan el orden como los contenedores
diferentes a los conjuntos, pero su conversión requiere resolver la llave o
etiqueta que tiene cada uno de sus elementos.
• A diferencia de las tuplas, cadenas y listas, cuyos índices o etiquetas son
autonuméricos, el diccionario necesita su especificación.
• En los siguientes ejemplos se presenta el uso de la función zip para relacionar
una colección generada automáticamente con los elementos y satisfacer la
llave. Esta función se presentará con más detalle en el transcurso de la unidad.
"""

#Conversion de cadena a diccionario
print('\nConversion de cadena a diccionario: ', Cadena2)
diccionario = dict(zip(range(len(Cadena2)), Cadena2))
print('Conversion de cadena a diccionario: ', diccionario)

#Conversion de lista a diccionario
lista = list(Cadena1 + Cadena2)
print('\nConversion de lista a diccionario', lista)
diccionario = dict(zip(range(len(lista)), lista))
print('Conversion de lista a diccionario', diccionario)

#Conversion de tupla a diccionario
tupla = tuple(Cadena1 + Cadena2)
print('\nConversion de tupla a diccionario', tupla)
diccionario = dict(zip(range(len(tupla)), tupla))
print('Conversion de tupla a diccionario', diccionario)

#Conversion de conjunto a diccionario
conjunto = set(Cadena1 + Cadena2)
print('\nConversion de conjunto a diccionario', conjunto)
diccionario = dict(zip(range(len(conjunto)), conjunto))
print('Conversion de conjunto a diccionario', diccionario)

"""
Conversión desde Diccionarios
• En el proceso contrario, dado que los diccionarios constituyen dos
colecciones, una correspondiente a las llaves y otra correspondiente a los
valores, se debe especificar cuál colección se requiere, o generalizar
obteniendo todos los ítems, que son retornados como tuplas.
• En los siguientes ejemplos se presenta cómo la información se puede
extraer y convertir en cualquiera de los contenedores.
• En algunos casos sólo se convierten los valores por la compatibilidad de
tipos que requerirían funciones adicionales.
"""

#Conversion de diccionario a cadena
diccionario = dict({0: 'h', 1: 'o', 2: 'l', 3: 'a', 4: ' ', 5: 'm', 6: 'u', 7: 'n', 8: 'd', 9: 'o'})
print('\nConversion de diccionario a cadena: ',diccionario)
cadena = ''.join(diccionario.values())
print('Conversion de diccionario a cadena: ',cadena)

#Conversion de diccionario a tuplas
diccionario = dict({0: 'h', 1: 'o', 2: 'l', 3: 'a', 4: ' ', 5: 'm', 6: 'u', 7: 'n', 8: 'd', 9: 'o'})
print('\nConversion de diccionario a tuplas: ',diccionario)
tuplaLlave = tuple(diccionario.keys())
print('Conversion de diccionario a tuplas: ',tuplaLlave)
tuplaValores = tuple(diccionario.values())
print('Conversion de diccionario a tuplas: ',tuplaValores)
tuplaItems = tuple(diccionario.items())
print('Conversion de diccionario a tuplas: ',tuplaItems)

#Conversion de diccionario a lista
diccionario = dict({0: 'h', 1: 'o', 2: 'l', 3: 'a', 4: ' ', 5: 'm', 6: 'u', 7: 'n', 8: 'd', 9: 'o'})
print('\nConversion de diccionario a lista: ',diccionario)
listaLlave = list(diccionario.keys())
print('Conversion de diccionario a lista: ',listaLlave)
listaValores = list(diccionario.values())
print('Conversion de diccionario a lista: ',listaValores)
listaItems = list(diccionario.items())
print('Conversion de diccionario a lista: ',listaItems)

#Conversion de diccionario a conjunto
diccionario = dict({0: 'h', 1: 'o', 2: 'l', 3: 'a', 4: ' ', 5: 'm', 6: 'u', 7: 'n', 8: 'd', 9: 'o'})
print('\nConversion de diccionario a conjunto: ',diccionario)
conjuntoLlave = set(diccionario.keys())
print('Conversion de diccionario a conjunto: ',conjuntoLlave)
conjuntoValores = set(diccionario.values())
print('Conversion de diccionario a conjunto: ',conjuntoValores)
conjuntoItems = set(diccionario.items())
print('Conversion de diccionario a conjunto: ',conjuntoItems)