class Usuariobancocuentaahorros:
    def __init__(self):
        self.nombre=input("ingrese nombre usuario: ")
        self.cuenta=float(input("ingrese cuanto dinero va asignar a su cuenta: "))
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Valor ingresado:",self.cuenta)
    def paga_manejocuenta(self):
        if self.cuenta>1000000:
            print("paga manejo de cuenta")
        else:
            print("no paga manejo de cuenta")
usuario1=Usuariobancocuentaahorros()
usuario1.imprimir()
usuario1.paga_manejocuenta()
