#Ejercicio 1

x = 0
x = x + 1
x += 1
print(x)

#Ejercicio 2

y = 10
y = y-1
y -= 9

print(y) #imprimir y

#Ejercicio 3

n = int(input('Por favor, ingrese un número mayor que cero '))

while n > 0:
    print(n)
    n = n - 1
print('Despegue!')

#Ejercicio 4
def factorial(n: int) -> int:
    resultado = 1
    numero_actual = 2
    while numero_actual <= n:
        resultado = resultado * numero_actual
        numero_actual += 1
    return resultado

#Ejercicio 5
#Alejarse de terminación

i = 1

while i > 0:
    print(i)
    i += 1
print("Terminé")

#Ejercicio 6
#Brincarse la meta
# le toca oprimir el boton de pausa sino el sigue dandole

i = 0

while i != 10:
    print(i)
    i += 2
print("Terminé")

#Ejercicio 7
#Problemas de indentación

i = 1
while i < 10:
    print(i)
i = i + 1
print("Terminé") #aqui tambien le toca hacer lo mismo


#Ejercicio 8
#Olvidar el avance
i = 1
while i < 10:
    print(i)
print("Terminé")

#Ejercicio 9
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Ejercicio 10

i = 0

while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#Ejercicio 11
#Mostrar los primeros 5 números impares saltando el cuarto valor (mostrando solo 4 de ellos)


n = -1

while n != 9:
    n=n+2
    if n==7:
        continue
    print(n)
#Para los impares

#Ejercicio 12
#Mostrar los primeros 5 números impares saltando el cuarto valor (mostrando solo 4 de ellos)


i=0
impar=1
while i < 5:
	
	impar=impar+2
	i=i+1
	if i == 4:
		continue
	
	print(impar)

#Ejercicio 13
#Mostrar los primeros 5 números impares saltando el cuarto valor (mostrando solo 4 de ellos)

variable = -1

while variable < 9:
    variable = variable +2
    if variable == 7:
        continue
    print('Actual valor de variable:', variable) # no imprime el 5

#Ejercicio 14
#Mostrar los primeros 5 números impares saltando el cuarto valor (mostrando solo 4 de ellos)

i=0
num=0
while i < 10:
    i+=1
    if i==7:
        continue
    if i%2!=0:
        num=i
        print("impares",num)


#Ejercicio 15
#Bucle 'while' con 'else'

i = 1

while i < 6:
  print(i)
  i += 1
else:
  print("i no es mayor o igual de 6")

#Ejercicio 16
#Bucle 'while' 
# Bucle 'while' controlado por Evento

acumuladorNotas = promedioNotas = contadorNotas = 0

calificacion = int(input("Introduzca la nota de un estudiante (-1 para salir): "))

while calificacion != -1:               #Ejecutará el While mientras no se introduzca el número -1
    acumuladorNotas += calificacion     #Acumulador de notas
    contadorNotas += 1                  #Contador de notas
    calificacion = int(input("Introduzca la nota de un estudiante (-1 para salir): "))
    promedioNotas = acumuladorNotas / contadorNotas #Calcula el promedio de notas
print ("Promedio de notas del grado escolar es: " + str(promedioNotas)) #Imprime promedio de notas
    
#Ejercicio 17
#Bucle 'while' con 'else'

acumuladorNotas = promedioNotas = contadorNotas = 0

calificacion = int(input("Introduzca la nota de un estudiante (-1 para salir): "))

while calificacion != -1:               #Ejecutará el While mientras no se introduzca el número -1
    acumuladorNotas += calificacion     #Acumulador de notas
    contadorNotas += 1                  #Contador de notas
    calificacion = int(input("Introduzca la nota de un estudiante (-1 para salir): "))
else:
    if acumuladorNotas != 0:
        promedioNotas = acumuladorNotas / contadorNotas #Calcula el promedio de notas
        print ("Promedio de notas del grado escolar es: " + str(promedioNotas)) #Imprime promedio de notas
    else:
        print('No existen calificaciones')

#Ejercicio 18
#Ciclo While c/Sentencia break
variable = 10

while variable > 0:
    print('Actual valor de variable:', variable)
    variable = variable -1
    if variable == 5:
        break

#Ejercicio 19
# Ciclo While c/Sentencia continue
variable = 10

while variable > 0:
    variable = variable -1
    if variable == 5:
        continue
    print('Actual valor de variable:', variable) # no imprime el 5

#Ejercicio 20
#Ciclo For

for x in range(0, 4):
    print("Estamos en la iteración " + str(x))

#Ejericio 21
for j in range(0, 10, 2):
    print("Estamos en la iteración " + str(j))

#Ejercicio 22
for j in range(10, 0, -2):
    print("Estamos en la iteración " + str(j))


#Ejercicio 23
oracion = 'Mary entiende muy bien Python'
frases = oracion.split() # convierte a una lista cada palabra
print("La oración analizada es:", oracion, ".\n")

for palabra in range(len(frases)):
    print("Palabra: {0}, en la frase su posición es: {1}".format(frases[palabra], palabra))

#Ejercicio 24
# Bucle 'for' con Diccionarios
datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}

clave = datos_basicos.keys()
valor = datos_basicos.values()

cantidad_datos = datos_basicos.items()

for clave, valor in cantidad_datos:
    print(clave + ": " + valor)

#Ejercicio 25
# Bucle 'for' con Diccionarios
frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
for nombre, color in frutas.items():
    print(nombre, "es de color", color)


#Ejercicio 26
#Ejemplo dos con diccionarios

frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
for llave in frutas:
    print(llave, 'es de color', frutas[llave])


#Ejercicio 27
#Bucle 'for' con 'else'

"""
La cláusula else se ejecuta después de que el ciclo se completa normalmente. 
Esto significa que el bucle no encontró una declaración de interrupción. 
Son realmente útiles una vez que sabes dónde usarlos.
La construcción común es ejecutar un bucle y buscar un elemento. Si se encuentra
el elemento, salimos del ciclo usando la declaración break. Hay dos escenarios en
los que el ciclo puede terminar. El primero es cuando se encuentra el artículo y 
se produce una rotura. El segundo escenario es que el ciclo termina sin encontrar 
una declaración de interrupción. 
"""

#range(start, stop, step)


"""
Números primos
Número natural mayor que 1 que tiene únicamente dos divisores positivos distintos: 
 *** él mismo y la unidad (1).
"""

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'es igual a ', x, '*', round(n/x))
            break
    else:
        # bucle falló sin encontrar un factor
        print(n, 'es un número primo')

#Ejemplo 28

db_connection = "127.0.0.1","5432","root","nomina"

for parametro in db_connection:
    print(parametro)
else:
    print("""El comando PostgreSQL es: 
$ psql -h {server} -p {port} -U {user} -d {db_name}""".format(
        server=db_connection[0], port=db_connection[1], 
        user=db_connection[2], db_name=db_connection[3]))

#Ejemplo 29

for x in range(6):
      print(x)
else:
  print("Finalmente, finalizó")