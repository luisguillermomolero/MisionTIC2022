#modelo 1
class celular:
    def __init__(self, marca, modelo, tamaño, color, peso):
        self.marca = marca
        self.modelo = modelo
        self.tamaño = tamaño
        self.color = color
        self.peso = peso
    def gama(self):
       print('Su celular es de gama alta.')
    def estado(self):
        print('Su celular se encuentra en perfecto estado')
    def precio(self):
        if self.peso > 200:
            print(f'su celular {micelu.marca} es pesado.')
        else:
            print(f'su celular {micelu.marca} es liviano.')

micelu = celular("Iphone","11 PRO", "7 pulgadas", "gris", 130)  # Instanciando la clase celular()
print(micelu.marca)              #Imprimir el atributo "marca" del objeto "celular"
print(micelu.modelo)              #Imprimir el atributo "modelo" del objeto "celular"
print(micelu.tamaño)              #Imprimir el atributo "tamaño" del objeto "celular"
print(micelu.color)              #Imprimir el atributo "color" del objeto "celular"
print(micelu.peso) 
