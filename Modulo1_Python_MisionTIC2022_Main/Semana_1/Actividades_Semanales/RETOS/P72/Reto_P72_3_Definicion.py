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

