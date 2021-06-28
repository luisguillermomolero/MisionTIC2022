def Agendamiento(eventos: list):
    agenda={} #Inicializar diccionario
    for fEvento,hEvento,aEvento in eventos:         #Ciclo para agregar un nuevo evento
        if agenda.get(fEvento) == None:             #Fuerza la entrada
            agenda[fEvento] = []                    #Creacion de un nuevo evento
        agenda[fEvento].append((hEvento, aEvento))  #Registro de una nueva lista de tuplas en el dict agenda
    return agenda

#Casos de prueba

Agendamiento([
    ('25/12/2021','9:30am','Universidad'),
    ('26/12/2021','8:30am','Desayuno'),
    ('26/12/2021','12:30pm','Almuerzo')])
print()
