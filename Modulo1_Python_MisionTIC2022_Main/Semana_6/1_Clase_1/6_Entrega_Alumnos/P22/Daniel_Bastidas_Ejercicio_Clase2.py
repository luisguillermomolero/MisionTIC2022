#Desarollado por: Daniel Bastidas
#Programa que permite calcular el area, perimetro y volumen de algunas formas geométricas

import math

class geometria:
    
    
    #Definimos el método inicial (constructor)
    def __init__(self): # self inicializa los atributos de la instancia que se está inicializando
        print("Calculadora de perimetro y area")
        self.radio = float(input("Ingrese el radio del circulo:"))#Atributo, propiedad o caracteristica de la Clase "Geometria"
        self.base = float(input("Ingrese el base del rectangulo:"))#Atributo, propiedad o caracteristica de la Clase "Geometria"
        self.altura = float(input("Ingrese la atura del rectangulo:")) #Atributo, propiedad o caracteristica de la Clase "Geometria"
        self.base2 = float(input("Ingrese el base del triangulo isósceles:"))#Atributo, propiedad o caracteristica de la Clase "Geometria"
        self.altura2 = float(input("Ingrese la atura del triangulo isósceles:"))#Atributo, propiedad o caracteristica de la Clase "Geometria"

    def imprimir(self):   #imprime los datos de entrada
        print("Radio del Circulo: ",self.radio)
        print("Base del rectangulo: ",self.base)
        print("Altura del rectangulo: ",self.altura)
        print("Base del triangulo: ",self.base2)
        print("Altura del triangulo: ",self.altura2)

    def area(self):   #esta definición calcula el area del circulo, rectangulo y triangulo
        areaCirculo = math.pi * self.radio**2
        print("El area del circulo es: "+ str(round(areaCirculo,2)))
        areaRectangulo= self.base*self.altura
        print("El area del cuadrado es: "+ str(round(areaRectangulo,2)))
        areaTriangulo= (self.base2*self.altura2)/2
        print("El area del triangulo es: "+ str(round(areaTriangulo,2)))

    def perimetro(self):  #esta definición calcula el perimetro del circulo, rectangulo y triangulo
        pCirculo = 2* math.pi * self.radio
        print("El perimetro del circulo es: "+ str(round(pCirculo,2)))
        pRectangulo= (self.base*2) + (self.altura*2)
        print("El perimetro del cuadrado es: "+ str(round(pRectangulo,2)))
        pTriangulo= (self.base2*2) + self.altura2
        print("El perimetro del triangulo es: "+ str(round(pTriangulo,2)))

    def volumenCirculo(self):  #esta definición calcula el volumen del circulo
        pCirculo = (4/3)* math.pi * self.radio**3
        print("El volumen del circulo es: "+ str(round(pCirculo,2)))


calcular = geometria()  #Instancia de la clase geometria.
calcular.imprimir()
calcular.area()
calcular.perimetro()
calcular.volumenCirculo()



class figura():
    def __init__(self):
        self.medida = "una figura puede tener un radio, baseo o altura"
    def mensaje(self):
        print(self.medida)

class circulo(figura):
    def __init__(self):
        self.radio = float(input("Ingrese el radio del circulo:"))
    def mensaje(self):
        print("Soy un circulo y mi radio es: "+ str(self.radio))

class rectangulo(figura):
    def __init__(self):
        self.base = float(input("Ingrese el base del rectangulo:"))
        self.altura = float(input("Ingrese la atura del rectangulo:")) 
    def mensaje(self):
        print("Soy un rectangulo mi base es: "+ str(self.base)+" y mi altura es: "+ str(self.altura))

class triangulo(figura):
    def __init__(self):
        self.base = float(input("Ingrese el base del triangulo:"))
        self.altura = float(input("Ingrese la atura del triangulo:"))
    def mensaje(self):
        print("Soy un triangulo mi base es: "+ str(self.base)+" y mi altura es: "+ str(self.altura))


fig = figura()
fig.mensaje()
cir = circulo()
cir.mensaje()
rec = rectangulo()
rec.mensaje()
tri = triangulo()
tri.mensaje()

