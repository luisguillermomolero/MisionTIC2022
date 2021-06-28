class electronica():
    def __init__(self):
        self.leyohm = "La ley de ohm es basica para entender el funcionamiento de los circuitos electricos \n se denota como V = I * R \n"
        self.resist = "Vamos a calcular la resistencia a partir del voltaje y la resistencia \n en un circuito electrico \n"
    def mensaje(self):  
        print(self.leyohm)  
        print(self.resist)

class resistencia(figura):
    def __init__(self):
        self.volta = "\nVamos a calcular ahora el voltaje a partir de la corriente y la resistencia \n en un circuito electrico \n"
        self.volt = float(input("Ingrese un voltaje:"))
        self.corr = float(input("Ingrese una coriente:"))
    def mensaje(self):
        print("La resistencia del circuito es: "+ str(self.volt/self.corr)+'Ω')
        print(self.volta)
class voltaje(figura):
    def __init__(self):
        self.corri = "\nVamos a calcular ahora la corriente a partir del voltaje y la resistencia \n en un circuito electrico \n"
        self.res = float(input("Ingrese una resistencia:"))
        self.corr = float(input("Ingrese una coriente:"))
    def mensaje(self):
        print("El voltaje del circuito es: "+ str(self.res*self.corr)+'V')
        print(self.corri)

class corriente(figura):
    def __init__(self):
        self.res = float(input("Ingrese una resistencia:"))
        self.volt = float(input("Ingrese una coriente:"))
    def mensaje(self):
        print("La corriente del circuito es: "+ str(self.volt/self.res)+'A\n')
        print("Gracias por utilizar esta herramienta ")



circuito = electronica()
circuito.mensaje()

resistencia = resistencia()
resistencia.mensaje()

voltaje = voltaje()
voltaje.mensaje()

corriente = corriente()
corriente.mensaje()


#Para enviar el archivo: nombre del archivo: suNombreCompleto_Grupo_Dia.py
#correo: luisguillermomolero@gmail.com
