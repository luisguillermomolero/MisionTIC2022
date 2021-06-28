#Tuplas
#Las tuplas son inmutables

#Una tupla es una secuencia de valores muy parecida a una lista. 
# Los valores almacenados en una tupla pueden ser de cualquier 
# tipo, y están indexados por números enteros. La diferencia importante
# es que las tuplas son inmutables. Las tuplas también son comparables y 
# hashables, por lo que podemos ordenar listas de ellas y utilizar las 
# tuplas como valores clave en los diccionarios de Python.

#Sintácticamente, una tupla es una lista de valores separada por comas:

t = 'a', 'b', 'c', 'd', 'e'

#Aunque no es necesario, es común encerrar las tuplas entre paréntesis para 
#ayudarnos a identificar rápidamente las tuplas cuando miramos el código de Python:

t = ('esto es una cadena', 'b', 'c', 'd', 'e')
print(t)

#Para crear una tupla con un solo elemento, hay que incluir la coma final:

t1 = ('a',)
type(t1)

#Sin la coma Python trata ('a') como una expresión con una cadena entre 
# paréntesis que evalúa a una cadena:

t2 = ('a')
type(t2)

#Otra forma de construir una tupla es la tupla de función incorporada. Sin ningún 
#argumento, crea una tupla vacía:

t = tuple()
print(type(t))
<class 'tuple'>

#Si el argumento es una secuencia (cadena, lista o tupla), el resultado de la 
#llamada a la tupla es una tupla con los elementos de la secuencia:

t = tuple('lupines')
print(t)

#Debido a que tupla es el nombre de un constructor, debes evitar usarlo como un 
#nombre de variable.

#La mayoría de los operadores de listas también trabajan con tuplas. El operador 
# de corchetes indexa un elemento:

t = ('a', 'b', 'c', 'd', 'e')
print(t)

#Y el operador de rebanadas selecciona una serie de elementos.

print(t[1:3])

#Pero si intentas modificar uno de los elementos de la tupla, obtienes un error:

t[0] = 'A'
"""
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-17-7e674cdf20e6> in <module>
----> 1 t[0] = 'A'

TypeError: 'tuple' object does not support item assignment
No se pueden modificar los elementos de una tupla, pero se puede reemplazar una tupla por otra:
"""

t = ('A',) + t[1:]
print(t)
('A', 'b', 'c', 'd', 'e')

#Comparando tuplas
#Los operadores de comparación trabajan con tuplas y otras secuencias. Python 
# comienza comparando el primer elemento de cada secuencia. Si son iguales, pasa 
# al siguiente elemento, y así sucesivamente, hasta encontrar elementos que difieren. 
# Los elementos subsiguientes no se consideran (aunque sean realmente grandes).

(0, 1, 2) < (0, 3, 4)
True
(0, 1, 2000000) < (0, 3, 4)
True

#La función de sort funciona de la misma manera. Se ordena principalmente por el 
# primer elemento, pero en el caso de un empate, se clasifica por el segundo 
# elemento, y así sucesivamente.

#Esta característica se presta a un patrón llamado DSU

#Decorate: ordenar una secuencia construyendo una lista de tuplas con una o más 
# claves de clasificación que preceden a los elementos de la secuencia,

#Sort: Ordena la lista de tuplas usando la clasificación incorporada de Python, y

#Undecorate desordena la lista extrayendo los elementos ordenados de la secuencia.

#Por ejemplo, supongamos que tienes una lista de palabras y quieres ordenarlas de 
# más a menos:

txt = "but soft what light in yonder window breaks"
palabras = txt.split()
palabras


l = list()
for subcadena in palabras:
    l.append((len(subcadena), subcadena))
print(l)


l.sort(reverse=True)
print(l)

res = list()

for longitud, palabra in l:
    res.append(palabra)
    
print(res)

