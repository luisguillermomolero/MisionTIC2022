#Aplicación CRUD (Controlador) - Lista de Tareas Pendientes
###########################################################

#Librerías (capas)
import CRUD #Capa lógica o backend básico
import InterfazConsola as ic #Interfaz para interacción con el usuario UI
import sys #API para comunicar la App con funciones del sistema operativo

#Carga de la base de datos de la aplicación (archivo json)
tareas = CRUD.Read()
if not(tareas): #Si no se obtiene el listado de tareas del archivo json (Base de Datos)
    sys.exit(1) #Terminación de la App reportando error

#Iniciar Mainloop de la App
#--------------------------
mainloop = True
while mainloop:

    #Solicitar a la interfaz la selección de una opción
    opcion = ic.formularioMenuAppCRUD()
    
    #Si Create fue seleccionado por el usuario en el menú
    if opcion == 1:        

        #Solicitar a la interfaz mostrar el mensaje
        ic.mensaje("->Adicionando Tarea")

        #Presentar formulario para encapsular ingreso de datos en diccionario tareaNueva
        identificador,tareaNueva = ic.formularioAdicionarTarea()
        
        #Adicionar la tarea al contenedor
        CRUD.Create(tareas, identificador, tareaNueva)        
        
    #Si el listado general de tareas fue solicitado por el usuario
    elif opcion == 2:

        #Solicitar a la interfaz mostrar el mensaje
        ic.mensaje("->Listado de Tareas")       

        #Solicitar a la interfaz que muestre la base de datos de tareas cargada
        ic.mostrarTareas(tareas)              
        
    #Si Update fue seleccionado por el usuario en el menú
    elif opcion == 3:

        #Solicitar a la interfaz mostrar el mensaje
        ic.mensaje("->Actualizar Tarea")       

        #Presentar formulario de actualización de tareas
        respuestaInterfaz = ic.formularioActualizarTarea(tareas)

        #Si la interfaz preparó la actualización
        if respuestaInterfaz != False:
            #Desempacar información de la respuesta
            identificador,tareaActualizada = respuestaInterfaz
            #Realizar la actualización
            CRUD.Update(tareas, identificador, tareaActualizada)

    #Si Delete fue seleccionado por el usuario en el menú
    elif opcion == 4:

        #Solicitar a la interfaz mostrar el mensaje
        ic.mensaje("->Eliminar Tarea") 

        #Presentar formulario de eliminación de tareas
        identificador = ic.formularioEliminarTarea(tareas)

        #Si la interfaz preparó la eliminación
        if identificador != False:            
            #Realizar la eliminación si llega autorización desde la interfaz (identificador)
            CRUD.Delete(tareas,identificador)    

    #Si la opcíon de salida fue seleccionadA por el usuario en el menú    
    elif opcion == 5:
        
        #Solicitar a la interfaz mostrar el mensaje
        ic.mensaje("->Eliminar Tarea") 

        #Guardar el listado de tareas en la base de datos (archivo json)
        if CRUD.Write(tareas):            
            #Solicitar a la interfaz reporte de salida exitosa            
            ic.mensaje("Datos guardados: Cierre exitoso.")
        
        #Terminar el mainloop de la aplicación
        mainloop = False
    
    else:

        #Solicitar a la interfaz mostrar el mensaje
        ic.mensaje("Opción inválida!")