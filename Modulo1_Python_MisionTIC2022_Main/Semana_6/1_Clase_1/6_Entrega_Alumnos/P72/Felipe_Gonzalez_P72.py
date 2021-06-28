
class Estudiante:      
         
    def __init__(self): 
        self.nombre = input("Ingrese el nombre del estudiante:")             
        self.carrera = str(input("Ingrese la carrera a  la que pertenece:"))                
    
    def imprimir(self):               
        print("Nombre:",self.nombre)         
        print("Carrera:",self.carrera)      
    
    def entrada_laboratorio(self):           
        if self.carrera=='Electronica' or self.carrera=='Sistemas' or 'Electrónica':             
            print("El estudiante puede entrar al laboratorio las 24 horas")         
        else:             
            print(f"El estudiante {self.nombre} no está autorizado a entrar al laboratorio en horario no hábil")  
    
    # bloque principal  
            

estudiante1 = Estudiante()  
estudiante1.imprimir() 
estudiante1.entrada_laboratorio()
