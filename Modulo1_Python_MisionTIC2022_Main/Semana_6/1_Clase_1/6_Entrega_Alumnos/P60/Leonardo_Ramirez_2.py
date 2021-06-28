#Programa que permite conocer el estado de un alumno matriculado en una universidad, 
# todos los datos internos para seguimiento del estudiante internamente.

#Autor: Leonardo E. Ramirez

class estudiante:

    def __init__(self, nombre, codigo, edad, sexo, jornada, tipo):

        self.nombre = nombre
        self.codigo = codigo
        self.edad = edad
        self.sexo = sexo
        self.jornada = jornada
        self.tipo = tipo

    def edad_ (self):

        if self.edad > 18:
            print('Es Mayor de Edad')
        else:
            print('Es Menor de Edad')

    def sexo_ (self):

        if self.sexo == 'Masculino':
            print('Es Hombre')
        else:
            print('Es Mujer')
    def jornada_ (self):

        if self.jornada == 'AM':
            print('Mañana')
        else:
            print('Tarde')

    def tipo_ (self):

        if self.tipo_ == 'V':
            print('Virtual')
        else:
            if self.tipo_ == 'P':
                print('Presencial')
            else:
                print('No esta Matriculado')


unestudiante = estudiante('Javier Lopez', str(1012), 19, 'Masculino', 'AM', 'V') 

print('El nombre del estudiante es: ', unestudiante.nombre)
print('El codigo del estudiante es: ', unestudiante.codigo)
unestudiante.edad_()
unestudiante.sexo_()  
unestudiante.jornada_()
unestudiante.tipo_()      

