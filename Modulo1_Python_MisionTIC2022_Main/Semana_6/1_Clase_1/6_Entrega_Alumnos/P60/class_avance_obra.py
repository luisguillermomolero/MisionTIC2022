#Calcula los rendimientos y avances diarios de de obra a partir de la meta a cumplir y el rendimiento
#esperado. Para establecerlos valores toma los reportes diarios de cantidades instaladas y tiempo empleado

class avanceObra:

    def __init__(self, meta, instalado, tiempo, rendimiento, avance): 
        self.meta = meta
        self.instalado = instalado
        self.tiempo = tiempo
        self.rendimiento = rendimiento
        self.avance = avance
    def verificaMeta(self):
        if self.meta==1500:
           print("La cantidad de meta a instalar  es 1500 y esta correcta")
        else:
            print("Ajuste la meta a 1500")
    def calculaRendimiento(self):
        rend=(self.instalado/self.tiempo)
        if self.rendimiento<=rend>=3:
           print("El rendimiento está en lo planeado")
        else:
            print("Hay desviaciones en la ejecución")    
    def calculaAvance(self):
        avan=(self.instalado/self.meta)*100
        if avan>=self.avance:            
            print("El avance es "+str(avan)+" % y está dentro de lo planificado")
        else:
            print("Se debe revisar el rendimiento porque se presentan retrasos en la ejecución")

reporteDia = avanceObra(1500,1150,480,2.5,90.5)  # Instanciando la clase avanceObra()

print(reporteDia.meta)              
print(reporteDia.instalado)
print(reporteDia.tiempo)
print(reporteDia.rendimiento)  
print(reporteDia.avance)            
