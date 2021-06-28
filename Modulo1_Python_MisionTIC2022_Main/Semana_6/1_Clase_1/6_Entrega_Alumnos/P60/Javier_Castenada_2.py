#Javier Felipe Castañeda Sanchez
#Desarrollar una clase con al menos 5 atributos, adicional, 4 métodos + el constructor,
# entregando el objeto al momento de instanciar la clase con la variable. 
# No olvidar, colocar su nombre como autor de la app y el enunciado.

#Programa que permite saber que requerimientos cumple una persona para pensionarse


print("Requerimientos para pensionarse\n")
class empleado:
    def __init__(self, nombre,edad,salario,semanas_cot,años_trab): #metodo

        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.semanas_cot = semanas_cot
        self.años_trab = años_trab

    def calculoedad (self):
        if self.edad > 60:
            print("Por su edad ",self.nombre," es apt@ para pensionarse")
        else:
            print("Por su edad ",self.nombre," no es apt@ para pensionarse")

    def calculosalario (self):
        if self.salario > 1000:
            self.salario1=self.salario*2
            print("El salario para pensionarse seria: ",self.salario1)
        else:
            self.salario2=self.salario
            print("El salario para pensionarse seria: ",self.salario2)

    def calculosemanas_cot (self):
        if self.semanas_cot > 100:
            print(self.nombre," cumple con las semanas cotizadas requeridas para pensionarse")
        else:
            print(self.nombre," no cumple con las semanas cotizadas requeridas para pensionarse")

    def calculoaños_trab (self):
        if self.años_trab > 20:
            print(self.nombre," cumple con los años trabajados requeridos para pensionarse")
        else:
            print(self.nombre," no cumple con los años trabajados requeridos para pensionarse")

empleado1 = empleado('Carlos',65,1500,10,15)  # Instanciando la clase 
print(empleado1.nombre)

empleado1.calculoedad()
empleado1.calculosalario()
empleado1.calculosemanas_cot()
empleado1.calculoaños_trab()