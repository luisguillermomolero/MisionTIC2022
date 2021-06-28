#Desarrollado por: Javier Castañeda
class Conversion:
    def __init__(self):  
        self.x=float(input("Ingrese la medida en metros que desea convertir: "))
    def Operaciones(self):   
        self.yarda =self.x*1.094              
        self.pulgada=self.x*39.37
        self.milimetro=self.x*1000
        self.milla =self.x/1609
        self.kilometros =self.x/1000 
	    
    def imprimir(self):     
        print("la medida en yardas es: ",self.yarda)
        print("la medida en pulgadas es: ",self.pulgada)
        print("la medida en milimetros es: ",self.milimetro)
        print("la medida en millas es: ",self.milla)
        print("la medida en kilometros es: ",self.kilometros)

conversion = Conversion()  
conversion.Operaciones()
conversion.imprimir()
