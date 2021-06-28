def Logica(cantidadAnimales):
    """ Compra de animales por un ganadero

    Parametros:
    -----------
            ventaInicial (float):
                Costo inicial por la compra de 18 animales (por defecto 9725482.00 )
            animalInicial (int):
                Cantidad inicial de animales comprados (por defecto 18)
            Descuento (float):
                Porcentaje de descuento por la compra de mas de 100 animales (por defecto 0.085)
            valorTotalActual (float):
                Calculo del monto a pagar con el descuento
    
    Retorna:
    --------
        str:Cadena de caracteres de la forma “Ud paga con un descuento del 15%
            un valor de: ", Logica(119), donde, la Lógica calcula el monto a 
            pagar menos el descuento en base a 119 animales.
    """


    ventaInicial = 9725482
    animalInicial = 18
    Descuento = 0.85
    valorTotalActual = round(((cantidadAnimales * ventaInicial) / animalInicial) * Descuento, 2)
    return " Ud con un descuento del 15% paga un valor de: " + str(valorTotalActual)

#Casos de prueba
print(Logica(119))
print(Logica(150))
print(Logica(205))
print(Logica(178))
print(Logica(142))
print(Logica(17))