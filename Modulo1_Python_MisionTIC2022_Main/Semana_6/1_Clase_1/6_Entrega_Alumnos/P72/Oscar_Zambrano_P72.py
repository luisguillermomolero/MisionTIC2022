class Estudiante:

    # definimos el metodo inicial(constructor)
    def __init__(self):  # self inicializa los atributos de la instancia que se esta inicializando
        # atributo, propiedad, o caracteristica de la clase "Empleado"
        self.id = input("Ingrese ID del estudiante: ")
        self.datos = input("Ingrese Nombre y Apeliido del Estudiante: ")
        # atributo, propiedad, o caracteristica de la clase "Empleado"
        self.nota = float(input("Ingrese la nota del estudiante: "))

    def imprimir(self):  # comportamiento, funcionalidad, metodo
        print("id", self.id)
        print("nota", self.nota)

    def pasa_materia(self):
        if self.nota > 3 and self.nota <= 5:
            print("Felicitaciones")
        elif self.nota <= 3:
            print("Estudie mas por favor :( ")
        elif self.nota > 5:
            print("Valor no admitido")


alumno = Estudiante()  # instancia, declarar la variable "empleado1" como tipo "clase"
alumno.imprimir()
alumno.pasa_materia()
