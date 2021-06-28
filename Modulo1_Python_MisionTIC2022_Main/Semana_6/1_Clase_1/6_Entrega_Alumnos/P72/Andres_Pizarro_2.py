#Desarrollado por Andrés Pizarro Grupo 72 Misión TIC
"""
Programa que permite armar un carro con sus componentes básicos
Primero, arma el motor con sus válvulas, bielas y sus cc,
Luego, arma las ruedas con sus neumáticos y rines,
Luego, junta el motor y las ruedas en la clase Carro().

Finalmente muestra la descripción del carro con sus componentes.
"""

class Motor:
    def __init__(self,valvulas:int,bielas:int,centCubs:int) -> None:
        self.valvulas = valvulas
        self.bielas = bielas
        self.centCubs = centCubs
    def getMotor(self):
        return self
    def getDescripcion(self):
        print(f"Automovil con motor de {self.valvulas} valvula, {self.bielas} bielas y {self.centCubs} Centimetro Cúbicos")

class Neumaticos:
    def __init__(self,cantidad:int) -> None:
        self.cantidad = cantidad
    def getNeumaticos(self):
        return self

class Rines:
    def __init__(self,cantidad:int) -> None:
        self.cantidad = cantidad
    def getRines(self):
        return self
    def getCantidad(self)->int:
        return self.cantidad

class Ruedas:
    neumaticos:Neumaticos
    rines:Rines
    def __init__(self,neumaticos:Neumaticos,rines:Rines) -> None:
        self.neumaticos = neumaticos
        self.rines = rines
    def getRuedas(self):
        return self
    def getDescripcion(self):
        print(f"El automovil tiene {self.rines.getCantidad()} Ruedas")

class Carro:
    def __init__(self,motor:Motor,ruedas:Ruedas,) -> None:
        self.motor = motor
        self.ruedas = ruedas
    def getDefinicion(self):
        self.motor.getDescripcion()
        self.ruedas.getDescripcion()

motor:Motor = Motor(24,4,1800)
rines:Rines = Rines(4)
neumaticos:Neumaticos = Neumaticos(4)
ruedas:Ruedas = Ruedas(neumaticos,rines)
carro1:Carro = Carro(motor,ruedas)

carro1.getDefinicion()