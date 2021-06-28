def Logica(precioArticulo, cantidadArticulos):
    
    """ Calculo de la comisión por ventas

    Parametros:
    -----------
            comisionVentas (float):
                Valor del procentaje de comisión por total de ventas
            comisionTotal (float):
                Calculo de comisión total por ventas
                            
    Retorna:
    --------
        str:Cadena de caracteres de la forma " La comisión total es 
            de: " + str(comisionTotal)
    """

    comisionVentas = 0.075
    comisionTotal = round(precioArticulo * cantidadArticulos * comisionVentas, 2)
    return " La comisión total es de: " + str(comisionTotal)

#Casos de Prueba
print(Logica(53650.25, 78))
print(Logica(8974.25, 25))
print(Logica(156987.587, 115))
print(Logica(896523.00, 896))
print(Logica(23.987, 15))
print(Logica(3.659874, 66))