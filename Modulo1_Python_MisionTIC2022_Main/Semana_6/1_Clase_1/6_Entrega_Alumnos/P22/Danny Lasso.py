class RaizDe:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del usuario:")
        self.valor = int(input('Por favor, introduzca un numero para calcular su raiz cuadrada: '))
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("operacion: raiz cuadrada de: ", self.valor)
    def Raiz_cuadrada(self):
        if type(self.valor) == int:
            raiz = round(self.valor ** 0.5, 3)
            mensaje=( 'la raiz cuadrada de: '+ str(self.valor) + ' es ' + str(raiz))
            print(mensaje)
        else:
            print("Raiz imaginaria")
# bloque principal
calculo = RaizDe()
calculo.imprimir()
calculo.Raiz_cuadrada()

