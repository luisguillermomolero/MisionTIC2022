def MesaServicios(incidencias: list):
    #Inicializar diccionario
    incidencia={}
    #Ciclo para agregar un nuevo evento
    for fIncidencia, uIncidencia, tSoporte, eIncidencia  in incidencias:
        #Fuerza la entrada
        if incidencia.get(fIncidencia) == None:                           
            #Creacion de un nuevo evento
            incidencia[fIncidencia] = []                                  
        #Registro de una nueva lista de tuplas en el dict agenda
        incidencia[fIncidencia].append((uIncidencia, tSoporte, eIncidencia))                 
    return incidencia
#Definición de función consulta
def consultaRegistro(incidencias, fIncidencia):
    #Ubicar una fecha dentro de la agenda
    if fIncidencia in incidencias:
        for uIncidencia, tSoporte, eIncidencia in incidencias[fIncidencia]:
            #Muestra todos los registros encontrados
            print('Fecha consultada ', fIncidencia, ' Usuario Incidencia ', uIncidencia, ' Tipos Soporte ', tSoporte, ' Estado Incidencia ', eIncidencia)
    else:
        #Si no ubica coincidencia de registros
        print("No hay registro de incidencia para ese día")
