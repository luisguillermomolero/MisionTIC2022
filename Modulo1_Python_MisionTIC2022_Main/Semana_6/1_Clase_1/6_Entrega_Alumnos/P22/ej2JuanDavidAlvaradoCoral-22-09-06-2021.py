#ejercicio1
class Animal():
    def __init__(self):
        self.tipodeanimal='mamiferos'
    def mensaje(self):
        print("mensaje desde la clase animal")

class Perro(Animal):
    def __init__(self):
        self.raza='pequines'
    def mensaje(self):
        print("mensaje desde la clase perro")

class Gato(Animal):
    def __init__(self):
        self.raza='gato comun'
    def mensaje(self):
        print("mensaje desde la clase gato")

class Hamster(Animal):
    def __init__(self):
        self.raza='sirio o dorado'
    def mensaje(self):
        print("mensaje desde la clase Hamster")
        
class Pez(Animal):
    def __init__(self):
        self.raza='golfish'
    def mensaje(self):
        print("mensaje desde la clase pez")


tipodeperro=Perro()
tipodegato=Gato()
tipodehamster=Hamster()
tipodepez=Pez()
tipodeperro.mensaje()
tipodegato.mensaje()
tipodehamster.mensaje()
tipodepez.mensaje()
