#Este programa nos ayuda validar por edad si esta priorizado para  la vacunacion
#  #Autor: edwin velandia

class vacunacion:

    def __init__(self, nombre, edad, genero, horario, vacuna):

        self.Nombre = nombre
        self.Edad = edad
        self.Genero = genero
        self.Horario=horario
        self.Vacuna = vacuna   
    
    
    def nombre(self):
        print("Nombre: ",self.Nombre)


    def edad (self):

        if self.Edad < 18:
            print('usted  es menor Edad no esta agendado debe esperar la fase 4',self.Edad)
        elif self.Edad >18 and self.Edad < 50:
            print('Debe llamar para agendar la cita',self.Edad)
    
        if self.Edad > 50:
            print('es priorizado para vacunarse agendese',self.Edad)

    def genero (self):

        if self.Genero == 'Masculino':
            print("hombre,Le pertenece la zona norte",self.Genero)
        else:
            print("mujer,Le pertenece zona centro",self.Genero)
    
    def horario (self):

        if self.Horario == 'A':
            print('Mañana',self.Horario)
        else:
            print('Tarde',self.Horario)

    def vacuna (self):
        if self.Vacuna == 0:
            print('primera dosis',self.Vacuna)
        elif self.Vacuna ==1:
            print('segunda dosis',self.Vacuna)
                
        else:    
            print('ya se encuntra vacunado')



vacunante = vacunacion("sandro",20,"Masculino","p",0)
vacunante.nombre()
vacunante.edad()
vacunante.genero()
vacunante.horario()
vacunante.vacuna()