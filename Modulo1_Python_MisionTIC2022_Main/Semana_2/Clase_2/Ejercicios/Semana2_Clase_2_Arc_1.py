#Ejercicio 1
fruta = 'fresa'
letra = fruta[1]
print(letra)

fruta = 'banana'
letra = fruta[0]
print(letra)

#Ejercicio 2
fruta = 'banana'
print(len(fruta))

#Ejercicio 3
fruta = 'banana'
longitud = len(fruta)
ultimo = fruta[longitud - 1]
print(ultimo)

#Ejercicio 4
s = 'Monty Python'
print(s[0:5])
print(s[6:12])

#Ejercicio 5
fruta = 'banana'
print(fruta[:3])
print(fruta[3:])

#Ejercicio 6
fruta = 'banana'
print(fruta[3:3])

#Ejercicio 7
saludo = '¡Hola, mundo!'
nuevo_saludo = 'J' + saludo[1:]
print(nuevo_saludo)

#Ejercicio 8
var1 = 'a'
var2 = 'banana'
print(var1 in var2)

var1 = 'ola'
var2 = 'banana'
print(var1 in var2)

#Ejercicio 9
palabra = 'banana'
if palabra == 'banana':
    print('Está bien, bananas')

#Ejercicio 10

palabra2 = 'pera'

if palabra2 < 'banana':
    print('Tu palabra ' + palabra2 + ', viene antes de banana')
elif palabra2 > 'banana':
    print('Tu palabra ' + palabra2 + ', viene después de banana.')
else:
    print('Está bien, su palabra es banana')

#Ejercicio 11
Cadena = 'Hola mundo'
print(type(Cadena))
print(dir(Cadena))

#Ejercicio 12
palabra = 'banana'
palabra_nueva = palabra.upper()
print(palabra_nueva)

#Ejercicio 13
palabra = 'banana'
index = palabra.find('a')
print(index)

#Ejercicio 14

palabra = 'banana'
print(palabra.find('na'))

#Ejercicio 15

palabra = 'banana'
print(palabra.find('na', 3))

#Ejercicio 16

linea = '    Aquí vamos    '
print(linea.strip())

#Ejercicio 17

linea = 'Que Tengas Un Buen Día'
print(linea.startswith('Que'))
print(linea.startswith('q'))

#Ejercicio 18

linea = 'Que Tengas Un Buen Día'
print(linea.startswith('t'))
print(linea.lower().startswith('q'))
print(linea.lower()) #que tengas un buen día

#Ejercicio 19

"""
Pieza de código que permite cortar el host del correo electrónico e imprimirlo luego
"""

#Consigue la @
data = 'De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
enlaposicion = data.find('@') # Devuelve la posición de la '@'
print(enlaposicion) # Imprime un valor entero
#Consigue el espacio luego de uct.ac.za
espacioenlaposicion = data.find(' ',enlaposicion) #Consigue el espacio en blanco luego de la '@'
print(espacioenlaposicion) #Imprime el valor
#Corta el fragmento localizado previamente
host = data[enlaposicion+1:espacioenlaposicion] #Corta el fagmento del host del correo y elimina el resto
print(host) #Solo imprime el host del correo


# ***** OPERADOR FORMATO *****

#Ejercicio 20
# %s cadena
# %d números

nombre = 'Margot'
numero = 42
print ('%s %d' % (nombre, numero))

saludo = 'Hola'
print('%s, Luis' % (saludo))

camellos = 42
print('He visto %d camellos' % camellos)

#Ejercicio 21
# Saldrán dos líneas en pantalla, una con Hola, la otra con Mundo

cadena = "Hola\nMundo"
print(cadena)

#Ejercicio 22

cadena = "un uno, un dos, un tres"
# Saca 4, hay 4 "un" en cadena.
print (cadena.count("un")) 
# Saca 1, hay 1 "un" a partir de la posición 10 de cadena.
print (cadena.count("un",10)) 
# Saca 3, hay 3 "un" entre la posición 0 y la 10.
print (cadena.count("un",0,10)) 

cadena = "un uno, un dos, un tres"
# saca por pantalla "XXX XXXo, XXX dos, XXX tres"
print (cadena.replace("un", "XXX")) 
# Sólo reemplaza 2 "un", así que saca por pantalla "XXX XXXo, un dos, un tres"
print (cadena.replace("un", "XXX", 2)) 


#Ejercicio 22

var1 = 10
var2 = 15
suma = var1 + var2

print("El valor es {}".format(12))                          #El valor es 12
print("El valor es {}".format(12.3456))                     #El valor es 12.3456
print("Los valores son {}, {} y {}".format(1,2,3))          #Los valores son 1, 2 y 3
print("Los valores son {2}, {1} y {0}".format(1,2,3))       #Los valores son 3, 2 y 1
print("{pepe} y {juan}".format(juan=1, pepe=2))             #2 y 1
print('La suma de {} + {} es {}'.format(var1,var2,suma))    #La suma de 10 + 15 es 25
print('La suma de {0} + {1} es {2}'.format(var1,var2,suma)) #La suma de 10 + 15 es 25

#Ejercicio 23

mensaje1 = 'Hola' + ' ' + 'Luis' + ' ' +'Guillermo' + ' ' + 'Molero' + ' ' + 'Suarez'
print(mensaje1)

#Ejercicio 24

msg1 = 'Hola ' * 3
msg2 = 'Luis' + ' ' + 'Guillermo' + ' Molero'  + ' Suarez'
print(msg1 + msg2)

#Ejercicio 25

msg = 'Hola'
msg += ' '
msg += 'Luis'
msg += ' ' + 'Guillermo' + ' Molero' + ' ' + 'Suarez'
print(msg)

