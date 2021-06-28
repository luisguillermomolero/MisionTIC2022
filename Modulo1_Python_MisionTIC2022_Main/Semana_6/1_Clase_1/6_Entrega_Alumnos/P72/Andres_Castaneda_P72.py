#Codigo:

class Mascota:

    # definimos el metodo inicial(constructor)
    def __init__(self):  # self inicializa los atributos de la instancia que se esta inicializando
        # atributo, propiedad, o caracteristica de la clase "Empleado"
        self.id = input("Ingrese ID de la Mascota: ")
        self.datos = input("Ingrese Nombre y Apellido de la Mascota: ")
        # atributo, propiedad, o caracteristica de la clase "Empleado"
        self.peso = float(input("Ingrese Peso Mascota: "))

    def imprimir(self):  # comportamiento, funcionalidad, metodo
        print("id", self.id)
        print("Peso", self.peso)

    def pasa_peso(self):
        if self.peso > 5 and self.peso <= 25:
            print("Felicitaciones Peso ideal Raza Pequeña")
        elif self.peso <= 4:
            print("No corresponde a Razas pequeñas :( ")
        elif self.peso > 26:
            print("Valor no admitido")


Mascota1 = Mascota()  # instancia, declarar la variable "Mascota1" como tipo "clase"
Mascota1.imprimir()
Mascota1.pasa_peso()
