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

#Casos de prueba

consultaRegistro(MesaServicios([
    ('11/12/2021','Luis Molero','BD','Terminado'),
    ('12/12/2021','Jose Molina','Call center','Terminado'),
    ('12/12/2021','Carlos Perez','Scripting','Pendiente'),
    ('13/12/2021','Carlos Perez','Interfaz','Revision')]), '12/12/2021')
print()
consultaRegistro(MesaServicios([
    ('14/12/2021','Julio Alvarez','BD','Pendiente'),
    ('14/12/2021','Jose Ramones','Impresión','Terminado'),
    ('15/12/2021','Carlos Perez','WIFI','Revision')]), '15/12/2021')
print()
consultaRegistro(MesaServicios([
    ('16/12/2021','Pedro Cañon','Impresión','Pendiente'),
    ('16/12/2021','Jacinto Perez','Scripting','Terminado'),
    ('16/12/2021','Peter Manjarres','BD','Sin atender'),
    ('16/12/2021','Diomendez Días','Impresión','Revisión'),
    ('16/12/2021','Silvestre Dangon','WIFI','Terminado')]), '17/12/2021')
print()
consultaRegistro(MesaServicios([
    ('18/12/2021','Julio Alvarez','BD','Pendiente'),
    ('18/12/2021','Jacinto Perez','Scripting','Terminado'),
    ('19/12/2021','Diomendez Días','Impresión','Revisión'),
    ('20/12/2021','Julio Alvarez','BD','Pendiente'),
    ('21/12/2021','Carlos Perez','WIFI','Revision')]), '19/12/2021')
print()
consultaRegistro(MesaServicios([
    ('22/12/2021','Luis Molero','BD','Terminado'),
    ('23/12/2021','Julio Alvarez','BD','Pendiente'),
    ('27/12/2021','Peter Manjarres','BD','Sin atender'),
    ('28/12/2021','Silvestre Dangon','WIFI','Terminado')]), '24/12/2021')
print()
consultaRegistro(MesaServicios([
    ('05/01/2022','Peter Manjarres','BD','Sin atender'),
    ('06/01/2022','Diomendez Días','Impresión','Revisión'),
    ('07/01/2022','Julio Alvarez','BD','Pendiente'),
    ('07/01/2022','Carlos Perez','WIFI','Revision')]), '07/01/2022')
print()
