class motor:
    def __init__(self, numero, cilindrage, combustible, velocidades, potencia):
        self.numero = numero
        self.cilindrage = cilindrage
        self.combustible = combustible
        self.velocidades = velocidades
        self.potencia = potencia
    def imprimir_numero_y_cilindrage(self):
        print(self.numero)
        print(self.cilindrage)
    def imprimir_combustible_y_velocidades(self):
        print(self.combustible)
        print(self.velocidades)
    def imprimir_potencia(self):
        print(self.potencia)
mymotor = motor('numero: xy008978', 'cilinadrage: 3000', 'combustible: acpm', 'velocidades: 6', 'potencia: 3500')
mymotor.imprimir_combustible_y_velocidades()
mymotor.imprimir_numero_y_cilindrage()
mymotor.imprimir_potencia()