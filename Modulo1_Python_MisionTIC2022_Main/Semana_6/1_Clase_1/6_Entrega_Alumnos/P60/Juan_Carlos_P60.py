#Desarrollado por: Juan Carlos Cañón Sossa
class Automovil:
    def __init__(self):
        self.Marca=input("Ingrese la marca del Automovil: ")
        self.cilindraje=input("Ingrese el cilindraje: ")
        self.color=input("Ingrese el color: ")
        self.puertas=input("Ingrese el número de puertas: ")
    def imprimir(self):
        print(f"los datos ingresados son: Marca: ", self.Marca + "    cilidraje  ", self.cilindraje + "   color  ", self.color + "   Número de puertas  ", self.puertas)
    def tipo_vehiculo (self):
        if self.puertas =="2":
            print("Su auto es un Coupe de color: ", self.color)
        else:
            print("Su auto es un Sedán de color: ", self.color)
empleado1 = Automovil() 
empleado1.imprimir()
empleado1.tipo_vehiculo()
        
