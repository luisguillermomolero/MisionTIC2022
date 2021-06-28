def Creditos(prestamos):
    #Importar la funcion "reduce" desde la libreria "functools"
    from functools import reduce

    #Declarar constante "ordenMinimaDiaria"
    ordenMinimaDiaria = 200000000
    #Primer lambda que suma el total de cada tupla de cada lista
    ordenTotal = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), prestamos))
    #Segundo lambda suma los totales de todas las tuplas de toda la lista
    ordenTotal = list(map(lambda x: [x[0]] + [reduce(lambda a,b: round(a + b,2), x[1:])], ordenTotal)) 
    #Tercer lambda que suma el incremento de 200000 pesos
    ordenTotal = list(map(lambda x: x if x[1] >= ordenMinimaDiaria else (x[0], x[1] + 200000), ordenTotal))

    print('------------------------ Inicio Registro diario ---------------------------------')
    #Ciclo para imprimir el total diario
    for x in range(len(ordenTotal)):
        print(f'El préstamo de número {ordenTotal[x][0]} es de un total en pesos de {ordenTotal[x][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')

