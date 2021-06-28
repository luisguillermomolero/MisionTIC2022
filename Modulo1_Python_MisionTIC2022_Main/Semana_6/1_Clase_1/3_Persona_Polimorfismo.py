class Persona():
    def __init__(self):
        self.cedula = 13765890
    def mensaje(self):
        print("mensaje desde la clase Persona")

class Obrero(Persona):
    def __init__(self):
        self.__especialista = 1
    def mensaje(self):
        print("mensaje desde la clase Obrero")
