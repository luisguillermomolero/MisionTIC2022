#Librería para interacción por consola (interfaz)
#################################################

#Presentar mensaje genérico en pantalla
def mensaje(info=''):
    print()
    print(info)
    print()

#Formulario menú aplicación CRUD
def formularioMenuAppCRUD():
    print(" ")
    print("-- Aplicación CRUD TareasPendientes ---")
    print("1. Adicionar Tarea")
    print("2. Consultar Tareas")
    print("3. Actualizar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")

    #Capturar la opción validando el tipo de dato para retornarlo al controlador
    opcion = None
    while opcion == None:
        try:
            opcion = int(input("Ingrese una opción: "))
        except:        
            print("Entrada inválida: Se debe ingresar una opción numérica.")    

    #Retornar opción al controlador
    return opcion

#Función de validación en la colección recibida del controlador           
def estaElemento(identificador, tareas):
    
    #Extraer de la base de datos (contenedor) los identificadores
    conjuntoIdentificadores = set(tareas.keys())
    
    #Revisar si se encuentra el elemento solicitado        
    if identificador in conjuntoIdentificadores:
        return True
    else:
        return False 

#Formulario para adicionar tareas (Create)
def formularioAdicionarTarea():
    #Recoger los campos de la tarea
    identificador = input("Ingrese identificador de la Tarea: ")
    descripcion = input("Ingrese descripción de Tarea: ")
    estado = input("Ingrese el estado inicial de la Tarea: ")
    #Capturar el tiempo validando el tipo de dato ingresado
    tiempo = None
    while tiempo == None:
        try:
            tiempo = int(input("Ingrese el tiempo de realización: "))
        except:
            print("Entrada inválida: Se debe ingresar un tiempo numérico.")
    #Encapsular la nueva tarea
    tareaNueva = {
                    'descripcion' : descripcion,
                    'estado' : estado,
                    'tiempo' : tiempo                 
                }
    #Retornar al controlador el identificador y la nueva tarea
    return identificador,tareaNueva

#Formulario para actualización de tareas
def formularioActualizarTarea(tareas):   

    #Solicitar al usuario el identificador
    identificador = input("Ingrese identificador de la Tarea para modificar: ")
    
    #Revisar si se encuentra el elemento solicitado        
    if estaElemento(identificador, tareas):

        #Recolectar los nuevos datos        
        nuevaDescripcion = str(input('Nueva descripción: '))        
        nuevoEstado = str(input('Nuevo estado: '))        

        #Capturar el tiempo validando el tipo de dato ingresado        
        nuevoTiempo = '' #Alternativa a nulo, para conservar el tiempo anterior        
        try:
            nuevoTiempo = int(input('Nuevo tiempo de realización: '))
        except:
            print("Entrada inválida: Se debe ingresar un tiempo numérico.")

        #Encapsular la tarea actualizada
        tareaActualizada = {
                            'descripcion' : nuevaDescripcion,
                            'estado' : nuevoEstado,
                            'tiempo' : nuevoTiempo         
                            }

        #Retornar el identificador de la tarea con los campos actualizados
        return identificador,tareaActualizada

    else:

        print("No ha sido encontrada la Tarea para actualización!")
        return False

#Formulario para eliminación de tareas
def formularioEliminarTarea(tareas):

    #Solicitar al usuario el identificador
    identificador = input("Ingrese identificador de la Tarea para eliminar: ")
    
    #Revisar si se encuentra el elemento solicitado para autorizar eliminado en el controlador    
    if estaElemento(identificador, tareas):
        #Retornar la bandera y el identificador para que el controlador elimine
        return identificador    
    else:
        print("No ha sido encontrada la Tarea para eliminación!")
        return False

#Presentación de las tareas que llegan del controlador
def mostrarTareas(tareas):
    for identificador, tarea in tareas.items():    
        print(identificador,' - ',end='')
        for nombre_atributo, atributo in tarea.items():
            print(atributo, ', ', end='')
        print()

