#Desarrollado por: Jose Navia
# Programa que permite saber si una persona es apta pora votar.
class Votante:
    #Definimos el método inicial (constructor)
    def __init__(self): # self inicializa los atributos de la instancia que se está inicializando
        self.nombre=input("Ingrese el nombre completo de la persona: ")    #Atributo, porpiedad o caracteristica de la Clase "Votante"
        self.nacimiento=int(input("Ingrese el año completo de su nacimiento: "))          
        self.cedula=int(input('Ingrese su número de cédula: '))
        self.genero=input("Para hombre digite \"H\", mujer digite \"M\" y otro digite \"O\": ")    
        self.ciudad=input("Cuál es su ciudad de domicilio: ")         
    def imprimir(self):      #Comportamiento, funcionalidad, método
        print("Nombre:",self.nombre, "Género: ", self.genero)
        print("Cédula:",self.cedula)
        print("Edad:",2021-(self.nacimiento))
        print("Procedente de: ", self.ciudad)
    def votacion(self):   #Comportamiento, funcionalidad, método
        if 2021 - self.nacimiento > 18:
            print("Persona de género", self.genero, "que es apta para votar en la ciudad de ", self.ciudad)
        else:
            print("Persona menor de edad que no tiene la edad para votar")

votante1= Votante()
votante1.imprimir()
votante1.votacion()
