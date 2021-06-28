#Programa que permita validar si un estudiante aprobó o reprobó de acuerdo a su nota
class estudiante:

    #Definimos el método inicial (constructor)
    def __init__(self):                                             # self inicializa los atributos de la instancia que se está inicializando
        self.nombre=input("Ingrese el nombre del estudiante:")      #Atributo, porpiedad o caracteristica de la Clase "estudiante"
        self.nota=float(input("Ingrese la nota:"))                  #Atributo, propiedad o caracteristica de la Clase "estudiante"

    def imprimir(self):                                             #Comportamiento, funcionalidad, método
        print("Nombre:",self.nombre)
        print("nota:",self.nota)

    def aprobado(self):                                             #Comportamiento, funcionalidad, método
        if self.nota>3.0:
            print("Aprobado")
        else:
            print("Reprobado")
estudiante1 = estudiante()                                          #Instancia, declarar la variable "estudiante1" como tipo "clase".
estudiante1.imprimir()
estudiante1.aprobado()

