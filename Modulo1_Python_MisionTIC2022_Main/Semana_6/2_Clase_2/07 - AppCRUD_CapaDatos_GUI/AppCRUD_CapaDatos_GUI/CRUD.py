#Librería con la lógica de las operaciones CRUD
###############################################

import json

#Adición de una tarea (Create)
def Create(tareas, identificador, tareaNueva):    
    tareas[identificador] = tareaNueva #Mutación del diccionario por referencia      

#Consultar la información de todas las tareas (Read)
def Read(rutaArchivo='listadoTareas.json'):

    #Cargar el listado de tareas a un diccionario desde la capa de datos (archivo JSON)    
    diccionarioTareas = {}#Contenedor del listado de tareas que gestiona la App
    try:    
        with open(rutaArchivo) as archivo:
            diccionarioTareas = json.load(archivo)
    except:
        print("No se pudo cargar la información de la capa de datos")
        return False #Reportar fallo en la carga

    #Retornar el contenedor o colección obtenido
    return diccionarioTareas

#Actualizar una tarea específica (Update)
def Update(tareas, identificador, tareaActualizada):
    #Revisar los campos que llegan con información para actualizar
    for id_campo, campo in tareaActualizada.items():        
        if campo:
            tareas[identificador][id_campo] = campo #Actualizar el campo del diccionario (referencia)

#Eliminar una tarea específica (Delete)
def Delete(tareas, identificador):
    tareas.pop(identificador)

#Operación de escritura en la capa de datos al cierre de la aplicación
def Write(tareas, rutaArchivo='listadoTareas.json'):
    #Descargar contenedor de datos con las modificaciones realizadas por la App
    try:
        with open(rutaArchivo, 'w') as archivo_json:
            json.dump(tareas, archivo_json)
    except:
        print("Error: No se pudo guardar la información en la capa de datos.")
        return False
    
    #Si la escrutra fue exitosa retorno correspondiente
    return True