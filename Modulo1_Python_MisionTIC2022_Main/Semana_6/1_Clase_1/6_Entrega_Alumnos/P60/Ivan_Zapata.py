# Frank Ivan Zapata Ayala
# Grupo 60
# CC 79951347

class Calculadora:

    def __init__(self):
        self.a = float(input("Digite el primer numero: "))
        self.b = float(input("Digite el segundo numero:"))

    def calculos(self):
        if self.b != 0:
            return(self.a, self.b, self.a+self.b, self.a-self.b,self.a*self.b, self.a/self.b)
        else:
            return(self.a, self.b, self.a+self.b, self.a-self.b,self.a*self.b, 'div/0')


calculadora = Calculadora()
a,b,suma,resta,mult,div = calculadora.calculos()
print("")
print('Suma: ', a , "+", b,"=" ,suma)
print('Resta: ', a , "-", b,"=" ,resta)
print('Multiplicación: ', a , "x", b,"=" ,mult )
print('División: ', a , "/", b,"=" ,div)