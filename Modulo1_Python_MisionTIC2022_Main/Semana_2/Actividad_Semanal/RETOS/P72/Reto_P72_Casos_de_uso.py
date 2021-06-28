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

Inventario = {
    'idDisco': 150001,
    'genDisco': 'Floklore',
    'costoDisco': 30000, 
    'cantanteD': 'Luis Silva',
    'empDisco': 'Sony',
    'volDisco': 5,
    'cantCompra': 6
}

print(discoTienda(Inventario))

Inventario = {
    'idDisco': 170001,
    'genDisco': 'Pop',
    'costoDisco': 25365, 
    'cantanteD': 'Justin Bieber',
    'empDisco': 'WMG',
    'volDisco': 3,
    'cantCompra': 2
}

print(discoTienda(Inventario))


Inventario = {
    'idDisco': 200000,
    'genDisco': 'O/G',
    'costoDisco': 31578, 
    'cantanteD': 'KPop',
    'empDisco': 'JYP',
    'volDisco': 2,
    'cantCompra': 7
}

print(discoTienda(Inventario))

Inventario = {
    'idDisco': 180001,
    'genDisco': 'Gospel',
    'costoDisco': 31875.68, 
    'cantanteD': 'Sam Cooke',
    'empDisco': 'WMG',
    'volDisco': 8,
    'cantCompra': 6
}

print(discoTienda(Inventario))

Inventario = {
    'idDisco': 160001,
    'genDisco': 'Rock',
    'costoDisco': 29874.12, 
    'cantanteD': 'Pink Floyd',
    'empDisco': 'PolyGram',
    'volDisco': 2,
    'cantCompra': 5
}

print(discoTienda(Inventario))

Inventario = {
    'idDisco': 170001,
    'genDisco': 'Pop',
    'costoDisco': 23587.65, 
    'cantanteD': 'Lil Uzi Vert',
    'empDisco': 'SM',
    'volDisco': 2,
    'cantCompra': 3
}

print(discoTienda(Inventario))