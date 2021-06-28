class Carro:
    def __init__(self, nombre, placa):
        self.nombre = nombre
        self.placa = placa
    def acelerar(self):
            print('El vehiculo ha acelerado.')
    def frenar(self):
            print('El vehiculo ha frenado')
#-------------------------------------------------------------
toreto = Carro('Toreto', 'ABC-123')
print('Tipo de dato: ', type(toreto).__name__)
print()
print('=== Atributos ===')
print()
print('Nombre:  ', toreto.nombre)
print()
print('Placa:   ', toreto.placa)
print()
print('=== Métodos ===\n')
toreto.acelerar()
print()
toreto.frenar()
print()
print('\n======================\n')
