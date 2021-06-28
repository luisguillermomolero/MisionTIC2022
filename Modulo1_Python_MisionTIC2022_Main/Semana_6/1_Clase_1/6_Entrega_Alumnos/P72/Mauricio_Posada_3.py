# Desarrollado por Muricio Posada grupo 72
# Programa que permite clasificar los animales que llegan al zoologico

print('======================\n')

class Animal:

    def __init__(self, nombre, color, nacimiento, alimentacion, habitat, peso):
        self.nombre = nombre
        self.color = color
        self.nacimiento = nacimiento
        self.alimentacion = alimentacion
        self.habitat = habitat
        self.peso = peso

    def verificar_color(self):
        print(f'El color del {self.nombre} es: {self.color}')

    def clasif_nacimiento(self):
        if self.nacimiento == 'Viviparo':
            print('Es un animal Viviparo')
        else:
            print('Es un animal Oviparo')
    
    def alistar_alimentacion(self):
        if self.alimentacion == 'Carnivoro':
            cantidad = self.peso * 0.32
            print(f'Debe alimentarse con {cantidad}kgs de carne.')
        else:
            cantidad = self.peso * 10
            print(f'Debe alimentarse con {cantidad}gramos de vegetales.')

    def ubicar_ejemplar(self):
        if self.habitat == 'Selva':
            print('Se debe ubicar en el sector A.')
        elif self.habitat == 'Desierto':
            print('Se debe ubicar en el sector B.')
        elif self.habitat == 'Llanura':
            print('Se debe ubicar en el sector C.')


tigre = Animal('Tigre', 'Amarillo', 'Viviparo', 'Carnivoro', 'Selva', 350)
camello = Animal('Camello', 'Cafe', 'Viviparo', 'Herviboro', 'Desierto', 850)
aguila = Animal('Aguila', 'Negro - Blanco', 'Oviparo', 'Carnivoro', 'Llanura', 25)

tigre.verificar_color()
tigre.clasif_nacimiento()
tigre.alistar_alimentacion()
tigre.ubicar_ejemplar()
print()
camello.verificar_color()
camello.clasif_nacimiento()
camello.alistar_alimentacion()
camello.ubicar_ejemplar()
print()
aguila.verificar_color()
aguila.clasif_nacimiento()
aguila.alistar_alimentacion()
aguila.ubicar_ejemplar()