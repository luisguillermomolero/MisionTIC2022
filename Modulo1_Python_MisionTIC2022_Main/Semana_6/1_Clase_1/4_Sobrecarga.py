class Punto:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return x, y

punto1 = Punto(4,6)
punto2 = Punto(1,-2)
print(punto1 + punto2)