#Desarollado por: Sergio Doncel
#Programa que identifica si un cuadrilatero es cuadrado o rectangulo
class cuadrilateros:
    def __init__(self): 
        self.base=input("Ingrese la base del cuadrilatero:")    
        self.altura=input("Ingrese la altura del cuadrilatero:")
               
    def imprimir(self):     
        print("Base:",self.base, "  cm")
        print("Altura:",self.altura, "   cm")
        

    def tipo(self):
        if self.base == self.altura:            
            print("El cuadrilatero es un cuadrado")

        else:
            print("El cuadrilatero es un rectangulo")

cuadrilateros1 = cuadrilateros() 
cuadrilateros1.imprimir()
cuadrilateros1.tipo()
