#Creación de un conjunto
#Para crear un conjunto especificamos sus elementos entre llaves:

s = {1, 2, 3, 4}

#Al igual que otras colecciones, sus miembros pueden ser de diversos tipos:

s = {True, 3.14, None, False, "Hola mundo", (1, 2)}

#No obstante, un conjunto no puede incluir objetos mutables como listas, 
# diccionarios, e incluso otros conjuntos.

s = {[1, 2]}

#Python distingue este tipo operación de la creación de un diccionario ya que no 
# incluye dos puntos. Sin embargo, no puede dirimir el siguiente caso:

s = {}

#Por defecto, la asignación anterior crea un diccionario. Para generar un conjunto 
# vacío, directamente creamos una instancia de la clase set:

s = set()

#De la misma forma podemos obtener un conjunto a partir de cualquier objeto iterable:

s1 = set([1, 2, 3, 4])
s2 = set(range(10))
print(s1)
print(s2)

#Un set puede ser convertido a una lista y viceversa. En este último caso, los elementos
# duplicados son unificados.

list({1, 2, 3, 4})
set([1, 2, 2, 3, 4])

# Crea un conjunto con una serie de elementos entre llaves
# Los elementos repetidos se eliminan

c = {1, 3, 2, 9, 3, 1}
print(c)

# Crea un conjunto a partir de un string
# Los caracteres repetidos se eliminan

a = set('Hola Pythonista')
print(a)

# Crea un conjunto a partir de una lista
# Los elementos repetidos de la lista se eliminan

unicos = set([3, 5, 6, 1, 5])
print(unicos)

#Cómo acceder a los elementos de un conjunto en Python
#Dado que los conjuntos son colecciones desordenadas, en ellos no se guarda la posición 
# en la que son insertados los elementos como ocurre en los tipos list o tuple. Es por
# ello que no se puede acceder a los elementos a través de un índice.

#Sin embargo, sí se puede acceder y/o recorrer todos los elementos de un conjunto usando 
# un bucle for:

mi_conjunto = {1, 3, 2, 9, 3, 1}
print(mi_conjunto)
for numero in mi_conjunto:
    print(numero)

#Métodos
#Los objetos de tipo conjunto mutable y conjunto inmutable integra una serie de métodos 
# integrados a continuación:

#add()

# Este método agrega un elemento a un conjunto mutable. Esto no tiene efecto si el 
# elemento ya esta presente.

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
print(set_mutable1)
set_mutable1.add(22.000001)
print(set_mutable1)

#clear()
#Este método remueve todos los elementos desde este conjunto mutable.

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
print(set_mutable1)
set_mutable1.clear()
print(set_mutable1)


#copy()
#Este método devuelve una copia superficial del tipo conjunto mutable o conjunto 
# inmutable:

set_mutable = set([4.0, 'Carro', True])
otro_set_mutable = set_mutable.copy()
set_mutable == otro_set_mutable

#difference()
#Este método devuelve la diferencia entre dos conjunto mutable o conjunto inmutable: 
# todos los elementos que están en el primero, pero no en el argumento.

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1)
print(set_mutable2)
print(set_mutable1.difference(set_mutable2))
print(set_mutable2.difference(set_mutable1))

#La diferencia también se puede generar de la siguiente manera. Se retorna un nuevo 
# conjunto que contiene los elementos de a que no están en b.

a = {1, 2, 3, 4}
b = {2, 3}
c = a - b
print(c)

#Dos conjuntos son iguales si y solo si contienen los mismos elementos 
# (a esto se lo conoce como principio de extensionalidad):

{1, 2, 3} == {3, 2, 1}
{1, 2, 3} == {1, 2, 6}

#difference_update()
#Este método actualiza un tipo conjunto mutable llamando al método difference_update() 
# con la diferencia de los conjuntos.

proyecto1 = {'python', 'Zope2', 'ZODB3', 'pytz'}
proyecto1
proyecto2 = {'python', 'Plone', 'diazo'}
proyecto2
proyecto1.difference_update(proyecto2)
proyecto1

#Si proyecto1 y proyecto2 son dos conjuntos. La diferencia del conjunto proyecto1 
# y conjunto proyecto2 es un conjunto de elementos que existen solamente en el conjunto
# proyecto1 pero no en el conjunto proyecto2.

#discard()
#Este método remueve un elemento desde un conjunto mutable si esta presente.

paquetes = {'python', 'zope', 'plone', 'django'}
paquetes
paquetes.discard('django')
paquetes

#El conjunto mutable permanece sin cambio si el elemento pasado como argumento al
# método discard() no existe.

paquetes = {'python', 'zope', 'plone', 'django'}
paquetes.discard('php')
paquetes

#intersection()
#Este método devuelve la intersección entre los conjuntos mutables o conjuntos 
# inmutables: todos los elementos que están en ambos.

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1)
print(set_mutable2)
print(set_mutable1.intersection(set_mutable2))
print(set_mutable2.intersection(set_mutable1))

#También se puede expresar de la siguiente forma La intersección opera de forma análoga, 
# pero con el operador &, y retorna un nuevo conjunto con los elementos que se encuentran
# en ambos.

set_intersection = set_mutable1 & set_mutable2
print(set_intersection)

#intersection_update()
#Este método actualiza un conjunto mutable con la intersección de ese mismo y otro 
# conjunto mutable.

#El método intersection_update() le permite arbitrariamente varios numero de argumentos 
# (conjuntos).

