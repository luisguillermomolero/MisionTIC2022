def Agendamiento(eventos: list):
    agenda = {} #Inicializar diccionario
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

#Casos de prueba

consultaRegistro(Agendamiento([
    ('25/12/2021','9:30am','Universidad'),
    ('26/12/2021','8:30am','Desayuno'),
    ('26/12/2021','12:30pm','Almuerzo')]), '24/12/2021')
print()
consultaRegistro(Agendamiento([
    ('15/12/2021','9:30am','Universidad'),
    ('16/12/2021','7:15am','Desayuno'),
    ('16/12/2021','10:00am','Universidad'),
    ('16/12/2021','2:00pm','Estudiar'),
    ('17/12/2021','4:00pm','Homework'),
    ('19/12/2021','5:15am','Ejercicios'),
    ('19/12/2021','8:00am','Desayuno'),
    ('19/12/2021','11:45am','Gym'),
    ('19/12/2021','2:00am','Universidad'),
    ('19/12/2021','5:45am','Cine'),
    ('19/12/2021','10:30pm','Cena')]), '19/12/2021')
print()
consultaRegistro(Agendamiento([
    ('25/12/2021','9:30am','Universidad'),
    ('26/12/2021','8:30am','Desayuno'),
    ('26/12/2021','12:30pm','Almuerzo')]), '26/12/2021')
print()
consultaRegistro(Agendamiento([
    ('20/12/2021','9:30am','Universidad'),
    ('21/12/2021','8:30am','Desayuno'),
    ('22/12/2021','12:30pm','Almuerzo')]), '26/12/2021')
print()
consultaRegistro(Agendamiento([
    ('22/12/2021','9:30am','Universidad'),
    ('22/12/2021','8:30am','Desayuno'),
    ('22/12/2021','12:30pm','Almuerzo')]), '22/12/2021')
print()
consultaRegistro(Agendamiento([
    ('19/12/2021','9:30am','Universidad'),
    ('21/12/2021','8:30am','Desayuno'),
    ('26/12/2021','12:30pm','Almuerzo')]), '19/12/2021')
print()


