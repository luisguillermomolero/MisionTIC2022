def AutoPartes(ventas: list):
    #Inicializar diccionario
    venta={}
    #Ciclo para agregar un nuevo evento
    for idProducto, dProducto, pnProducto, cvProducto, sProducto, \
        nComprador, cComprador, fVenta in ventas:
        #Fuerza la entrada
        if venta.get(idProducto) == None:                           
            #Creacion de un nuevo evento
            venta[idProducto] = []                                  
        #Registro de una nueva lista de tuplas en el dict agenda
        venta[idProducto].append((dProducto, pnProducto, cvProducto, \
        sProducto, nComprador, cComprador, fVenta))                 
    return venta
#Definición de función consulta
def consultaRegistro(ventas, idProducto):
    #Ubicar una fecha dentro de la agenda
    if idProducto in ventas:
        for dProducto, pnProducto, cvProducto, sProducto, nComprador, \
            cComprador, fVenta in ventas[idProducto]:
            #Muestra todos los registros encontrados
            print('Producto consultado :', idProducto, ' Descripción '\
                , dProducto, ' #Parte ', pnProducto, ' Cantidad vendida '\
                , cvProducto, ' Stock ', sProducto, ' Comprador', nComprador,\
                ' Documento ', cComprador, ' Fecha Venta ', fVenta)
    else:
        #Si no ubica coincidencia de registros
        print("No hay registro de venta de ese producto")