proyecto1 = {'python', 'Zope2', 'pytz'}
proyecto1
proyecto2 = {'python', 'Plone', 'diazo', 'z3c.form'}
proyecto2
proyecto3 = {'python', 'django', 'django-filter'}
proyecto3
proyecto3.intersection_update(proyecto1, proyecto2)
proyecto3

#La intersección de dos o mas conjuntos es el conjunto de elemento el cual es común 
# a todos los conjuntos.

#isdisjoint()
#Este método devuelve el valor True si no hay elementos comunes entre los conjuntos 
# mutables o conjuntos inmutables.

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1)
print(set_mutable2)
print(set_mutable1.isdisjoint(set_mutable2))

#issubset()
#Este método devuelve el valor True si el conjunto mutable es un subconjunto del conjunto 
# mutable o del conjunto inmutable argumento.

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
set_mutable3 = set([11, 5, 2, 4])
print( set_mutable1)
print(set_mutable2)
print(set_mutable3)
print(set_mutable2.issubset(set_mutable1))
print(set_mutable3.issubset(set_mutable1))

#issuperset()
#Este método devuelve el valor True si el conjunto mutable o el conjunto inmutable es un 
# superset del conjunto mutable argumento.

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
set_mutable3 = set([11, 5, 2, 4])
print(set_mutable1)
print(set_mutable2)
print(set_mutable3)
print(set_mutable1.issuperset(set_mutable2))
print(set_mutable1.issuperset(set_mutable3))

#pop()
#Este método remueve arbitrariamente y devuelve un elemento de conjunto mutable. 
# El método pop() no toma ningún argumento. Si el conjunto mutable esta vacío se 
# lanza una excepción KeyError.

paquetes = {'python', 'zope', 'plone', 'django'}
paquetes
print("Valor aleatorio devuelto es:", paquetes.pop())
print(paquetes)
print("Valor aleatorio devuelto es:", paquetes.pop())
paquetes
print("Valor aleatorio devuelto es:", paquetes.pop())
paquetes
print( "Valor aleatorio devuelto es:", paquetes.pop())
print("Valor aleatorio devuelto es:", paquetes.pop())

#Tenga en cuenta que usted podría obtener diferente salida devueltas usando el método 
# pop() por que remueve aleatoriamente un elemento.

#remove()
#Este método busca y remueve un elemento de un conjunto mutable, si debe ser un 
# miembro.

paquetes = {'python', 'zope', 'plone', 'django'}
paquetes
paquetes.remove('django')
paquetes

#Si el elemento no es existe en el conjunto mutable, lanza una excepción KeyError.
# Usted puede usar el método discard() si usted no quiere este error. El conjunto 
# mutable permanece sin cambio si el elemento pasado al método discard() no existe.

#Un conjunto es una colección desordenada de elementos. Si usted quiere remover 
# arbitrariamente elemento un conjunto, usted puede usar el método pop().

#symmetric_difference()
#Este método devuelve todos los elementos que están en un conjunto mutable e conjunto 
# inmutable u otro, pero no en ambos.

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1)
print(set_mutable2)
print(set_mutable1.symmetric_difference(set_mutable2))

#symmetric_difference_update()
#Este método actualiza un conjunto mutable llamando al método symmetric_difference_update()
# con los conjuntos de diferencia simétrica.

#La diferencia simétrica de dos conjuntos es el conjunto de elementos que están en 
# cualquiera de los conjuntos pero no en ambos.

proyecto1 = {'python', 'plone', 'django'}
proyecto1
proyecto2 = {'django', 'zope', 'pyramid'}
proyecto2
proyecto1.symmetric_difference_update(proyecto2)
proyecto1

#El método symmetric_difference_update() toma un argumento simple de un tipo conjunto
# mutable.

#union()
#Este método devuelve un conjunto mutable y conjunto inmutable con todos los elementos 
# que están en alguno de los conjuntos mutables y conjuntos inmutables.

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1)
print(set_mutable2)
print(set_mutable1.union(set_mutable2))

#La unión también se puede realizar con el caracter | y retorna un conjunto que contiene 
# los elementos que se encuentran en al menos uno de los dos conjuntos involucrados en la 
# operación.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b


#update()
#Este método agrega elementos desde un conjunto mutable (pasando como un argumento) un tipo 
# tupla, un tipo lista, un tipo diccionario o un tipo conjunto mutable llamado con el
# método update().

#A continuación un ejemplo de agregar nuevos elementos un tipo conjunto mutable usando 
# otro tipo conjunto mutable:

version_plone_dev = set([5.1, 6])
version_plone_dev
versiones_plone = set([2.1, 2.5, 3.6, 4])
versiones_plone
versiones_plone.update(version_plone_dev)
versiones_plone

#A continuación un ejemplo de agregar nuevos elementos un tipo conjunto mutable usando 
# otro tipo cadena de caracteres:

cadena = 'abc'
cadena
conjunto = {1, 2}
conjunto.update(cadena)
conjunto

#A continuación un ejemplo de agregar nuevos elementos un tipo conjunto mutable 
# usando otro tipo diccionario:

diccionario = {'key': 1, 2:'lock'}
diccionario.items()
conjunto = {'a', 'b'}
conjunto.update(diccionario)
conjunto

#Convertir a conjuntos
#Para convertir a tipos conjuntos debe usar las funciones set() y frozenset(), las cuales 
# están integradas en el interprete Python.