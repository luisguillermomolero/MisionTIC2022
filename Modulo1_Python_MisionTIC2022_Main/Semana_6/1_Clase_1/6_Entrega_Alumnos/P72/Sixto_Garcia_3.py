#Desarrollado por: Sixto Garcia
#Programa para clasificar los elementos de un almacen. 
# Contiene:4 métodos + el constructor, 5 atributos, enunciado es libre

class almacen:
     #Definimos el método inicial (constructor)           
    def __init__(self):  # self inicializa los atributos de la instancia que se está inicializando

        self.nombre = input("Ingrese el elemento: ")    # Atributo, porpiedad o caracteristica de la Clase "almacen"
        self.precio = int(input("Ingrese el precio del elemento: ")) # Atributo, propiedad o caracteristica de la Clase "almacen"
        self.marca = input("Marca del elemento: ")    # Atributo, porpiedad o caracteristica de la Clase "almacen"
        self.modelo = input("Modelo del elemento :")    # Atributo, porpiedad o caracteristica de la Clase "almacen"
        self.cantidad = input("Ingrese la cantidad de elementos: ")    # Atributo, porpiedad o caracteristica de la Clase "almacen"


    def imprimir(self):      #Comportamiento, funcionalidad, método
        print("Nombre:",self.nombre)
        print("precio:",self.precio)
        print("marca:",self.marca)
        print("modelo:",self.modelo)        
        print("cantidad:",self.cantidad)

    def Inventario(self):   #Comportamiento, funcionalidad, método
        if self.cantidad > 100 :
            print("No se require mas compras de este elemento")
        else:
            if self.cantidad < 20:
                print("Stock de seguridad, se recomienda hacer nuevo pedido de este elemento")

    def modelos(self):
       print(f'El moledo del elemento {self.nombre} es: {self.modelo} y su marca es: {self.marca} ')

    def estado_elemento(self):
        print('los elementos se encuentran en buen estado estado')

    def precio_elemento(self):
        if self.precio > 500:
            print(f'El Valor del elemento {self.nombre} es: {self.precio} se recomienda no comprar. ')
        else:
            if self.precio < 500:
                print(f'El Valor del elemento {self.nombre} es: {self.precio} se recomienda comprar maximo 80. ')


elemento = almacen()  #Instancia, declarar la variable "empleado1" como tipo "clase".
elemento.modelos()
elemento.precio_elemento()