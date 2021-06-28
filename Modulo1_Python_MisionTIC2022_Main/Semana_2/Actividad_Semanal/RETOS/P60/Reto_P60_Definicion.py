def gananciasVentas (Productos:dict)-> dict:
    
    #Variables
    codigoVenta = Productos['idVenta']   # Código de artículo
    ventaArt = Productos['vArticulo']    # Valor en pesos del producto para la venta
    dProd = Productos['dProducto']       # Descripción del producto
    tProd = Productos['tProducto']       # Talla producto
    a = ventaArt >= 0 and ventaArt <= 100000 and tProd == 's' or tProd == 'S'       # Comisión 5%, Gatos
    b = ventaArt >= 0 and ventaArt <= 100000 and tProd == 'm' or tProd == 'M'       # Comisión 6%
    c = ventaArt >= 0 and ventaArt <= 100000 and tProd == 'l' or tProd == 'L'       # Comisión 7%
    d = ventaArt >= 101000 and ventaArt <= 180000 and tProd == 's' or tProd == 'S'  # Comisión 8%
    e = ventaArt >= 101000 and ventaArt <= 180000 and tProd == 'm' or tProd == 'M'  # Comisión 9%
    f = ventaArt >= 101000 and ventaArt <= 180000 and tProd == 'l' or tProd == 'L'  # Comisión 10%
    g = ventaArt >= 181000 and ventaArt <= 230000 and tProd == 's' or tProd == 'S'  # Comisión 11%
    h = ventaArt >= 181000 and ventaArt <= 230000 and tProd == 'm' or tProd == 'M'  # Comisión 12%
    i = ventaArt >= 181000 and ventaArt <= 230000 and tProd == 'l' or tProd == 'L'  # Comisión 13%
    # Productos tipo A
    cArtAs = 0.05 
    cArtAm = 0.06
    cArtAl = 0.07
    # Productos tipo B
    cArtBs = 0.08
    cArtBm = 0.09
    cArtBl = 0.10
    # Productos tipo C
    cArtCs = 0.11
    cArtCm = 0.12
    cArtCl = 0.13
    # Gatos de Servicio
    gServA = 0.15
    gServB = 0.20
    gServC = 0.25
    # Gastos de servicio
    rCompraA = 0.40
    rCompraB = 0.45
    rCompraC = 0.50

    # Ganancias

    if a:                               # Venta producto tipo A 
        cProd = ventaArt * cArtAs
        gServicio = ventaArt * gServA
        rCompra = ventaArt * rCompraA
    elif b:
        cProd = ventaArt * cArtAm
        gServicio = ventaArt * gServA
        rCompra = ventaArt * rCompraA
    elif c:
        cProd = ventaArt * cArtAl
        gServicio = ventaArt * gServA
        rCompra = ventaArt * rCompraA
    elif d:                             # Venta producto tipo B
        cProd = ventaArt * cArtBs
        gServicio = ventaArt * gServB
        rCompra = ventaArt * rCompraB
    elif e:
        cProd = ventaArt * cArtBm
        gServicio = ventaArt * gServB
        rCompra = ventaArt * rCompraB
    elif f:
        cProd = ventaArt * cArtBl
        gServicio = ventaArt * gServB
        rCompra = ventaArt * rCompraB
    elif g:                             # Venta producto tipo C
        cProd = ventaArt * cArtCs
        gServicio = ventaArt * gServC
        rCompra = ventaArt * rCompraC
    elif h:
        cProd = ventaArt * cArtCm
        gServicio = ventaArt * gServC
        rCompra = ventaArt * rCompraC
    elif i:
        cProd = ventaArt * cArtCl
        gServicio = ventaArt * gServC
        rCompra = ventaArt * rCompraC
        
       
    diccionario_respuesta = {
        'idVenta': codigoVenta,                           # Código de artículo
        'vArticulo': ventaArt,                            # Valor en pesos del producto para la venta
        'cProducto': round(cProd, 2),                     # Comisión por venta del producto
        'gServicios': round(gServicio, 2),                # Gastos de servicios
        'rCompra': round(rCompra, 2)                      # Retención por costo del producto
    }
    
    return diccionario_respuesta

