def Agendamiento(eventos: list):
    agenda={} #Inicializar diccionario
    for fEvento,hEvento,aEvento in eventos:          #Ciclo para agregar un nuevo evento
        if agenda.get(fEvento) == None:             #Fuerza la entrada
            agenda[fEvento] = []                    #Creacion de un nuevo evento
        agenda[fEvento].append((hEvento, aEvento))   #Registro de una nueva lista de tuplas en el dict agenda
    return agenda

def consultaRegistro(agenda, fechaEvento):          #Definición de función consulta
    if fechaEvento in agenda:                       #Ubicar una fecha dentro de la agenda
        for horaEvento,actividadEvento in agenda[fechaEvento]: #Muestra todos los registros encontrados
            print('Registro consultado: * Hora:', horaEvento,'* Actividad:',actividadEvento)
    else:                                           #Si no ubica coincidencia de registros
        print("No hay actividades agendadas para dicha fecha")
