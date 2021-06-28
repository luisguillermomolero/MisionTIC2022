#Desarrollado por: Ivan Cendales
class Estudiante:
    def __init__(self):
        self.nombre=input("Ingrese el nombre del estudiante:")
        self.nota1=float(input("Favor ingrese la nota 1 (de cero a cinco):"))
        self.nota2=float(input("Favor ingrese la nota 2 (de cero a cinco):"))
        self.notaFinal = (self.nota1 + self.nota2)/2
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota final",self.notaFinal)
    def aprobacion(self):
        if self.notaFinal>=3:
            print("Aprobo la materia")
        else:
            print("No aprobó la materia")

estudiante1 = Estudiante()
estudiante1.imprimir()
estudiante1.aprobacion()