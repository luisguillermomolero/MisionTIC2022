#Ejercicio - Leer un número entero y determinar si tiene 3 dígitos.
class Digitos:
    #Definimos el método inicial (constructor)
    def __init__(self): # self inicializa los atributos de la instancia que se está inicializando
        self.num_1 = int(input('Por favor digite un número entero para identificar si tiene 3 digitos:\n'))
    def imprimir(self):
        print('Numero ingresado:\n',self.num_1)
    def operacion_aritmetica(self):
        if self.num_1 >= 100 and self.num_1 <= 999:
            print('El número ingresado tiene 3 digitos')
        else:
            print('El número ingresado no tiene 3 digitos')
operacion = Digitos()
operacion.imprimir()
operacion.operacion_aritmetica()