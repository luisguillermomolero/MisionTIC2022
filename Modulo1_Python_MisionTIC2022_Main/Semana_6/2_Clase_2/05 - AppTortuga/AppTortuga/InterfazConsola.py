#Librería de interacción (interfaces)
#####################################

#Mensaje de apertura por consola
def mensajeBienvenida():
    print("----------------------------")
    print("Bienvenido a la aplicación")
    print("----------------------------")

#Mensaje de cierre por consola    
def mensajeDespedida():
    print("----------------------------")
    print("Cierre exitoso, hasta luego")
    print("----------------------------")

#Presentar mensaje genérico en pantalla
def mensaje(info=''):
    print()
    print(info)
    print()

#Formulario menú rutinas tortuga
def formularioMenuAppTortuga():
    print(" ")
    print("-- Aplicación Tortuga (Comportamiento de Objetos) ---")
    print("1. Dibujado Líneas Discontinuas")
    print("2. Polígono Irregular de 4 Lados sin Relleno")
    print("3. Polígono Irregular de 4 Lados con Relleno")
    print("4. Polilínea Ingresando Coordenadas")    
    print("5. Salir")

    #Capturar la opción validando el tipo de dato para retornarlo al controlador
    opcion = None
    while opcion == None:
        try:
            opcion = int(input("Elija una rutina: "))
        except:        
            print("Entrada inválida: Se debe ingresar una opción numérica.")    

    #Retornar opción al controlador
    return opcion
    
#Recolección de las coordenadas
def recogerCoordenadasTeclado():
    return int(input("Ingrese x: ")), int(input("Ingrese y: "))
    
#Recoger por teclado criterio de parada y retornar estado 
#(True -> Continuar, False -> Detenerse)
def controlParada():    
    estado = True
    if input("Desea salir? (s): ").lower() == 's':
        estado = False
    return estado
