"""
Listas
Python tiene varios tipos de datos compuestos y dentro de las secuencias, un tipo muy importante de secuencia son las listas.

Entre las secuencias, el más versátil, es la lista. Para definir una, usted debe escribir es entre corchetes cuadrados, separando sus elementos con comas cada uno.

La lista en Python son variables que almacenan arrays, internamente cada posición puede ser un tipo de datos distinto.

Las listas en Python son:

heterogéneas: pueden estar conformadas por elementos de distintos tipo, incluidos otras listas. mutables: sus elementos pueden modificarse. Una lista en Python es una estructura de datos formada por una secuencia ordenada de objetos.

Los elementos de una lista pueden accederse mediante su índice, siendo 0 el índice del primer elemento.
"""

#Ejercicio 1
lista = [1, 2.5, 'DevCode', [5,6] ,4]

print(lista[0]) # 1
print(lista[1]) # 2.5
print(lista[2]) # DevCode
print(lista[3]) # [5,6]
print(lista[3][0]) # 5
print(lista[3][1]) # 6
print(lista[1:3]) # [2.5, 'DevCode']
print(lista[1:6]) # [2.5, 'DevCode', [5, 6], 4]
print(lista[1:6:2]) # [2.5, [5, 6]]

#Ejercicio 2

lista = [ ]
lista

#Ejercicio 3

nombre = "Pepe"
edad = 25
listas = [nombre, edad]
listas

#Ejercicio 4

nombre = "Juan" # Queda la memoria cargada
listas

#Ejercicio 5

nombres = ["Ana", "Bernardo"]
edades = [22, 21]
lista = [nombres, edades]
lista

#Ejercicio 6

nombres += ["Cristina"]
lista

#Ejercicio 7

factura = ['pan', 'huevos', 100, 1234]
factura

#Ejercicio 8

factura[0]

#Ejercicio 9

factura[0]

#Ejercicio 10

len(factura)

#Ejercicio 11

len(factura) - 1

#Ejercicio 12

factura[-1]

#Ejercicio 13

factura[1] = "carne"
factura

#Ejercicio 14
#Métodos
#append(): Este método agrega un elemento al final de una lista.

versiones_plone = [2.5, 3.6, 4, 5]
versiones_plone

#Ejercicio 15
#Métodos
#append(): Este método agrega un elemento al final de una lista.

versiones_plone.append(6)
versiones_plone

#Ejercicio 16
#Métodos
#count(): Este método recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la lista.

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print("6 ->", versiones_plone.count(6))
print("5 ->", versiones_plone.count(5))
print( "2.5 ->", versiones_plone.count(2.5))

#Ejercicio 17
#Métodos
#extend(): Este método extiende una lista agregando un iterable al final.

versiones_plone = [2.1, 2.5, 3.6]
versiones_plone
versiones_plone.extend([4])
versiones_plone
versiones_plone.extend(range(5,7))
versiones_plone

#Ejercicio 18
#Métodos
#index(): Este método recibe un elemento como argumento, y devuelve el índice de su primera aparición en la lista.

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
print(versiones_plone.index(4))

#El método admite como argumento adicional un índice inicial a partir de donde comenzar la búsqueda, opcionalmente también el índice final.

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
versiones_plone[2]

print(versiones_plone.index(4, 2))

versiones_plone[3]

print(versiones_plone.index(4, 5))

versiones_plone[6]

#El método devuelve un excepción ValueError si el elemento no se encuentra en la lista, o en el entorno definido.

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
print(versiones_plone.index(9))
"""
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-50-c3c11fc57eef> in <module>
----> 1 print(versiones_plone.index(9))

ValueError: 9 is not in list
"""

#Ejercicio 19
#Métodos
#insert(): Este método inserta el elemento x en la lista, en el índice i.

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone)

versiones_plone.insert(2, 3.7)
print(versiones_plone)

#Ejercicio 20
#Métodos
#pop(): Este método devuelve el último elemento de la lista, y lo borra de la misma.

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]

print(versiones_plone.pop())

print(versiones_plone)

#Opcionalmente puede recibir un argumento numérico, que funciona como índice del elemento (por defecto, -1)

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone.pop(2))

print(versiones_plone)

#Ejercicio 21
#Métodos
#remove(): Este método recibe como argumento un elemento, y borra su primera aparición en la lista.

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone)

versiones_plone.remove(2.5)
print(versiones_plone)

#El método devuelve un excepción ValueError si el elemento no se encuentra en la lista.

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone)

versiones_plone.remove(7)
"""
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-60-09e9ae60eb3f> in <module>
----> 1 versiones_plone.remove(7)

ValueError: list.remove(x): x not in list

"""

#Ejercicio 22
#Métodos
#reverse(): Este método invierte el orden de los elementos de una lista.

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone)

versiones_plone.reverse()
print(versiones_plone)

#Ejercicio 23
#Métodos
#sort(): Este método ordena los elementos de una lista.

versiones_plone = [4, 2.5, 5, 3.6, 2.1, 6]
print(versiones_plone)
[4, 2.5, 5, 3.6, 2.1, 6]
versiones_plone.sort()
print(versiones_plone)
[2.1, 2.5, 3.6, 4, 5, 6]

#El método sort() admite la opción reverse, por defecto, con valor False. De tener 
# valor True, el ordenamiento se hace en sentido inverso.

versiones_plone.sort(reverse=True)
print(versiones_plone)

#Ejercicio 24
#Convertir a listas

#Para convertir a tipos listas debe usar la función list() la cual esta integrada en el interprete Python.

"""
Ejemplos
A continuación, se presentan algunos ejemplos de su uso:

Ejemplo de establecer una colección ordenada/arreglos o vectores

"""

lista = [2, "CMS", True, ["Plone", 10]]
print(lista, type(lista))

#Ejemplo de acceder a un elemento especifico de una lista

l2 = lista[1]
print(l2)

#Ejemplo de acceder a un elemento a una lista anidada

l3 = lista[3][0]
print(l3)

#Ejemplo de establecer nuevo valor de un elemento de lista

lista[1] = 4
print(lista)

lista[1] = "CMS"

#Ejemplo de obtener un rango de elemento especifico

l3 = lista[0:3]
print(l3)

#Ejemplos de obtener un rango con saltos de elementos específicos

l4 = lista[0:3:2]
print(l4)

l5 = lista[1::2]
print(l5)

#Ejemplo 25

#Ejemplo de iterar sobre cualquier secuencia

#Usted puede iterar sobre cualquier secuencia 
#(cadenas de caracteres, lista, claves en un diccionario, lineas en un archivo, ...):

#Ejemplo de iterar sobre una cadenas de caracteres


vocales = 'aeiou'
for letra in 'hermosa':
     if letra in vocales:
            print(letra)

#Ejemplo de iterar sobre una lista

#Para separar una cadena en frases, los valores pueden separarse
#con la función integrada split().

mensaje = "Hola, como estas tu?"
mensaje.split() # retorna una lista
['Hola,', 'como', 'estas', 'tu?']
for palabra in mensaje.split():
    print(palabra)

#Ejemplo de iterar sobre dos o más secuencias
#Para iterar sobre dos o más secuencias al mismo tiempo, los valores
#pueden emparejarse con la función integrada zip().

preguntas = ['nombre', 'objetivo', 'sistema operativo']
respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']

for pregunta, respuesta in zip(preguntas, respuestas):
    print('¿Cual es tu {0}?, la respuesta es: {1}.'.format(
         pregunta, respuesta))


#Ejemplo ayuda con listas

help(list)
Help on class list in module builtins:


"""
class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
 """