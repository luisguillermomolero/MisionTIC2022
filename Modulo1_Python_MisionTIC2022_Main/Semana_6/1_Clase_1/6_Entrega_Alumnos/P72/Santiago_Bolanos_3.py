#Elaborado por Santiago Bolaños
# Programa que permite validar si cumple con la meta diaria de recorrido en bicicleta y kcalorias quemadas

class ejercicio:

    #Definimos el método inicial (constructor)
    def __init__(self): # self inicializa los atributos de la instancia que se está inicializando
        self.nombre = input("Ingrese el nombre del deportista: ")    #Atributo, propiedad o caracteristica de la Clase "Ejercicio"
        self.distancia = float(input("Ingrese los km recorridos: "))        #Atributo, propiedad o caracteristica de la Clase "Ejercicio"
        self.peso= float(input("Ingrese el peso del deportista: "))
        self.velocidad= input("Ingrese velocidad promedio: ")
        self.tiporecorrido= input("Escriba montaña o carretera: ")  

    def imprimir(self):      #Comportamiento, funcionalidad, método
        print("Nombre:",self.nombre)
        print("Distancia:",self.distancia)

    def cumplemeta(self):   #Comportamiento, funcionalidad, método
        if self.distancia>80:
            print("Cumple con la meta")
        else:
            print("No cumple con la meta")

    def calorias(self):
        if self.peso<=60:
            c=self.peso*932
            print("El deportista quemó: ", {c}, "kilocalorias")
        else:
            c=self.peso*1088
            print("El deportista quemó: ", {c}, "kilocalorias")
    def aceleracion(self):
        ace=9,8*self.velocidad
        print("La acelaración promedio fue de", {ace},"m/s2")



ejercicio1 = ejercicio()  #Instancia, declarar la variable "ejercicio1" como tipo "clase".
ejercicio1.imprimir()
ejercicio1.cumplemeta()
ejercicio1.calorias()
ejercicio1.aceleracion()
