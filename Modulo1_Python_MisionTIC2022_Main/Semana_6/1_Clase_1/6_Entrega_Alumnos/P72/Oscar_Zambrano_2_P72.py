# programa que permite validar si ula mascota requiere o no vacunacion
class mascota:
    # definimos el metodo inicial(constructor)
    # self inicializa los atributos de la instancia que se esta inicializando
    def __init__(self, Tipo_mascota, raza, edad, sexo, vacunas, color):
        # atributo, propiedad, o caracteristica de la clase "Empleado"
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        self.Tipo_mascota = Tipo_mascota
        self.vacunas = vacunas
        self.color = color
    def Requierevacunas(self):  # comportamiento, funcionalidad, metodo
        if self.vacunas < 3:
            print('___Su Mascota Requiere vacunación!!!____')
        else:
            print('Su mascota se encuentra al dia con las vacunas')

    def rasgos(self):
        print(self.color)
        print(self.sexo)


mypet = mascota('Gato', 'persa', '8 años', 'macho', '3', 'Cafe')
print('tipo mascota: ', mypet.Tipo_mascota)
print('sexo: ', mypet.rasgos)
print('vacunas: ', mypet.vacunas)
