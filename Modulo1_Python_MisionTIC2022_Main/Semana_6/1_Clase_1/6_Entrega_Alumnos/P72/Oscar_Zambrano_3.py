
# programa que permite validar si un comprador tiene descuento
# desarrollado por OSCAR ZAMBRANO BENJUMEA GRUPO 72
class factura:

    # self inicializa los atributos de la instancia que se esta inicializando
    def __init__(self, totalD):
        # atributo, propiedad, o caracteristica de la clase "factura"
        self.nombre = input("Ingrese el nombre del Cliente: ")
        self.cedula = input("Ingrese cedula Cliente: ")
        self.producto = input("Ingrese tipo de producto: ")
        self.costo = float(input("Ingrese valor unitario del producto: "))
        self.cantidad = int(input("Ingrese cantidad de Producto: "))
        self.totalD = totalD
    def imprimir(self):  # comportamiento, funcionalidad, metodo
        print("Nombre", self.nombre)
        print("Cedula", self.cedula)
        print(("Producto", self.producto))
        print("Valor unitario", self.costo)
        print("Cantidad", self.cantidad)
    def descuento(self):  # realizamos el calculo para generar el descuento de acuerdo al producto
        if self.cantidad > 3 and self.producto == "pantalon":
            self.totalD = (self.cantidad * self.costo) * 0.10
            print("su descuento es :", self.totalD)
        elif self.cantidad > 3 and self.producto == "camisa":
            self.totalD = (self.cantidad * self.costo) * 0.10
            print("su descuento es :", self.totalD)
        elif self.cantidad > 3 and self.producto == "chaqueta":
            self.totalD = (self.cantidad * self.costo) * 0.10
            print("su descuento es :", self.totalD)
        else:
            print("No genera descuento")
    def pagoTotal(self):
        totalCompra = (self.cantidad * self.costo)-self.totalD
        print("Total a pagar :", totalCompra)


venta = factura(0)

venta.imprimir()
venta.descuento()
venta.pagoTotal()
