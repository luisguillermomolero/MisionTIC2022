#Librería para interacción por consola (interfaz)
#################################################

#Librerías con las clases para construir los widgets (ventanas, botones, cambos, labels, etc)
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Librerías de apoyo
import pprint as pp

#Librería para interactuar con el backend
import CRUD

#Función para crear la tabla de tareas en la estructura tipo treeview
def generarTablaListadoTareas(m,tareas):

    #Instanciado del treeview, permite jerarquía pero se utilizará como una tabla para las tareas
    TablaTareas = ttk.Treeview(m)

    #Especificación de las columnas
    TablaTareas['columns'] = ('ID', 'Descripción', 'Estado', 'Tiempo')
    TablaTareas.column('#0', width=0, stretch=tk.NO)
    TablaTareas.column('ID', anchor=tk.CENTER, width=80)
    TablaTareas.column('Descripción', anchor=tk.CENTER, width=80)
    TablaTareas.column('Estado', anchor=tk.CENTER, width=80)
    TablaTareas.column('Tiempo', anchor=tk.CENTER, width=80)

    #Especificación del encabezado
    TablaTareas.heading('#0', text='', anchor=tk.CENTER)
    TablaTareas.heading('ID', text='ID', anchor=tk.CENTER)
    TablaTareas.heading('Descripción', text='Descripción', anchor=tk.CENTER)
    TablaTareas.heading('Estado', text='Estado', anchor=tk.CENTER)
    TablaTareas.heading('Tiempo', text='Tiempo', anchor=tk.CENTER)

    #Insertar el listado de tareas cargado en memoria proveniente de la capa de datos en la tabla
    indiceNumerico = 0
    for identificador, tarea in tareas.items():
        TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, tarea['descripcion'], tarea['estado'], tarea['tiempo']) )
        indiceNumerico += 1    

    #Ubicar en la interfaz
    TablaTareas.pack()

    #Retornar el objeto para las actualizaciones que se generen por los eventos
    return TablaTareas 

