#Programa que permita validar si un empleado debe pagar o no impuesto de acuerdo a su ingreso mensual

class Raices:
     

    #Definimos el método inicial (constructor)
    def __init__(self):
        self.A=float(input("Ingrese a:"))   
        self.B=float(input("Ingrese b:"))   
        self.C=float(input("Ingrese c:")) 

    def imprimir(self):      
        print("numero1",self.A)
        print("numero2:",self.B)
        print("numero3:",self.C)

    def cuadrado(self):  
        if ((B**2)-4*A*C) < 0:
            print("La solución de la ecuación es con numeros complejos")
                else:
    x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)  
    x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)  
           print("Las soluciones de la ecuación son:")
           print(x1)
            print(x2)
            
            
            
Raices.imprimir()
 Raices.cuadrado()