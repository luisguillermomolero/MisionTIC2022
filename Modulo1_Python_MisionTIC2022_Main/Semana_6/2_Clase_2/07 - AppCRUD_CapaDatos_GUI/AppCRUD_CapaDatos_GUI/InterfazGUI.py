#Librería para interacción por consola (interfaz)
#################################################

#Librerías con las clases para construir los widgets (ventanas, botones, cambas, labels, etc)

# https://docs.python.org/es/3/library/tk.html

import tkinter as tk #Proporciona un conjunto de herramientas robusto e independiente de la plataforma para administrar ventanas.
from tkinter import ttk #Widgets temáticos
from tkinter import messagebox #Clase base de plantilla para cuadros de mensaje.

#Librería para interactuar con el backend
import CRUD

#Función para crear la tabla de tareas en la estructura tipo treeview
def generarTablaListadoTareas(marcoInteraccion,tareas):

    #Instanciado del treeview, permite jerarquía pero se utilizará como una tabla para las tareas
    TablaTareas = ttk.Treeview(marcoInteraccion)

    #Especificación de las columnas
    TablaTareas['columns'] = ('ID', 'Descripción', 'Estado', 'Tiempo')
    TablaTareas.column('#0', width=0, stretch=tk.NO)
    TablaTareas.column('ID', anchor=tk.CENTER, width=40)
    TablaTareas.column('Descripción', anchor=tk.W, width=300)
    TablaTareas.column('Estado', anchor=tk.W, width=100)
    TablaTareas.column('Tiempo', anchor=tk.CENTER, width=80)

    #Especificación del encabezado
    TablaTareas.heading('#0', text='', anchor=tk.CENTER)
    TablaTareas.heading('ID', text='ID', anchor=tk.CENTER)
    TablaTareas.heading('Descripción', text='Descripción', anchor=tk.W)
    TablaTareas.heading('Estado', text='Estado', anchor=tk.CENTER)
    TablaTareas.heading('Tiempo', text='Tiempo', anchor=tk.CENTER)    

    #Insertar el listado de tareas cargado en memoria proveniente de la capa de datos en la tabla
    indiceNumerico = 0
    for identificador, tarea in tareas.items():
        TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, tarea['descripcion'], tarea['estado'], tarea['tiempo']) )
        indiceNumerico += 1       

    #Retornar el objeto para las actualizaciones que se generen por los eventos
    return TablaTareas 