#Función para creación de la ventana o menú principal
def ventanaMenuPrincipal(tareas):

    #Crear el objeto de la ventana principal
    m = tk.Tk()
    m.title('App CRUD Lista Tareas')#Especificar el título de la ventana       

    ######## Composición de widgets y procedimientos para el funcionamiento de la interfaz ########

    #Crear los marcos para agrupar visualmente los widgets
    marcoCargaBorrado = ttk.Frame(m, borderwidth=2, relief="raised", padding=(10,10))
    #marcoCargaBorrado = ttk.Frame(m, borderwidth=2, relief="raised")
    #marcoCargaBorrado.pack()
    #marcoCargaBorrado.grid(column=0, row=0)

    #Crear tabla de tareas
    TablaTareas = generarTablaListadoTareas(m,tareas)

    #Agregar entradas para los atributos de las tareas

    #Id Tarea
    etiquetaId = tk.Label(m, text = 'ID')
    #etiquetaId = tk.Label(marcoCargaBorrado, text = 'ID')
    etiquetaId.pack()
    entradaId = tk.Entry(m)
    entradaId.pack()

    #Descripción Tarea
    etiquetaDescripcion = tk.Label(m, text = 'Descripción')
    etiquetaDescripcion.pack()
    entradaDescripcion = tk.Entry(m)
    entradaDescripcion.pack()
    
    #Estado Tarea
    etiquetaEstado = tk.Label(m, text = 'Estado')
    etiquetaEstado.pack()
    entradaEstado = tk.Entry(m)
    entradaEstado.pack()

    #Tiempo Tarea
    etiquetaTiempo = tk.Label(m, text = 'Tiempo')
    etiquetaTiempo.pack()
    entradaTiempo = tk.Entry(m)
    entradaTiempo.pack() 

    #Función que limpia los campos de la interfaz
    def limpiarCampos():        
        entradaId.delete(0,tk.END)
        entradaDescripcion.delete(0,tk.END)
        entradaEstado.delete(0,tk.END)
        entradaTiempo.delete(0,tk.END)    

    #Botón para limpiar los campos
    tk.Button(m, text='Limpiar Campos', command = limpiarCampos  ).pack()

    #Cargar información de la tarea seleccionada
    def cargarTareaSeleccionada():        
        
        #Extraer información de la interfaz
        seleccionada = TablaTareas.focus()
        infoSeleccionada = TablaTareas.item(seleccionada, 'values')

        #Limpiar los campos
        limpiarCampos()

        #Cargar la información extraída
        entradaId.insert(0,infoSeleccionada[0])        
        entradaDescripcion.insert(0,infoSeleccionada[1])        
        entradaEstado.insert(0,infoSeleccionada[2])
        entradaTiempo.insert(0,infoSeleccionada[3])
    
    #Botón para cargar la tarea seleccionada
    tk.Button(m, text='Cargar Info Tarea Seleccionada', command = cargarTareaSeleccionada).pack() 

    ######## Composición de widgets y procedimientos para las operaciones CRUD en la Interfaz ########  

    #Función intermediaria para preparar información recogida de los campos como la espera el CRUD
    #Redirige la información a los eventos especificados en los botones
    def encapsularInfoFormulario(accion):

        #Obtener el identificador de las entradas
        identificador = entradaId.get()

        #Intentar convertir el tiempo a tipo entero
        try:
            entradaTiempoFormatoEntero = int(entradaTiempo.get())
        except:
            #Colocar un valor por defecto si no es posible realizar el parseo
            entradaTiempoFormatoEntero = 0
        
        #Encapsular información
        infoCampos = {            
            'descripcion' : entradaDescripcion.get(),
            'estado' : entradaEstado.get(),
            'tiempo' : entradaTiempoFormatoEntero
        }

        #Revisar evento del botón para iniciar las acciones correspondientes en las otras capas
        if accion == "Create":

            #Llamar la función que realiza la actualización de la vista y el backend
            adicionarTarea(TablaTareas, tareas, identificador, infoCampos)
        
        elif accion == "Update":
            
            #Llamar la función que realiza la actualización de la vista y el backend
            actualizarTarea(TablaTareas, tareas, identificador, infoCampos)
        
        elif accion == "Delete":
            
            #Llamar la función que realiza la actualización de la vista y el backend
            eliminarTarea(TablaTareas, tareas, identificador, infoCampos)
    
    #Función que realiza la adición de la tarea en la vista y el backend
    def adicionarTarea(TablaTareas, tareas, identificador, tareaNueva):  

        #Actualizar el widget correspondiente en la interfaz
        indiceNumerico = len(TablaTareas.get_children())   
        TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, tareaNueva['descripcion'], tareaNueva['estado'], tareaNueva['tiempo']) )

        #Llamar el backend para actualizar el contenedor de las tareas
        CRUD.Create(tareas, identificador, tareaNueva) 

    #Botón para adición de tarea, desencadenando los eventos en las demás capas    
    tk.Button(m, text='Adicionar Tarea', command = lambda : encapsularInfoFormulario("Create")  ).pack()

    #Función que realiza la actualización de la tarea cargada en la vista y el backend
    def actualizarTarea(TablaTareas, tareas, identificador, tareaNueva):    

        #Actualizar el widget correspondiente en la interfaz
        indiceNumerico = len(TablaTareas.get_children())   
        TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, tareaNueva['descripcion'], tareaNueva['estado'], tareaNueva['tiempo']) )

        #Eliminar todos los elementos (filas o hijos)
        for i in TablaTareas.get_children():
            TablaTareas.delete(i)
        
        #Actualizar el contenedor cargado en memoria
        CRUD.Update(tareas, identificador, tareaNueva)

        #Insertar en la vista todas las tareas que están cargadas en memoria
        indiceNumerico = 0
        for identificador, tarea in tareas.items():
            TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, tarea['descripcion'], tarea['estado'], tarea['tiempo']) )
            indiceNumerico += 1   
    
    #Botón para actualización de tarea, desencadenando los eventos en las demás capas    
    tk.Button(m, text='Actualizar Tarea', command = lambda : encapsularInfoFormulario("Update")  ).pack()

    #Función que realiza la eliminación de la tarea cargada en la vista y el backend
    def eliminarTarea(TablaTareas, tareas, identificador, tareaNueva):    

        #Actualizar el widget correspondiente en la interfaz
        indiceNumerico = len(TablaTareas.get_children())   
        TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, tareaNueva['descripcion'], tareaNueva['estado'], tareaNueva['tiempo']) )

        #Eliminar todos los elementos (filas o hijos)
        for i in TablaTareas.get_children():
            TablaTareas.delete(i)
        
        #Actualizar el contenedor cargado en memoria
        CRUD.Delete(tareas, identificador)        

        #Insertar en la vista todas las tareas que están cargadas en memoria posterior a la eliminación
        indiceNumerico = 0
        for identificador, tarea in tareas.items():
            TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, tarea['descripcion'], tarea['estado'], tarea['tiempo']) )
            indiceNumerico += 1  

    #Botón para eliminación de tarea, desencadenando los eventos en las demás capas    
    tk.Button(m, text='Eliminar Tarea', command = lambda : encapsularInfoFormulario("Delete")  ).pack()
    
    #Función que guarda los cambios y cierra la aplicación
    def salirGuardar():

        #Solicitar al backend que actualice la base de datos
        CRUD.Write(tareas)

        #Informar a través de la interfaz gráfica
        messagebox.showinfo(message="Información guardada", title="Cierre Sesión")       

        #Cerrar la ventana
        m.destroy()

    #Botón para salir y guardar cambios
    tk.Button(m, text='Salir y Guardar', command = salirGuardar  ).pack()
    
    #Retornar la ventana construída con todos los elementos y funcionalidades, al controlador para que inicie el mainloop
    return m