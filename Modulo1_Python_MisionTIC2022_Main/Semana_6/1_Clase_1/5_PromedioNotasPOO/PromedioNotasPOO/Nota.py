##################
#Archivo con la descripción e implementación de la Clase Nota
##################

#Librerías para funcionalidades de la clase
from datetime import datetime

class Nota:
    
    #Atributos públicos (modificables desde afuera de la clase)
    ######################
    modeloPedagogico = 'Auto-estructurante'
    
    #Constructor(es) 
    ######################
    #Definen los atributos del objeto
    #Se inicializan los atributos
    def __init__(self,nota5=None,nota100=None,descripcion=None):
        self.__nota100 = nota100
        self.__descripcion = descripcion
        self.__fechaRegistro = datetime.now()
        self.__notaCualitativa = None
        if not(nota100 == None):
            #Cualitativa
            if nota100 > 60:
                self.__notaCualitativa = 'Aprobado'
            else:
                self.__notaCualitativa = 'Reprobado'
            #Realizar conversión desde el constructor
            self.__nota5 = (nota100 * 5)/100
        else:
            self.__nota5 = nota5          
    
    #Métodos (comportamiento del objeto)
    ################################### 
    def convertirNota_5_100(self):
        pass
    
    def convertirNota_100_5(self):
        pass
    
    def convertirNota_100_Cualitativa(self):
        pass
    
    #Getters
    ########
    def getNota5(self):
        return self.__nota5
    
    def getNota100(self):
        return self.__nota100
    
    def getNotaCualitativa(self):
        return self.__notaCualitativa
    
    def getFechaRegistro(self):
        return str(self.__fechaRegistro)
    
    def getDescripcion(self):
        return self.__descripcion
    
    def mostrarInfoNota(self):
        print('------------------------')
        print('Descripción: ', self.__descripcion)
        print('Fecha Registro: ', str(self.__fechaRegistro))
        print('Nota Cualitativa: ', self.__notaCualitativa)
        print('Nota Escala 100: ', self.__nota100)
        print('Nota Escala 5: ', self.__nota5)
        print('------------------------')
    
    #Setters
    ########
    def setNota5(self,nota5):
        pass
    
    def setNota100(self,nota100):
        pass
    
    def setDescripcion(self,descripcion):
        self.__descripcion = descripcion