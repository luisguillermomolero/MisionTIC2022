# Programa que permite inventariar los vehiculos que ingresan al concesionario.

print('======================')
print()

class Carro:
    def __init__(self, nombre, placa, marca, modelo, precio):
        self.nombre = nombre
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        
    def encender(self):
        print('El vehiculo ha encendido.')

    def apagar(self):
        print('El vehiculo se ha apagado')

    def clasificar(self):
        if self.precio > 10000:
            print(f'El vehiculo {toreto.nombre} es gama alta.')
        else:
            print(f'El vehiculo {toreto.nombre} es gama baja.')

toreto = Carro('Toreto', 'ABC-123', 'Mazda', 2016, 15000)
    
print()

print('=== Atributos ===')
print()

print('Nombre:  ', toreto.nombre)
print()

print('Placa:   ', toreto.placa)
print('Marca:   ', toreto.marca)
print('Modelo:  ', toreto.modelo)
print('Precio:  ', toreto.precio)

print('\n=== Métodos ===\n')

toreto.encender()
toreto.a
