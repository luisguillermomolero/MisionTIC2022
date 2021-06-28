"""
SECUENCIAS
Un tipo de secuencia es un tipo de dato en Python el cual es capaz de 
almacenar mas de un valor (o ninguno si la secuencia esta vacía), los 
cuales pueden ser secuencialmente (de ahí el nombre) examinados, elemento 
por elemento.
"""

"""
MUTABILIDAD
Es una propiedad de cualquier tipo de dato en Python que 
describe su disponibilidad para poder cambiar libremente durante la ejecución 
de un programa. Existen dos tipos de datos en Python: mutables e inmutables.
"""

"""
INMUTABILIDAD
Las tuplas....
"""

"""
•	Cada clave debe de ser única. No es posible tener una clave duplicada.
•	Una clave puede ser un tipo de dato de cualquier tipo: puede ser un número
    (entero o flotante), o incluso una cadena.
•	Un diccionario no es una lista. Una lista contiene un conjunto de valores 
    numerados, mientras que un diccionario almacena pares de valores.

"""


#Ejercicios 1
diccionario = {}

print(diccionario)

#Ejemplo 2

# #Diccionario vacio usando el constructor dict()
diccionario = dict()

print(diccionario)

#Ejercicio 2 - 

# Si necesitamos almacenar nuevos valores basta con separarlos mediante una coma.

diccionario = {
    "total": 55, 
    "descuento": True, 
    "subtotal": 15.325478596,
    "Cliente" : 'Luis Molero'
    }

print(diccionario)

#Ejercicio 4 

#Argumentos con nombre
Diccionario = dict(uno = 1, dos = 2, tres = 3)

print(Diccionario)

#Pares clave: valor encerrados entre llaves
Diccionario = dict({'uno': 1, 'dos': 2, 'tres': 3})

print(Diccionario)

#Iterable que contiene iterables con dos elementos

Diccionario = dict([('uno', 'Luis Molero'), ('dos', True), ('tres', 3.321654987)])
print(Diccionario)

#Ejercicio 5

dict = {
    "gato" : "chat", 
    "perro" : "chien", 
    "caballo" : "cheval"
    }

numerosTelefono = {
    'jefe' : '+57 5551234567', 
    'Suzy' : '+57 3669258787'
    }

diccionarioVacio = {}

print(dict)
print(numerosTelefono)
print(diccionarioVacio)

print(dict['gato'])
print(numerosTelefono['Suzy'])

#Ejemplo 6

usuario = {
    'nombre': 'Nombre del usuario',
    'edad' : 23, 
    'curso': 'Curso de Python',
    'skills':{
        'programacion' : True,
        'base_de_datos': False
    },
    'No medallas' : 10
}

print(usuario)

#Ejemplo 6
"""
Para poder agregar, obtener o modificar algún valor del diccionario haremos 
uso de corchetes.
"""
diccionario = dict()

diccionario['usuario'] = 'eduardo'
print(diccionario['usuario'])
diccionario['usuario'] = 'Carlos'
print(diccionario['usuario'])

diccionario['usuario'] = 'Luis'
print(diccionario['usuario'])
diccionario['usuario'] = 'Molero'
print(diccionario['usuario'])

#Ejemplo 7
"""
podemos obtener todas las llaves de nuestro diccionario utilizando el método 
keys, de igual forma podremos obtener todos los valores el diccionario con le 
método values.
"""

diccionario = { 'Eduardo': 1, 'Fernando':2, 'Uriel':3, 'Rafael': 4}
print(diccionario.keys())
print(diccionario.values())

#Ejercicio 7
Diccionario = {
    "Nombre":"Sixto Manuel", 
    "Apellido":"García Romero", 
    "Cedula":72153890, 
    "Dirección":"calle 50 carrera 20", 
    "Telefono":3197138795, 
    "Titulo":"Ingeniero", 
    "Ciudad":"Barranquilla", 
    "Trabajo":"independiente"
    }

print("cantidad de datos: ", len(Diccionario), "\n")
print(Diccionario, "\n")
print(Diccionario.keys(), "\n")
print(Diccionario.values(), "\n")

#Ejercicio 7

datos = {'id':'87689s87d6', 
'nombre':'Andres', 
'apellido':'Pizarro', 
'email':'andres.pizarro@hotmail.com', 
'telefono':3135555555, 
'direccion':'calle 98', 
'ciudad':'Pereira', 
'departamento':'Risaralda', 
'pais':'Colombia'}

print(f'Numero de datos: {len(datos)}')

for k in datos.keys():
    print(f'{k} = {datos[k]}')

#Ejercicio 7

print('======================')
print()

datos = dict(id = '87689s87d6', nombre = 'Mauricio', apellido = 'Posada', email = 'maopos@micorreo.com', telefono = 78576588765, github = '@maopos', instagram = '@maoposites', direccion = 'calle 5 carrera 20b', ciudad = 'cali', departamento = 'Valle', pais = 'Colombia')

