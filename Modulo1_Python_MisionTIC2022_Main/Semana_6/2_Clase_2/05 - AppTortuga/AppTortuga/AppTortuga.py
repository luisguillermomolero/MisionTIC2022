#Traemos la clase tortuga
#from turtle import * #Fundir con el espacio de nombres actual
import turtle #Importar la clase

#Librería para funciones aleatorias
import random

#Capa de interacción con el usuario por consola
from InterfazConsola import *

#Procedimientos trabajando con el objeto tortuga: comportamiento

def lineaHorizontalDiscontinua(tortuga,longitudPedazoLinea=5,x=0,y=0,numeroRayas=10):
    alternador = True
    tortuga.penup() #Se asegura de que el objeto no dibuje nada hasta activar el "pencil"
    tortuga.goto(x,y) #Hace un  salto de código a las coordenadas "x" "y"
    tortuga.pendown() #Deja el bolígrafo para que la tortuga dibuje una línea detrás de él mientras se mueve
    for _ in range(numeroRayas):
        tortuga.goto(x+longitudPedazoLinea,y)
        x += longitudPedazoLinea
        #y += longitudPedazoLinea
        if alternador:
            tortuga.penup()
            alternador = False
        else:
            tortuga.pendown()
            alternador = True        
    #Retornar al origen
    tortuga.penup()
    tortuga.goto(0,0)

def lineaDiagonalDiscontinua(tortuga,longitudPedazoLinea=5,x=0,y=0,numeroRayas=10):
    alternador = True
    tortuga.penup()
    tortuga.goto(x,y)
    tortuga.pendown()
    for _ in range(numeroRayas):
        tortuga.goto(x+longitudPedazoLinea,y+longitudPedazoLinea)
        x += longitudPedazoLinea
        y += longitudPedazoLinea
        if alternador:
            tortuga.penup()
            alternador = False
        else:
            tortuga.pendown()
            alternador = True        
    #Retornar al origen
    tortuga.penup()
    tortuga.goto(0,0)
    
def poligonoConvexo4LadosRelleno(tortuga):
    tortuga.begin_fill() #Rellena una figura
    tortuga.fillcolor('cyan') #Rellena con color Cyan
    tortuga.goto(0,0) #Vuelve a las coordenadas 0,0
    tortuga.pendown() #Se asegura de que el objeto no dibuje nada hasta activar el "pencil"
    tortuga.goto(100,50)
    tortuga.dot(10,'blue')#También: rgb -> reed green blue -> 255,255,255
    tortuga.goto(100,-50)
    tortuga.dot(10,'red')
    tortuga.goto(50,-50)
    tortuga.dot(10,'orange')
    tortuga.goto(0,0)
    tortuga.dot(10,'black')
    tortuga.end_fill()

def poligonoConvexo4Lados(tortuga):    
    tortuga.goto(0,0)
    tortuga.pendown() #Se asegura de que el objeto no dibuje nada hasta activar el "pencil"
    tortuga.goto(100,50)
    tortuga.dot(10,'blue')#También: rgb -> reed green blue -> 255,255,255
    tortuga.goto(100,-50)
    tortuga.dot(10,'red')
    tortuga.goto(50,-50)
    tortuga.dot(10,'orange')
    tortuga.goto(0,0)
    tortuga.dot(10,'black')

#Sección Principal
##################

#Crear un objeto tipo tortuga
tortuga = turtle

#Inicialización interacción por interfaz gráfica:
#Crear la ventana donde alojaremos la tortuga
tortuga.setup(800,600,0,0)#Ver el área de trabajo
tortuga.screensize(800,600)#Área de trabajo
tortuga.title("Ventana Trabajo Tortuga")
#Mostrar tortuga
tortuga.showturtle()

#Iniciar interacción por consola
mensajeBienvenida()

#Mainloop: procedimientos que muestran el comportamiento del objeto tortuga
mainloop = True
while mainloop:

    #Solicitar a la interfaz la selección de una opción
    opcion = formularioMenuAppTortuga()

    #Si Dibujado de líneas discontinuas fue seleccionado
    if opcion == 1:       

        #Reportar en consola procedimiento del objeto
        mensaje("->Dibujado de Líneas Discontinuas")
        
        #Procedimiento ralizando cambios de estado en el objeto        
        longitudPedazoLinea = 15
        tortuga.clear() #Elimina los dibujos de la tortuga de la pantalla.
        lineaHorizontalDiscontinua(tortuga,longitudPedazoLinea)        
        tortuga.clear()
        lineaDiagonalDiscontinua(tortuga,longitudPedazoLinea,x=-100,y=-100)        
        tortuga.clear()
        lineaHorizontalDiscontinua(tortuga,longitudPedazoLinea=5,x=-300,numeroRayas=25)      
        
    #Si Dibujado de polígono de 4 lados sin relleno fue seleccionado
    elif opcion == 2:

        #Reportar en consola procedimiento del objeto
        mensaje("->Dibujando Polígono Irregular de 4 Lados sin Relleno")       

        #Procedimiento ralizando cambios de estado en el objeto        
        tortuga.clear()
        poligonoConvexo4Lados(tortuga)#Crear un polígono convexo irregular 4 lados (paso a paso)                 
        
    #Si Dibujado de polígono de 4 lados con relleno fue seleccionado
    elif opcion == 3:

        #Reportar en consola procedimiento del objeto
        mensaje("->Dibujando Polígono Irregular de 4 Lados con Relleno")       

        #Procedimiento ralizando cambios de estado en el objeto        
        tortuga.clear()
        poligonoConvexo4LadosRelleno(tortuga)#Crear un polígono convexo irregular 4 lados (paso a paso)

    #Si Dibjuado de polilínea fue seleccionada
    elif opcion == 4:

        #Reportar en consola procedimiento del objeto
        mensaje("->Dibujando Polilínea Coordenadas por Consola")        

        #Polilínea (polígono que se va generando) con coordenadas ingresadas por el usuario
        tortuga.clear()
        tortuga.goto(0,0)
        recogiendoCoordenadas = True
        relleno = input('Rellenar polilínea? (s)').lower() == 's'
        if relleno:
            tortuga.begin_fill()
            tortuga.fillcolor('cyan')
        colores = ['blue','orange','red','black','yellow','cyan']
        while(recogiendoCoordenadas):
            x,y = recogerCoordenadasTeclado()
            tortuga.goto(x,y)
            tortuga.dot(10, colores[ random.randint(0,len(colores)-1) ] )
            recogiendoCoordenadas = controlParada()
        if relleno:
            tortuga.end_fill()   

    #Si la opcíon de salida fue seleccionadA por el usuario en el menú    
    elif opcion == 5:
        
        #Solicitar a la interfaz mostrar el mensaje de cierre        
        mensajeDespedida()
        input('Presione cualquier tecla para cerrar ventana.')

        #Finalización:
        #Cerrar la ventana
        #Terminar procesos con tortuga
        tortuga.bye()
        
        #Terminar el mainloop de la aplicación
        mainloop = False
    
    else:
        #Solicitar a la interfaz mostrar el mensaje
        mensaje("Opción inválida!")

    

    
















