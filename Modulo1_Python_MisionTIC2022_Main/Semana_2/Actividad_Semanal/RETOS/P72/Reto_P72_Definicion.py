def discoTienda (Inventario:dict)-> dict:
    
    #Variables
    codigoDisco = Inventario['idDisco']               # Id Disco
    genDisco = Inventario['genDisco']                 # Genero del disco
    costoDisco = Inventario['costoDisco']             # Costo del disco
    cantanteD = Inventario['cantanteD']               # Cantante del disco
    empDisco = Inventario['empDisco']                 # Empresa discografica
    volDisco = Inventario['volDisco']                 # Volumen del disco
    cantCompra = Inventario['cantCompra']             # Cantidad de ejemplares comprados
    a = codigoDisco == 150001 and cantCompra > 3
    b = codigoDisco == 150001 and cantCompra <= 3
    c = codigoDisco == 160001 and cantCompra > 4
    d = codigoDisco == 160001 and cantCompra <= 4
    e = codigoDisco == 170001 and cantCompra > 3
    f = codigoDisco == 170001 and cantCompra <= 3
    g = codigoDisco == 180001 and cantCompra > 5
    h = codigoDisco == 180001 and cantCompra >= 5
    i = codigoDisco == 200000

    # Venta

    if a:
        totalPago = round((costoDisco * cantCompra) * 0.90, 2)
    elif b:
        totalPago = round((costoDisco * cantCompra) * 0.95, 2)
    elif c:
        totalPago = round((costoDisco * cantCompra) * 0.80, 2)
    elif d:
        totalPago = round((costoDisco * cantCompra) * 0.90, 2)
    elif e:
        totalPago = round((costoDisco * cantCompra) * 0.78, 2)
    elif f:
        totalPago = round((costoDisco * cantCompra) * 0.95, 2)
    elif g:
        totalPago = round((costoDisco * cantCompra) * 0.60, 2)
    elif h:
        totalPago = round((costoDisco * cantCompra) * 0.85, 2)
    elif i:
        totalPago = round((costoDisco * cantCompra) * 0.75, 2)
    

       
    diccionario_respuesta = {
        'idDisco': codigoDisco,                     # Código de artículo
        'genDisco': genDisco,                       # Genero del disco
        'costoDisco': costoDisco,                   # Costo del disco
        'cantCompra': cantCompra,                   # Cantidad de ejemplares comprados
        'totalPago': totalPago                      # Total a pagar por compra
    }
    
    return diccionario_respuesta