print('Cantidad de datos: ', len(datos))
print(datos)
print()
print(datos.keys())
print()
print(datos.values())
print()



print()
print('======================')

#Ejemplo 8

diccionario = {
     "clave1":234,
     "clave2":True,
     "clave3":"Eduardo_gpg",
}

print(diccionario)
print(type(diccionario))
print(diccionario['clave1'])
print(type(diccionario['clave1']))
print(diccionario['clave2'])
print(type(diccionario['clave2']))
print(diccionario['clave3'])
print(type(diccionario['clave3']))

#Ejemplo 9

"""
Acceder a valor de clave
Esta operación le permite acceder a un valor especifico del diccionario 
mediante su clave.
"""

diccionario = dict(python = 2.7, zope = 2.13, plone = '+57 326.214.5698', django = 2.1)

print(diccionario['zope'])

#Ejemplo 10

"""
clear()
Este método remueve todos los elementos desde el diccionario.
"""

diccionario = dict(python = 2.7, zope = 2.13, plone = '+57 326.214.5698', django = 2.1)
print(diccionario)

diccionario.clear()
print(diccionario)

#Ejemplo 11
"""
copy()
Este método devuelve una copia superficial del tipo diccionario
"""

diccionario = dict(python = 2.7, zope = 2.13, plone = '+57 326.214.5698', django = 2.1)
print('Variable versiones     ', diccionario)

nuevaVersion = diccionario.copy()
print('Variable otro_versiones', nuevaVersion)

#Ejemplo 12
"""
fromkeys()
Este método crea un nuevo diccionario con claves a partir de un tipo 
de dato secuencia. El valor de value por defecto es el tipo None.
"""

lista = ('python', 'zope', 'plone')
versiones = dict.fromkeys(lista)
print("Nuevo Diccionario : %s" %  str(versiones))

"""
En el ejemplo anterior inicializa los valores de cada clave a 
None, mas puede inicializar un valor común por defecto para cada clave:
"""

versiones = dict.fromkeys(lista, 0.1)
print("Nuevo Diccionario : %s" %  str(versiones))

#Ejemplo 13

"""
get()
Este método devuelve el valor en base a una coincidencia de búsqueda en
un diccionario mediante una clave, de lo contrario devuelve el objeto None.
"""

diccionario = dict(python = 2.7, zope = 2.13, plone = '+57 326.214.5698', django = 2.1)
print(diccionario.get('plone'))
print(diccionario.get('python'))


#Ejemplo 14

"""
items()
Este método devuelve una lista de pares de diccionarios (clave, valor), 
como 2 tuplas 
"""

diccionario = dict(python = 2.7, zope = 2.13, plone = '+57 326.214.5698', django = 2.1)

print(diccionario.items())

#Ejemplo 15

"""
pop()
Este método remueve específicamente una clave de diccionario y 
devuelve valor correspondiente. Lanza una excepción KeyError si 
la clave no es encontrada.
"""

diccionario = dict(python = 2.7, zope = 2.13, plone = '+57 326.214.5698', django = 2.1)
print('Version original ', diccionario)

versiones.pop('zope')
print('Nueva version    ', diccionario)

#Ejemplo 16

"""
update()
Este método actualiza un diccionario agregando los pares clave-valores
en un segundo diccionario. Este método no devuelve nada.

El método update() toma un diccionario o un objeto iterable de pares 
clave/valor (generalmente tuplas). Si se llama a update() sin pasar 
parámetros, el diccionario permanece sin cambios.
"""

diccionarioOriginal = dict(python = 2.7, zope = 2.13, plone = '+57 326.214.5698')
print('Diccionario Original                ' ,diccionarioOriginal)

nuevoDiccionario = dict(django = 2.1)
print('Nuevo Diccionario - complemento     ' , nuevoDiccionario)

diccionarioOriginal.update(nuevoDiccionario)
print('Diccionario Actualizado             ' , diccionarioOriginal)

#Ejercicio 17
#Mauricio

print('======================\n')

producto_1 = dict(id = 123, marca = 'Apple', procesador = 'M1', memoria = '(8Gb', pantalla = '13"')

producto_2 = dict(id2 = 124, marca2 = 'Samsung', procesador2 = 'Intel core i7', memoria2 = '(16Gb', pantalla2 = '14"')

print('Producto 1:      ', producto_1)
print()
print('Producto 2:      ', producto_2)
print()

producto_1.update(producto_2)

print('Stock:           ', producto_1)

print('\n======================')

#Ejercicio 18
#Andres

datos = {
'nombre':'Andres', 
'apellido':'Pizarro',
'cc':'9862000', 
'email':'andres.pizarro@hotmail.com', 
'telefono':3135555555, 
'direccion':'calle 98', 
'ciudad':'Pereira', 
'departamento':'Risaralda', 
'pais':'Colombia'}

print(f'Numero de datos: {len(datos)}')

i:int =1
for k in datos.keys():
    print(f'Dato_{i}...{k}={datos[k]}')
    i+=1

