class Computador:

    def __init__(self):
        self.pagar=input("para comprar pc escriba tarjeta o efectivo: ")
        self.comparativa=input("ultima tecnologia escriba si o no: ")
        self.marca="Toshiba"
        self.año="2021"
        self.procesador="intel core i9 9th generation"
        self.tarjetagrafica="Nvidia 16Gb"
        self.precio="12'000.000"

    def imprimir(self):
        if self.comparativa=="no":
            print("Acaba de comprar con: ",self.pagar," un computador portatil")
            print("sus caracteristicas son: ", self.marca)
            print("año: ",self.año)
            print("procesador: ",self.procesador)
            print("tarjeta grafica",self.tarjetagrafica)
            print("precio", self.precio)
        
    def performance(self):
        if self.comparativa=="si":
            self.mayortarjeta="Nvidia 32Gb"
            self.mayorprocesador="intel core i9 10th generation"
            self.mayorprecio="15'000.000"

    def Actual(self):
        if self.comparativa=="si":
            print("Acaba de comprar con: ",self.pagar," un computador portatil")
            print("sus caracteristicas son: ", self.marca)
            print("año: ",self.año)
            print("procesador: ",self.mayorprocesador)
            print("tarjeta grafica",self.mayortarjeta)
            print("precio", self.mayorprecio)

        
    def descuento(self):
        if self.pagar=="tarjeta":
            print("tiene descuento")
        elif self.pagar=="efectivo":
            print("no tiene descuento")

pc1=Computador()
pc1.imprimir()
pc1.performance()
pc1.Actual()
pc1.descuento()
