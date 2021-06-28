#Diseñado por Nelson Enrique Acuña Medina Grupo72
#Programa que permite llevar el inventario, compra y venta de una tienda.
class Tienda:

    def __init__(self):
        self.nombreTienda = input('Ingrese el nombre de la tienda: ')
        self.direccion = input('Ingrese la dirección de la tienda: ')
        self.nombreProducto = input('Ingrese el nombre del producto: ')  
        self.claseProducto = input('Ingrese la clase de producto: ') 
        self.existenciaProducto = int(input('Ingrese cantidad existente (Stok): '))
        self.valor = float(input('Ingrese el precio del producto'))
        self.valorProdc1 =18000
        self.valorProdc2 = 10000

    def infoTienda(self):      
        print("Nombre de la tienda:",self.nombreTienda)
        print("Dirección:",self.direccion)
        print("Nombre del producto:",self.nombreProducto)
        print("Clase de producto:",self.claseProducto)
        print("Existencia del producto:",self.existenciaProducto)
        print("El precio del producto es:",self.valor)

    def precios(self):
        if self.valor > 20000:
            print('Producto de alta calidad')
        else:
            print('Producto básico')

    def existencia(self):   
        if self.existenciaProducto <= 0:
            print("No existe este producto")
        else:
            print("Aún tenemos este producto")
    
    def venta(self):
        
        print(self.valorProdc1 + self.valorProdc2)

tienda1 = Tienda()
tienda1.infoTienda()
tienda1.existencia()
tienda1.precios()
tienda1.venta()