print('\n')

print(f'Agregamos Información Adicional:')

datos_add = {
    'cuenta_ahorros':270819629,
    'banco':'Bancolombia',
    'Recibe_Transferencias':True,
    'Saldo':100000000000
}

datos.update(datos_add)

print('\n')

print(f'Nuevo Numero de Datos: {len(datos)}')

i = 1
for k,v in datos.items():
    print(f'Dato_{i}...{k}={v}')
    i+=1


#Ejemplo 19

"""
Funciones
Los objetos de tipo diccionario tienen disponibles una serie de funciones
integradas en el interprete Python para su tratamiento, a continuación 
algunas de estas:

len()
Esta función devuelve un valor entero con el número de claves de un
diccinario especificado en su parametro.
"""

diccionarioOriginal = dict(python = 2.7, zope = 2.13, plone = '+57 326.214.5698')

print(len(diccionarioOriginal))

#Ejemplo 20

"""
El método keys() y sorted()
El método retorna o regresa una lista de todas las claves dentro del diccionario.
Al tener una lista de claves se puede acceder a todo el diccionario de una manera 
fácil y útil.
"""

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in sorted(dict.keys()):
    print(key, "->", dict[key])

#Ejercicio 21

print('======================')
print()

animales = {'gato': 'chat', 'perro': 'chien', 'caballo': 'cheval', 'gallina': 'chaki', 'raton': 'choin'}

for i in sorted(animales.keys()):
    print(f'{i}: {animales[i]}')

print()
print('======================')

print('======================')
print()


animales = {'gato': 'chat', 'perro': 'chien', 'caballo': 'cheval', 'gallina': 'chaki', 'raton': 'choin'}

for i in sorted(animales.keys()):
    print(f'{i}:', animales[i])

print()
print('======================')

#Ejercicio 22

animals = {
    'chicken':'pio',
    'vaca':'mu',
    'perro':'guau',
    'gato':'miau',
    'loro':'quiere cacao'
}

for (animal,sonido) in animals.items():
    print(f'El {animal} dice {sonido}')

#Ejercicio 23

"""
Métodos item()
Este método regresa una lista de tuplas donde cada tupla es un par de cada clave 
con su valor.
"""

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dict.items():
    print(spanish, "->", french)


#Ejercicio 24

"""
Sentencias
Los objetos de tipo diccionario tienen disponibles una serie de sentencias 
integradas en el interprete Python para su tratamiento, a continuación 
algunas de estas:

del
Esta sentencia es la misma sentencia integrada del en el interprete Python 
pero aplicada al uso de la secuencia de tipo diccionario.
"""

diccionario = dict(python = 2.7, zope = 2.13, plone = '+57 326.214.5698', django = 2.1)
print('Version original                ', diccionarioOriginal)

del diccionarioOriginal['django']
print('Luego de borrar la clave django ', diccionarioOriginal)

#Ejercicio 25

#Tenemos el los siguientes diccionarios

Informacion = {
    'Alumno1': {'nombre':'Daniel', 'edad':11, 'estatura':1.75, 'grado':'Master'},
    'Alumno2':{'nombre':'David', 'edad':32, 'estatura':1.85, 'grado':'Doctor'}   
    }

print(Informacion)

#Comparemos los nombres de los estudiantes

if Informacion['Alumno1']['nombre'] == Informacion['Alumno2']['nombre']:
    print("Los nombres son iguales")
else:
    print('Los nombres son diferentes')

#Miremos quien es mayor

if Informacion['Alumno1']['edad'] > Informacion['Alumno2']['edad']:
    print(str(Informacion['Alumno1']['nombre']) + ' es mayor') 
    mayor = {'nombremayor':Informacion['Alumno1']['nombre'], 'edadmayor':Informacion['Alumno1']['edad'] }
    
elif Informacion['Alumno1']['edad'] < Informacion['Alumno2']['edad']:
    print(str(Informacion['Alumno1']['nombre']) + ' es menor') 
    mayor = {'nombremayor':Informacion['Alumno2']['nombre'], 'edadmayor':Informacion['Alumno2']['edad'] }

print(mayor)


#Ejercicio 26

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'leon', 'caballo']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "no está en el diccionario")

#Ejemplo 27

"""
Agregando nuevas claves
El agregar una nueva clave con su valor a un diccionario es tan simple como cambiar un valor. 
Solo se tiene que asignar un valor a una nueva clave que no haya existido antes.
"""

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict['cisne'] = 'cygne'
print(dict)

#También es posible insertar un elemento al diccionario utilizando el método update()

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict.update({"pato" : "canard"})
print(dict)

#Ejemplo 28

"""
Eliminado claves
Al eliminar la clave también se removerá el valor asociado. Los valores no pueden 
existir sin sus claves. Esto se logra con la instrucción del.
"""
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
print('Diccionario original ', dict)

del dict['perro']

print('Nuevo diccionario    ', dict)
