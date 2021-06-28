##################
#Archivo con la descripción e implementación de la Clase Materia
##################

#Librerías para funcionalidades de la clase
from datetime import datetime

class Materia:    
    
    #Constructor(es) 
    ######################
    #Definen los atributos del objeto
    #Se inicializan los atributos
    def __init__(self,nota1=None,nota2=None,nota3=None,nota4=None,nota5=None,nombre=None,creditos=None):
        self.__nombre = nombre
        self.__creditos = creditos
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota3 = nota3
        self.__nota4 = nota4
        self.__nota5 = nota5
        self.__promedio5 = 0
        self.__promedio100 = 0
        self.__promedioAjustado5 = 0
        self.__promedioAjustado100 = 0 
        self.__docenteEncargado = '' 
        self.__notas = [ nota1, nota2, nota3, nota4 ]
        
               
    
    #Métodos (comportamiento del objeto)
    ################################### 
    def calcularPromedio5(self):
        sumatoria = 0
        sumatoria += self.__nota1.getNota5()
        sumatoria += self.__nota2.getNota5()
        sumatoria += self.__nota3.getNota5()
        sumatoria += self.__nota4.getNota5()
        sumatoria += self.__nota5.getNota5()
        self.__promedio5 = round( sumatoria/5 , 2 )
        
    def calcularPromedioAjustado5(self):
        listaNotas = [  self.__nota1.getNota5(),
                        self.__nota2.getNota5(),
                        self.__nota3.getNota5(),
                        self.__nota4.getNota5(),
                        self.__nota5.getNota5(),
                      ]        
        self.__promedioAjustado5 = (sum(listaNotas) - min(listaNotas)) / (len(listaNotas)-1)
        
    def calcularPromedio100(self):
        sumatoria = 0
        sumatoria += self.__nota1.getNota100()
        sumatoria += self.__nota2.getNota100()
        sumatoria += self.__nota3.getNota100()
        sumatoria += self.__nota4.getNota100()
        sumatoria += self.__nota5.getNota100()
        self.__promedio100 = round( sumatoria/5 , 2 )
        
    def calcularPromedioAjustado100(self):
        listaNotas = [  self.__nota1.getNota100(),
                        self.__nota2.getNota100(),
                        self.__nota3.getNota100(),
                        self.__nota4.getNota100(),
                        self.__nota5.getNota100(),
                      ]        
        self.__promedioAjustado100 = round( (sum(listaNotas) - min(listaNotas)) / (len(listaNotas)-1), 2)
    
    def adicionarNota(self,nota):
         self.__notas.append(nota)
    
    def mostrarUltimaNota(self):
        self.__notas[-1].mostrarInfoNota()
        
    def mostrarInfoMateria(self):
        print('------------------------')
        print('Curso: ', self.__nombre)
        print('Créditos: ', str(self.__creditos))       
        print('Promedio5: ', self.__promedio5)
        print('Promedio100: ', self.__promedio100)
        print('Promedio5Ajustado: ', self.__promedioAjustado5)
        print('Promedio100Ajustado: ', self.__promedioAjustado100) 
        
    def mostrarNotasMateria(self):
        for nota in self.__notas:
            nota.mostrarInfoNota()
    
    #Getters
    ########
    def getPromedio5(self):
        return self.__promedio5
    
    def getPromedioAjustado5(self):
        return self.__promedioAjustado5
    
    def getPromedio100(self):
        return self.__promedio100
    
    def getPromedioAjustado100(self):
        return self.__promedioAjustado100
    
    def getNotas(self):
        return self.__notas    
    
           
        print('------------------------')
    
    #Setters
    ########   
    
    
class OtraClase:
    pass
