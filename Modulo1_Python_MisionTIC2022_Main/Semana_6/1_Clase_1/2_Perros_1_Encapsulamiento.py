class Perros(object): #Declaramos la clase principal Perros
    #Definimos el método inicial (constructor)
    def __init__(self, nombre, peso): #Definimos los parámetros 
        self.__nombre = nombre #Declaramos los atributos (privados ocultos)
        self.__peso = peso
    @property  #intercepta la escritura, lectura o borrado de los atributos y permite incorporar documentación sobre los mismos.
    def nombre(self): #Definimos el método para obtener el nombre
        "Documentación del método nombre" # Doc del método
        return self.__nombre #Aquí simplemente estamos retornando el atributo privado oculto
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
        
        #Hasta aquí property#
    def peso(self):    #Definimos el método para obtener el peso
        return self.__peso #Aquí simplemente estamos retornando el atributo privado
#Instanciamos
Tomas = Perros('Tom', 27)
print (Tomas.nombre) #Imprimimos el nombre de Tomas. Se hace a través de getter
#Que en este caso como esta luego de property lo toma como el primer método..
Tomas.nombre = 'Tomasito' #Cambiamos el atributo nombre que se hace a través de setter
del Tomas.nombre #Borramos el nombre utilizando deleter



#Getter: Se encargará de interceptar la lectura del atributo. (get = obtener)
#Setter : Se encarga de interceptar cuando se escriba. (set = definir o escribir)
#Deleter : Se encarga de interceptar cuando es borrado. (delete = borrar)
#doc :  Recibirá una cadena para documentar el atributo. (doc = documentación)