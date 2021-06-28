class Estudiante:

    def __init__(self):
        self.nombre = input("Ingrese el nombre del estudiante:")
        self.apellido = input("Ingrese el apellido del estudiante:")
        self.nota1 = float(input("Ingrese la nota 1:"))  
        self.nota2 = float(input("Ingrese la nota 2:"))
        self.nota3 = float(input("Ingrese la nota 3:"))
        self.promedio = 0

    def imprimir(self):      
        print("Nombre:",self.nombre)
        print("Apellido:",self.apellido)
        print("Nota 1",self.nota1)
        print("Nota 2",self.nota1)
        print("Nota 3",self.nota1)
        
    def prome(self):
        self.promedio = (self.nota1 + self.nota2 + self.nota3)/3

    def promover_estudiante(self):   
        if self.promedio > 3:
            print("Aprobó la asignatura ")
        else:
            print("Reprobó la asignatura")


estudiante1 = Estudiante()  
estudiante1.imprimir()
estudiante1.prome()
estudiante1.promover_estudiante()