#Función para creación de la ventana o menú principal
def ventanaMenuPrincipal(tareas):

    #Crear el objeto de la ventana principal
    m = tk.Tk()
    m.title('App CRUD Lista Tareas')#Especificar el título de la ventana       

    ######## Composición de widgets y procedimientos para el funcionamiento de la interfaz ########

    #Crear los marcos para agrupar visualmente los widgets
    marcoInteraccion = ttk.Frame(m, borderwidth=2, relief="raised", padding=(10,10))#Formulario    
    marcoCRUD = ttk.Frame(m, borderwidth=2, relief="raised", padding=(10,10))#Acciones   

    #Crear tabla de tareas
    TablaTareas = generarTablaListadoTareas(marcoInteraccion,tareas)

    #Agregar entradas para los atributos de las tareas

    #Id Tarea    
    etiquetaId = tk.Label(marcoInteraccion, text = 'ID:')    
    entradaId = tk.Entry(marcoInteraccion)   

    #Descripción Tarea
    etiquetaDescripcion = tk.Label(marcoInteraccion, text = 'Descripción:')    
    entradaDescripcion = tk.Entry(marcoInteraccion)    
    
    #Estado Tarea
    etiquetaEstado = tk.Label(marcoInteraccion, text = 'Estado:')    
    entradaEstado = tk.Entry(marcoInteraccion)    

    #Tiempo Tarea
    etiquetaTiempo = tk.Label(marcoInteraccion, text = 'Tiempo:')    
    entradaTiempo = tk.Entry(marcoInteraccion)   

    #Función que limpia los campos del formulario (marcoInteraccion)
    def limpiarCampos():        
        entradaId.delete(0,tk.END)
        entradaDescripcion.delete(0,tk.END)
        entradaEstado.delete(0,tk.END)
        entradaTiempo.delete(0,tk.END)    

    #Botón para limpiar los campos
    btnLimpiarCampos = tk.Button(marcoInteraccion, text='Limpiar Campos', command = limpiarCampos )

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
    btnCargarTareaSeleccionada = tk.Button(marcoInteraccion, text='Cargar Info Tarea Seleccionada', command = cargarTareaSeleccionada)

    #Ubicación de los elementos (frame para el formulario) de interacción en la ventana principal 
    marcoInteraccion.grid(column=0, row=0)    
    TablaTareas.grid(column=0,row=0,columnspan=3)    
    etiquetaId.grid(column=0,row=1,sticky=tk.W)
    entradaId.grid(column=1,row=1)
    etiquetaDescripcion.grid(column=0,row=2,sticky=tk.W)
    entradaDescripcion.grid(column=1,row=2)
    etiquetaEstado.grid(column=0,row=3,sticky=tk.W)
    entradaEstado.grid(column=1,row=3)
    etiquetaTiempo.grid(column=0,row=4,sticky=tk.W)
    entradaTiempo.grid(column=1,row=4)
    btnCargarTareaSeleccionada.grid(column=2,row=2)
    btnLimpiarCampos.grid(column=2,row=3)    

    ######## Composición de widgets y procedimientos para las operaciones CRUD en la Interfaz ########  

    #Función intermediaria para preparar información recogida de los campos como la espera el CRUD
    #Redirige la información encapsulada a los eventos especificados en los botones
    #Será utilizada por todas las operaciones Create, Update y Delete
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

        #Actualizar la interfaz acorde a la operación solicitada

        #Limpiar los campos de la interfaz
        limpiarCampos() 

        #Actualizar el widget correspondiente en la interfaz
        indiceNumerico = len(TablaTareas.get_children())   
        TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, tareaNueva['descripcion'], tareaNueva['estado'], tareaNueva['tiempo']) )

        #Llamar el backend para actualizar el contenedor de las tareas
        CRUD.Create(tareas, identificador, tareaNueva) 

    #Botón para adición de tarea, desencadenando los eventos en las demás capas    
    btnAdicionarTarea = tk.Button(marcoCRUD, text='Adicionar Tarea', command = lambda : encapsularInfoFormulario("Create")  )

    #Función que realiza la actualización de la tarea cargada en la vista y el backend
    def actualizarTarea(TablaTareas, tareas, identificador, tareaNueva):

        #Actualizar la interfaz acorde a la operación solicitada

        #Limpiar los campos de la interfaz
        limpiarCampos()        

        #Eliminar todos los elementos (filas o hijos) de la tabla de la interfaz
        for i in TablaTareas.get_children():
            TablaTareas.delete(i)
        
        #Actualizar el contenedor cargado en memoria (llamado a backend)
        CRUD.Update(tareas, identificador, tareaNueva)

        #Insertar en la vista todas las tareas que están cargadas en memoria
        indiceNumerico = 0
        for identificador, tarea in tareas.items():
            TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, tarea['descripcion'], tarea['estado'], tarea['tiempo']) )
            indiceNumerico += 1   
    
    #Botón para actualización de tarea, desencadenando los eventos en las demás capas    
    btnActualizarTarea = tk.Button(marcoCRUD, text='Actualizar Tarea', command = lambda : encapsularInfoFormulario("Update")  )

    #Función que realiza la eliminación de la tarea cargada en la vista y el backend
    def eliminarTarea(TablaTareas, tareas, identificador, tareaNueva):    

        #Actualizar la interfaz acorde a la operación solicitada

        #Limpiar los campos de la interfaz
        limpiarCampos() 

        #Eliminar todos los elementos (filas o hijos) de la tabla de la interfaz
        for i in TablaTareas.get_children():
            TablaTareas.delete(i)
        
        #Actualizar el contenedor cargado en memoria (llamado a backend)
        CRUD.Delete(tareas, identificador)        

        #Insertar en la vista todas las tareas que están cargadas en memoria posterior a la eliminación
        indiceNumerico = 0
        for identificador, tarea in tareas.items():
            TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, tarea['descripcion'], tarea['estado'], tarea['tiempo']) )
            indiceNumerico += 1
    
    #Botón para eliminación de tarea, desencadenando los eventos en las demás capas    
    btnEliminarTarea = tk.Button(marcoCRUD, text='Eliminar Tarea', command = lambda : encapsularInfoFormulario("Delete")  )
    
    #Función que guarda los cambios y cierra la aplicación
    def salirGuardar():

        #Solicitar al backend que actualice la base de datos
        CRUD.Write(tareas)

        #Informar a través de la interfaz gráfica
        messagebox.showinfo(message="Información guardada en capa de datos", title="Cierre Sesión")       

        #Cerrar la ventana
        m.destroy()

    #Botón para salir y guardar cambios
    btnSalirGuardar = tk.Button(marcoCRUD, text='Salir y Guardar', command = salirGuardar  )

    #Carga de imagen para asociar a widget tipo etiqueta    
    from PIL import ImageTk,Image #Librería para procesar formato png y redimensionar
    #Proporciones de la imagen
    w = 120 
    h = 140   
    imagenCargada = Image.open("imagenListaTareas.png")#Carga de la imagen
    imagenCargada.thumbnail((w,h))#Redimensionado de la imagen a las proporciones establecidas
    imagenListaTareas = ImageTk.PhotoImage(imagenCargada)#Encapsular para tkinter
    #Creación de la etiqueta 
    etiquetaImagenListaTareas = tk.Label(marcoCRUD)
    #Asociación de la imagen a la etiqueta    
    etiquetaImagenListaTareas.config(image=imagenListaTareas, width=w, height=h)    
    etiquetaImagenListaTareas.image = imagenListaTareas

    #Etiqueta informativa funcionamiento App
    mensajeFuncionamiento = "-> Cargar Info antes de CRUD"
    etiquetaFuncionamiento = tk.Label(marcoCRUD,text=mensajeFuncionamiento)
    
    #Ubicación de los botones del CRUD    
    marcoCRUD.grid(column=1, row=0, rowspan=5, sticky=tk.N+tk.S)
    etiquetaImagenListaTareas.grid(column=1,row=0,sticky=tk.W+tk.E)    
    btnAdicionarTarea.grid(column=1,row=1, sticky=tk.W+tk.E)
    btnActualizarTarea.grid(column=1,row=2, sticky=tk.W+tk.E)
    btnEliminarTarea.grid(column=1,row=3, sticky=tk.W+tk.E)
    btnSalirGuardar.grid(column=1,row=4, sticky=tk.W+tk.E)
    etiquetaFuncionamiento.grid(column=1,row=5)    
    
    #Retornar la ventana de la App construída con todos los elementos y funcionalidades al controlador, para que inicie el mainloop
    return m