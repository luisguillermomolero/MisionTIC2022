def Logica(lado):
    """ Calculo del perímetro y área de un terreno

    Parametros:
    -----------
            perimetroTerreno (float):
                Formula para el calculo del perímetro de un terreno
            hTerreno (float):
                Formula para el calculo de la altura de la forma geométrica
            areaTerreno (float)
                Formula para el calculo del área del terreno
                
    Retorna:
    --------
        str:Cadena de caracteres de la forma " El perimetro del terreno 
            es: " + str(perimetroTerreno) + " kilómetros, y su área de: " 
            + str(areaTerreno), donde, la Lógica calcula el perímetro y
            el área del terreno
    """
    perimetroTerreno = round(3 * lado, 4)
    hTerreno = round(((3 ** 0.5) / 2) * lado, 4)
    areaTerreno = round(lado * hTerreno /2, 4)
    return " El perímetro del terreno es: " + str(perimetroTerreno) + " kilómetros, y su área de: " + str(areaTerreno)


#Casos de prueba    
print(Logica(1.25))
print(Logica(33.25))
print(Logica(254.256))
print(Logica(12.25))
print(Logica(985.2655))
print(Logica(1624.525))
print(Logica(124.52))