"""
El primer bucle construye una lista de tuplas, donde cada tupla es una palabra precedida 
por su longitud.

La función sort compara el primer elemento, la longitud, primero, y sólo considera el 
segundo elemento para romper los empates. El argumento de la palabra clave reverse=True le 
dice a sort que vaya en orden decreciente.

El segundo bucle atraviesa la lista de tuplas y construye una lista de palabras en orden
 descendente de longitud. Las palabras de cuatro caracteres se ordenan en orden alfabético 
 inverso, así que "what" aparece antes de "soft" en la siguiente lista. El resultado del 
 programa es el siguiente:

['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']

Por supuesto, la línea pierde mucho de su impacto poético cuando se convierte en una lista 
Python y se ordena en orden descendente de longitud de palabra.
"""

#Asignación de tupla
#Una de las características sintácticas únicas del lenguaje Python es la capacidad de tener
# una tupla en el lado izquierdo de una declaración de asignación. Esto permite asignar más 
# de una variable a la vez cuando el lado izquierdo es una secuencia.

#En este ejemplo tenemos una lista de dos elementos (que es una secuencia) y asignamos el 
# primer y segundo elemento de la secuencia a las variables x e y en una única sentencia.

m = ['have', 'fun']
x, y = m
print(x)
print(y)

#No es magia, Python traduce aproximadamente la sintaxis de la asignación de tupla como 
# la siguiente:

m = ['have', 'fun']
x = m[0]
y = m[1]
print(x)
print(y)

#Cuando usamos una tupla en el lado izquierdo de la declaración de asignación, omitimos los
# paréntesis, pero la siguiente es una sintaxis igualmente válida:

m = [ 'have', 'fun' ]
(x, y) = m

print(x)
print(y)

#Una aplicación particularmente inteligente de la asignación de tupla nos permite intercambiar 
# los valores de dos variables en una sola declaración:

a, b = b, a

#Ambos lados de esta declaración son tuplas, pero el lado izquierdo es una tupla de variables;
# el lado derecho es una tupla de expresiones. Cada valor del lado derecho se asigna a su 
# respectiva variable del lado izquierdo. Todas las expresiones del lado derecho se evalúan 
# antes de cualquiera de las asignaciones.

#El número de variables de la izquierda y el número de valores de la derecha deben ser iguales:

a, b = 1, 2, 3

#En general, el lado derecho puede ser cualquier tipo de secuencia (cadena, lista o tupla). 
# Por ejemplo, para dividir una dirección de correo electrónico en un nombre de usuario y un
# dominio, se podría escribir:

addr = 'monty@python.org'
uname, domain = addr.split('@')

#El valor de retorno de la división es una lista con dos elementos; el primer elemento se asigna 
# a uname, el segundo a dominio.

print(uname)
print(domain)


#Diccionarios y tuplas
#Los diccionarios tienen un método llamado elementos que devuelve una lista de tuplas, en la que 
# cada tupla es un par clave-valor:

d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)

#Como es de esperar de un diccionario, los artículos no están en un orden particular.

#Sin embargo, como la lista de tuplas es una lista, y las tuplas son comparables, podemos ahora 
# ordenar la lista de tuplas. Convertir un diccionario en una lista de tuplas es una forma de obtener
# el contenido de un diccionario ordenado por clave:

d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)
t.sort()
print(t)

#La nueva lista está ordenada en orden alfabético ascendente por el valor clave.

#Usando tuplas como claves en los diccionarios
#Debido a que las tuplas son hashable y las listas no, si queremos crear una clave compuesta para 
# usar en un diccionario debemos usar una tupla como clave.

#Nos encontraríamos con una clave compuesta si quisiéramos crear un directorio telefónico que mapee 
# desde pares de apellidos y nombres a números de teléfono. Asumiendo que hemos definido las variables 
# apellido, nombre y número, podríamos escribir una declaración de asignación de diccionario como sigue:

directory[apellido,nombre] = numero

