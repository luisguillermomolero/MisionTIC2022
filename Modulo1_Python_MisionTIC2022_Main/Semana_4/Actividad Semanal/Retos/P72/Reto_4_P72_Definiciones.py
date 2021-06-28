def RegistroDiario(produccion):
    #Importar la funcion "reduce" desde la libreria "functools"
    from functools import reduce

    #Declarar constante "inrcementoProduccion"
    inrcementoProduccion = 30000000
    #Primer lambda que suma el total de cada tupla de cada lista
    producionDiaria = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), produccion))
    #Segundo lambda suma los totales de todas las tuplas de toda la lista
    producionDiaria = list(map(lambda x: [x[0]] + [reduce(lambda a,b: round(a + b,2), x[1:])], producionDiaria)) 
    #Tercer lambda que suma el incremento por produccion
    producionDiaria = list(map(lambda x: x if x[1] >= inrcementoProduccion else (x[0], x[1] + 50000), producionDiaria))

    print('------------------------ Inicio Registro diario ---------------------------------')
    #Ciclo para imprimir el total de cada compra
    for x in range(len(producionDiaria)):
        print(f'El registro diario número {producionDiaria[x][0]} tiene un monto total en pesos de {producionDiaria[x][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')