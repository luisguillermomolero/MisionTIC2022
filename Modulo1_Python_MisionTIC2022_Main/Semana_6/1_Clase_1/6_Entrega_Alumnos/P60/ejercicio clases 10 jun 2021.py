class Celular: 
    def __init__(self, marca, memoria_ram, memoria_rom, pantalla, bateria, precio):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.memoria_rom = memoria_rom
        self.pantalla = pantalla
        self.bateria = bateria
        self.precio = precio
    def mram (self):
        if self.memoria_ram >= 4:   #dato en gigas
            print ('Memoria RAM cumple')
        else:
            print ('Memoria RAM no cumple')
    def mrom (self):
        if self.memoria_rom >= 64:   #dato en Gigas
            print ('Almacenamiento cumple')
        else:
            print ('Almacenamiento no cumple')
    def display (self):
        if self.pantalla >= 6:      #dato en pulgadas
            print ('pantalla cumple')
        else:
            print ('pantalla no cumple')
    def bat (self):
        if self.bateria >=4000: #dato en miliamperios hora
            print ('Batería cumple')
        else:
            print ('Batería no cumple')
    def price (self):
        if self.precio <=600000: #dato en pesos col
            print ('Presupuesto cumple')
        else:
            print ('Presupuesto no cumple')
celular1 = Celular('motorola',3, 32, 6, 5000, 569000)
print(celular1.marca)
celular1 .mram()
celular1 .mrom()  
celular1 .display()
celular1 .bat()  
celular1 .price()