#La expresión entre paréntesis es una tupla. Podríamos usar la asignación de la tupla en un bucle de for 
# para atravesar este diccionario.

for last, first in directory:
    print(first, last, directory[last,first])

#Este bucle atraviesa las teclas del directorio, que son tuplas. Asigna los elementos de cada 
# tupla al último y al primero, y luego imprime el nombre y el número de teléfono correspondiente.

#Métodos
#count()

#Este método recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la tupla.

valores = ("Python", True, "Zope", 5)
print("True ->", valores.count(True))
print("'Zope' ->", valores.count('Zope'))
print("5 ->", valores.count(5))


#index()
#Comparte el mismo método index() del tipo lista. Este método recibe un elemento como argumento, y 
# devuelve el índice de su primera aparición en la tupla.

valores = ("Python", True, "Zope", 5)
print(valores.index(True))
print(valores.index(5))

#El método devuelve un excepción ValueError si el elemento no se encuentra en la tupla, o en 
# el entorno definido.

valores = ("Python", True, "Zope", 5)
print(valores.index(4))


#Convertir a tuplas
#Para convertir a tipos tuplas debe usar la función tuple(), la cual está integrada en el interprete
# Python.

#Ejemplos
#A continuación, se presentan algunos ejemplos de su uso:

#Ejemplo simple de tupla

tupla = 12345, 54321, 'hola!'

#Ejemplo de tuplas anidadas

otra = tupla, (1, 2, 3, 4, 5)

#Operación asignar de valores de una tupla en variables

x, y, z = tupla

#Cuidar seguimiento del número de la numeración
#Una tarea común es iterar sobre una secuencia mientras cuidas el seguimiento de 
# la numeración de un elemento.

#Podría usar un bucle while con un contador o un bucle for usando la función range() y la función len():

tecnologias = ('Zope', 'Plone', 'Pyramid')
for i in range(0, len(tecnologias)):
    print(i, tecnologias[i])

#Ejemplo Cartero Viajante Vecino Mas Cercano

def RutaInicialVecinoMasCercano(distancias: dict, nodos: list)-> dict:
    #preparar las variables de salida
    rutaSolucion=[]
    kilometros = 0
    
    #modelar los nodos ya visitados
    yaesta = {}
    for nodo in nodos:
        yaesta.update({nodo:0})
    
    #inicializar el nodo de trabajo
    nodoActual = nodos[0]
    
    #iterar cuantos arcos debamos agregar
    for i in range(1,len(nodos)):
        
        #Crear unicamente las llaves que me interesan
        listallaves = []
        for nodo in nodos:
            if nodo != nodoActual and yaesta[nodo]==0:
                arco = (nodoActual,nodo)
                listallaves.append(arco)
        
        #Encontrar el minimo
        minimaDistancia = 999999
        for arco in listallaves:
            if distancias[arco] < minimaDistancia:
                minimaDistancia = distancias[arco]
                minimoarco = (minimaDistancia, arco)
        
        #Actualizar las listas de solucion y de YaEsta        
        rutaSolucion.append(minimoarco[1])
        kilometros = kilometros + minimoarco[0]
        
        yaesta[minimoarco[1][0]]= 1
        yaesta[minimoarco[1][1]]= 1
        
        nodoActual = minimoarco[1][1]
        
    #tenemos que crear el ultimo
    ultimoarco = (nodoActual,nodos[0])
    rutaSolucion.append(ultimoarco)
    kilometros = kilometros + distancias[ultimoarco]
    
    #Dar la salida
    salida = {}
    salida.update({"ruta":rutaSolucion})
    salida.update({"kilometraje":kilometros})
    
    return salida
    
    
distanciasEjemplo = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}

nodosEjemplo = ['H', 'A', 'B', 'C', 'D', 'E', 'F']


print(RutaInicialVecinoMasCercano(distanciasEjemplo, nodosEjemplo))