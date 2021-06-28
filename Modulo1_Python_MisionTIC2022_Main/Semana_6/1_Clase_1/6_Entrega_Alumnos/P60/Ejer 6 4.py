#Autor:Iván Julián Cendales Montenegro. Grupo 60 UTP
#Código para determinar el valor a pagar en una factura de ladrillos teniendo en cuenta la cantidad comprada y su tamaño
class Material:

    #Definimos el método inicial (constructor)
    def __init__(self): # self inicializa los atributos de la instancia que se está inicializando
        self.material = input("Ingrese el nombre del material:")    #Atributo, porpiedad o caracteristica de la Clase "Material"
        self.cantidad = int(input("Ingrese cantidad:"))          #Atributo, propiedad o caracteristica de la Clase "Material"
        self.largo = int(input("Medidas disponibles, largo: 24 cm o 30 cm:"))
        self.ancho = int(input("Medidas disponibles, ancho: 13 cm o 20 cm:"))
        self.alto = int(input("Medidas disponibles, ancho: 9 cm o 10 cm:"))
        self.precioUnitario = int

    def imprimir(self):      #Comportamiento, funcionalidad, método
        print("Nombre:", self.material)
    
    def unidades(self):
        if self.cantidad<12:
            print("Tipo de venta:", self.cantidad, "unidades, venta al por menor")
        else:
            print(self.cantidad, "venta al por mayor")

    def descuento(self):   #Comportamiento, funcionalidad, método
        if self.cantidad<12:
            print("No hay descuento")
        else:
            print("Descuento del 5%")

    def precio(self):
        if self.largo==24 and self.ancho==13 and self.alto==9:
            self.precioUnitario=3000
        elif self.largo==30 and self.ancho==20 and self.alto==10:
            self.precioUnitario=6000
        else:
            print("No hay material con esas dimensiones.")
            exit()

    def valordelPago(self):
        if self.cantidad<12:
            print("El valor a pagar es:", self.precioUnitario * self.cantidad)
        else:
            print("El valor a pagar es:", (self.precioUnitario*0.95) * self.cantidad)

material1 = Material()  #Instancia, declarar la variable "material1" como tipo "clase".
material1.imprimir()
material1.unidades()
material1.descuento()
material1.precio()
material1.valordelPago()