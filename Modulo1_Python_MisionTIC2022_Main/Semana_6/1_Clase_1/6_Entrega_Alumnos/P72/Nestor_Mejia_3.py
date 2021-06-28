#PROGRAMA DESARROLLADO POR - NESTOR DAVID MEJIA PINILLA
#PROGRAMA QUE PERMITE ENCONTRAR AREAS, PERIMETROS Y DIAMETROS DE DIFERENTES FIGURAS GEOMETRICAS

class fig_Geometricas:
    
    def __init__(self, base_rect, altura_rect, base_triang, altura_triang, diametro_circ):
    
        self.base_rect = base_rect#Atributo
        self.altura_rect = altura_rect#Atributo
        self.base_triang = base_triang#Atributo
        self.altura_triang = altura_triang#Atributo
        self.diametro_circ = diametro_circ#Atributo
        
    
    #Metodo para calcular el area de un rectangulo
    def calcular_area_rect(self):#Metodo
        self.operacion_area_rect = self.base_rect * self.altura_rect
        print('Su área es: \n', self.operacion_area_rect)

    #Metodo para calcular el perimetro de un rectangulo
    def calcular_perimetro_rect(self):#Metodo
        self.operacion_perimetro_rect = (self.base_rect*2) + (self.altura_rect*2)
        print('\nSu perímetro es: \n', self.operacion_perimetro_rect)

    #Metodo para calcular el area de un triangulo
    def calcular_area_triang(self):#Metodo
        self.operacion_area_triang = (self.base_triang * self.altura_triang) / 2
        print('Su area es: \n', self.operacion_area_triang)

    #Metodo para calcular el diametro de un circulo conociendo su circunferencia
    def calcular_diametro_circ(self):#Metodo
        self.operacion_diametro_circ = self.diametro_circ / 3.14
        print('Su diametro es: \n', self.operacion_diametro_circ)

operacion_rect = fig_Geometricas(4, 8, 10, 20, 100)  # Instanciando la clase fig_Geometricas()
print('\nVALORES DEL RECTANGULO')
operacion_rect.calcular_area_rect()#Llamando metodos
operacion_rect.calcular_perimetro_rect()#Llamando metodos
print('************************************')
print('\nVALORES DEL TRIANGULO')
operacion_rect.calcular_area_triang()#Llamando metodos
print('************************************')
print('\nVALORES DEL CIRCULO CONOCIENDO SU CIRCUNFERENCIA')
operacion_rect.calcular_diametro_circ()#Llamando metodos
print('************************************')
