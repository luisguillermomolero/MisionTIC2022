# -*- coding: utf-8 -*-
"""
Created on Tue Jun  10  2021 - Hora 8:00 p.m.

@author: Juan Carlos Cañón Sossa
         C.C. 7.556.291
         Grupo 60
         Formador: Luis Molero

Enunciado: Crea¡e un programa que resuelva cualquier ecuación de segundo grado, determinando que tipo de 
soluciones presenta, su vértice, su tipo de concavidad, presente 10 puntos de la gráfica y finalmente muestre 
la gráfica de la función asociada a esa ecuación. 
"""

#Programa que resuelve una ecuación de segundo grado, dados los coeficientes a, b y c
import matplotlib.pyplot as plt
class Raices: # Se define la clase 
     

    #Definimos el método inicial (constructor)
    def __init__(self):
        self.A=float(input("Ingrese a: "))# se solicita el ingreso del valor a   
        self.B=float(input("Ingrese b: "))  # se solicita el ingreso del valor b  
        self.C=float(input("Ingrese c: ")) # se solicita el ingreso del valor c   

    def imprimir(self):      #función que imprime los valores capturados
          print("\n Los números ingresados fueron: ")    
          print("numero 1: ",self.A)
          print("numero 2: ",self.B)
          print("numero 3: ",self.C)

    def calcula_raices(self):   #función que calcula las raices de la ecuación
         determinante=(((self.B)**2)-4*(self.A)*self.C)
         if determinante > 0:
             print("\n")
             print ("El valor del determinante es: ", determinante)
             print("La ecuación tiene 2 soluciones reales diferentes y son: ")
             x1 = (-1*self.B + ((self.B**2)-(4*self.A*self.C))**(1/2))/(2*self.A) # Fórmula de Bhaskara parte positiva
             x2 = (-1*self.B - ((self.B**2)-(4*self.A*self.C))**(1/2))/(2*self.A)  # Fórmula de Bhaskara parte negativa
             print("x1 = ",x1)
             print("x2= ", x2)
             print("tiene dos puntos de corte con el eje x: \n")
             print(f"Punto de corte 1: ({x1}, 0)")
             print(f"Punto de corte 2: ({x2}, 0)")
             
         elif determinante == 0:
             print("\n")
             print ("El valor del determinante es: ", determinante)
             print("La ecuación tiene 2 soluciones reales iguales y son : ")
             x1 = (-1*self.B + ((self.B**2)-(4*self.A*self.C))**(1/2))/(2*self.A) # Fórmula de Bhaskara parte positiva
             print(" x1 y x2 = ", x1)
             print("solo tiene un punto de corte con el eje x:")
             print(f"Punto de corte 1 ({x1}, 0)")
             
         else:
             print("\n")
             print ("El valor del determinante es: ", determinante)
             print("La ecuación no tiene soluciones Reales")
             print("No hay punto de corte con el eje x")
   
    def concavidad(self): #función que determina la concavidad de la parábola
        if self.A >0:
            print("La gráfica es concava hacia arriba")
        else:
            print("La gráfica es concava hacia abajo")
            
    def grafica(self):#función que construye la gráfica
        puntos=()
        verticex = -1*self.B/(2*self.A)
        valoresx=[]
        verticey = self.A*(verticex)**2+(self.B*verticex)+self.C
        valoresy =[]
        puntos=[]
        
        for x in range(-5,6):
           #puntos.append( (valoresx.append(x), valoresy.append((self.A)*x**+self.B*x+self.C)))
           valoresx.append(x)
           valoresy.append((x*x)*self.A + x*self.B+self.C)
           #puntos.append(valoresx, valoresy) 
        print(valoresx)
        print(valoresy)
        for x in valoresx:
            puntos.append((valoresx[x],valoresy[x]))
            
        print("El vértice y los puntos a graficar son: ")
        print(f"Vértice = ({verticex}, {verticey})   , puntos: {puntos}")  
        plt.scatter(valoresx,valoresy, color="blue", linewidth = 3, label = "puntos de la función") 
        plt.title('Gráfica de la Función')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.legend()
        plt.grid()
        plt.show()
    #Instanciación y llamado de funciones      
raices1 = Raices ()
raices1.imprimir()
raices1.calcula_raices()
raices1.concavidad()   
raices1.grafica()