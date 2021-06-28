def Agendamiento(fecha,hora,actividad):
    agenda={} #Inicializar diccionario
    nuevaFecha = 's' #Fuerza la entrada de una fecha al while
    while nuevaFecha =='s':
        nuevaActividad = 's' #Fuerza la entrada de una nueva actividad 
        registro = [] #Inicializar lista
        while nuevaActividad == "s":
            registro.append((hora,actividad))
            nuevaActividad = 'n'
        agenda[fecha] = registro
        nuevaFecha = 'n'
    print(agenda)
    return agenda

def consultaRegistro(agenda, fecha):
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print('Registro consultado: * Hora: ', hora,'* Actividad: ',actividad)
    else:
        print("No hay actividades agendadas para dicha fecha")
    


consultaRegistro(Agendamiento('25/12/2021','9:30am','Universidad'), fecha='25/12/2021')
consultaRegistro(Agendamiento('27/12/2021','10:30PM','Comer'), fecha='26/12/2021')
