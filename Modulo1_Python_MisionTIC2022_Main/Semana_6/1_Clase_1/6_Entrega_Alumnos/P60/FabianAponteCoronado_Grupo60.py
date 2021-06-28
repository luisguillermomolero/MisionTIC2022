
'''Desarrollar una clase con al menos 5 atributos, 
adicional, 4 métodos + el constructor, 
entregando el objeto al momento de instanciar la clase con la variable. 
No olvidar, colocar su nombre como autor de la app y el enunciado.
'''


# Autor: Fabian Andrés Aponte _ Grupo:60 

'''Ingrese la siguiente información en referencia a su vehículo, en algunos puntos se indicara
las opciones de respuesta, al final el aplicativo le indicará algunas conclusiones sobre su vehículo'''


class car:
    def __init__(self, model, color,carroceria,marca,tipocombustible):
        self.model = model
        self.color = color
        self.carroceria = carroceria
        self.marca= marca
        self.tipocombustible=tipocombustible

    def imprimir(self):
        print('Las características del vehículo son:')
        print('- Modelo: '+ str(mycar.model))
        print('- '+ mycar.color)
        print('- '+ mycar.carroceria)
        print('- '+ mycar.marca)      
        print('- ' + mycar.tipocombustible)

    def pagaimpuestos(self):
        if self.tipocombustible=='Electrico':
            print('El vehículo descrito no debe pagar impuestos')
        else:
            print('El vehículo descrito debe pagar impuestos')

    def clasificacionmodelo(self):
        if self.model==2021:
            print("El vehículo es último modelo")
        elif self.model>=2015 and self.model<2021:
            print("El vehículo es un modelo reciente")
        else: print("El vehículo es un modelo ordinario")

    def ambiental(self):
        if self.tipocombustible=='Electrico':
            print("El vehículo es amigable con el medio ambiente")
        elif self.tipocombustible=='Gas':
            print("El vehículo contamina moderadamente el medio ambiente")
        else: print("el vehículo contamina bastante el medio ambiente")

    def espacio(self):
        if self.carroceria=='Camioneta':
            print("El vehículo es espacioso, apto para viajar en familia")
        else: print ("El vehículo no es tan espacioso, apto para usar dentro la ciudad")
    


print ('''Ingrese la siguiente información en referencia a su vehículo, en algunos puntos se indicará
las opciones de respuesta, al final el aplicativo le indicará algunas conclusiones sobre su vehículo
''')
modelo=int(input('Ingrese el año del fabricación del vehículo: '))
color=input('Ingrese el color de vehículo: ')
tipo=input('Ingrese el tipo de carrocería del vehículo: Automovil ó Camioneta: ')
marca=input('Ingrese la marca del vehículo:')
combustible=input('Indique el tipo de combustible del vehículo: Gas,Gasolina, Diesel o Electrico:')

mycar = car(modelo,color,tipo,marca,combustible)
mycar.imprimir()
mycar.pagaimpuestos()
mycar.clasificacionmodelo()
mycar.ambiental()
mycar.espacio()

       


