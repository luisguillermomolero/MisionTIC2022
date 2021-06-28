"""
Decisiones Generalizadas
Any, All y Aplicaciones


Introducción
• Hemos visto una parte del paradigma de programación funcional en Python, el cual
puede ser fácilmente mezclado con paradigmas imperativos, aprovechando la
disminución de los cambios de estados de las variables.
• Así como se pueden generalizar los cómputos para contenedores, también es
posible la generalización de decisiones.
• Any y All nos permiten coleccionar sentencias declarativas o valores de verdad para
tomar una decisión.
• En estas diapositivas se presentan ejemplos que encadenan conceptos vistos de
funcional con las funciones Any y All.


All y Any
• Las funciones all y any se aplican sobre un iterable (una estructura que podamos
recorrer de forma iterativa, como una lista o un conjunto) 

Devuelven True si todos los elementos son True (en el caso de la función all) 
Devuelve False si algún elemento es True (en el caso de la función any), 
devolviéndose False en cualquier otra circunstancia.

"""

#Un caso especial se produce cuando el iterable en cuestión está vacío (cuando no
# tiene ningún elemento). En esta caso la función all devuelve True y la función any
# devuelve False:

print(all(list())) #True
print(any(list())) #False

#Ejemplo All, Any y Programación Funcional

"""
La empresa ABCD tiene hasta 100 empleados. La compañía decide crear un número
de identificación único UID para cada uno de sus empleados. La compañía le ha
asignado la tarea de validar los UIDs generados aleatoriamente. Un UID válido debe
cumplir con las siguientes reglas:
• Debe contener por lo menos dos letras mayúsculas en el alfabeto inglés.
• Debe tener por lo menos 3 dígitos.
• Contener únicamente dígitos alfanuméricos.
• No tener repeticiones.
• Contener exactamente 10 caracteres.
"""

# Aquí todos los iterables son verdaderos, así que todos
# devolverá True y se imprimirá lo mismo
print (all([True, True, True, True]))
  
# Aquí el método provocará un cortocircuito en el
# primer elemento (Falso) y devolverá False.
print (all([False, True, True, False]))
  
# Esta declaración devolverá False, ya que no
# True se encuentra en los iterables
print (all([False, False, False]))

# Este código explica cómo podemos
# usar la funcion 'any' en la lista 
list1 = []
list2 = []
  
# El índice varía de 1 a 10 para multiplicar
for i in range(1,11):
    list1.append(4*i) 
  
# El índice para acceder a la lista 2 es de 0 a 9
for i in range(0,10):
    list2.append(list1[i]%5==0)
  
print('Vea si al menos un número es divisible por 5 en la lista 1 =>')
print(any(list2))



# Ilustración de la función 'all' en Python
  
# Toma dos listaslist1=[]
list1=[]
list2=[]
  
# Todos los números en list1 están en forma: 4 * i-3
for i  in range(1,21):
    list1.append(4*i-3)
  
# list2 almacena información de números impares en list1
for i in range(0,20):
    list2.append(list1[i]%2==1)
  
print('Vea si todos los números en list1 son impares =>')
print(all(list2))


print(any([2 == 2, 3 == 2]))
print(any([True, False, False]))
print(any([False, False]))


dict = {True : False, False: False}
print(any(dict))

#all

print(all([2 == 2, 3 == 2]))
print(all([2 > 1, 3 != 4]))
print(all([True, False, False]))
print(all([False, False]))

