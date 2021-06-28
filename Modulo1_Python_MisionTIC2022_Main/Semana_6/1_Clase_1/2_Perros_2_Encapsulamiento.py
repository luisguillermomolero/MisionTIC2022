# -*- coding: utf-8 -*-
class Perros(object): #Declaramos la clase principal Perros
    def __init__(self, nombre, peso): #Definimos los parámetros 
        self.__nombre = nombre #Declaramos los atributos
        self.__peso = peso
    @property
    def nombre(self): #Definimos el método para obtener el nombre
        "Documentación del método nombre" # Doc del método
        return self.__nombre #Aquí simplemente estamos retornando el atributo privado
#Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
#Ahora vamos a utilizar setter y deleter para modificarlos
    @nombre.setter #Propiedad SETTER
    def nombre(self, nuevo):
        print ("Modificando nombre..")
        self.__nombre = nuevo
        print ("El nombre se ha modificado por")
        print (self.__nombre) #Aquí vuelvo a pedir que retorne el atributo para confirmar
    @nombre.deleter #Propiedad DELETER
    def nombre(self): 
        print("Borrando nombre..")
        del self.__nombre
        
    @property
    def peso(self):    #Definimos el método para obtener el peso #Automáticamente GETTER
        return self.__peso #Aquí simplemente estamos retornando el atributo privado
    @peso.setter
    def peso(self, nuevopeso):
        self.__peso = nuevopeso
        print ("El peso ahora es")
        print (self.__peso)
    @peso.deleter #Propiedad DELETER
    def peso(self): 
        print("Borrando peso..")
        del self.__peso
#Instanciamos
Tomas = Perros('Tom', 27)
print (Tomas.nombre) #Imprimimos el nombre de Tomas. Se hace a través de getter
#Que en este caso como esta luego de property lo toma como el primer método..
Tomas.nombre = 'Tomasito' #Cambiamos el atributo nombre que se hace a través de setter
print (Tomas.nombre) #Volvemos a imprimir
Tomas.peso = 28
del Tomas.nombre #Borramos el nombre utilizando deleter