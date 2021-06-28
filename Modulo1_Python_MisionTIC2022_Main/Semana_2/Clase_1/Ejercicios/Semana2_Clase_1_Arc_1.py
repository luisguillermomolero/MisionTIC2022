#Ejemplo 1: División con divisor igual a cero

dividendo = 10
divisor = 0
try:
    cociente = dividendo / divisor
    print(cociente)
except:
    print ("No se permite la división por cero")


#Ejemplo 2: Conversión de Fahrenheit a celcius

temperatura_fahr = input('Introduzca una temperatura en Fahrenheit:')
try:
    fahr = float(temperatura_fahr)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('No ingreso ningún número, gracias')


#Ejemplo 3: Valor diferente a un número introducido por teclado

while True:
    try:
        x = int(input("Por favor, ingrese un número: "))
        print(x)
        break  # Si no da error, corta el while con break
    except ValueError:
        print("Eso no es un número, prueba otra vez...")


a = 25
b = 'dasdas'
try:
    resultado = a/b
    print('El resultado de ', a, ' entre ', b,' es: ', round(resultado,2))
except ZeroDivisionError:
    print("Error, division por cero.")
except TypeError:
    print("Error en el tipo de dato.")
finally:
    print("Gracias por usar el programa.")

