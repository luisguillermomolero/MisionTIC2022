#Programa que permite validar si un empleado debe pagar o no impuesto de acuerdo a su ingreso mensual
class Empleado:

    #Definimos el método inicial (constructor)
    def __init__(self): # self inicializa los atributos de la instancia que se está inicializando
        self.nombre = input("Ingrese el nombre del empleado:")    #Atributo, porpiedad o caracteristica de la Clase "Empleado"
        self.sueldo = float(input("Ingrese el sueldo:"))          #Atributo, propiedad o caracteristica de la Clase "Empleado"

    def imprimir(self):      #Comportamiento, funcionalidad, método
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):   #Comportamiento, funcionalidad, método
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

# bloque principal

"""
Miembros de una Clase: Las clases también son denominadas tipos abstractos de datos. 
Cada clase contiene datos, así como un conjunto de funciones que manipulan estos datos. 
A los datos que componen una clase se les llama datos miembro. A las funciones que 
componen una clase se les llama funciones miembro(o métodos)
"""
empleado1 = Empleado()  #Instancia, declarar la variable "empleado1" como tipo "clase".
empleado1.imprimir()
empleado1.paga_impuestos()

"""
class car:

    def __init__(self, model, color):

        self.model = model
        self.color = color

mycar = car('model XYZ','red')  # Instanciando la clase car()
print(mycar.model)              #Imprimir el atributo "model" del objeto "car"
print(mycar.color)              #Imprimir el atributo "model" del objeto "car"
"""