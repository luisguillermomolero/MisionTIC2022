class motocicleta:
    def __init__(self):
        self.marca=input("Ingrese la marca de su moto: ")
        self.modelo=input("Ingrese el modelo de su motocicleta: ")
        self.placa=input("ingrese la placa de su moto")
        self.color=input("Ingrese el color de su motocicleta")
        self.cilindraje=input("Ingrese el cilindraje de su moto")
   
    def imprimir(self):
        print(f" Marca: ", self.marca + "  Modelo: ",self.modelo + "  Placa: ",self.placa + "  Color: ",self.color + "  Cilindraje: ",self.cilindraje)

    def Modelo(self):
            if self.modelo<="2000":
                print("Su moto es antigua porque es modelo",self.modelo)
            else:
                print("Su moto no es antigua porque es modelo",self.modelo)

antiguedad= motocicleta ()
antiguedad.imprimir()
antiguedad.Modelo()