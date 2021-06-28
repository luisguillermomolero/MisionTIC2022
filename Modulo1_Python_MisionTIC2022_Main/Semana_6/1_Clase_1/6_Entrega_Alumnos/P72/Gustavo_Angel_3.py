#GUTSAVO ADOLFO ANGEL LOAIZA
#prorgrama que sirve para verificar los distintos tratamientos o seguimientos que debe tener
#un paciente dependienddo de su edad y condicion clinica

class Clinica:

    def __init__(self, aplicar_vacuna, pyp, odontologia, diabetes, ht, adulto_mayor):

        self.nombre = input('ingrese nombre paciente: ')
        self.apellido = input('ingrese apellido paciente:')
        self.edad = int(input('ingrese edad del paciente: '))
        self.adulto_mayor = adulto_mayor
        self.aplicar_vacuna = aplicar_vacuna
        self.pyp = pyp
        self.odontologia= odontologia
        self.diabetes = diabetes
        self.ht = ht

    def aplicar_vacunas(self):
        if self.edad >= 1: 
            print('Ud se debe aplicar 5 vacunas.')
        else:
            print('El paciente recibira otro tratamiento.')

    def verificar_adulto_mayor(self):
        if self.edad > 70:
            print('el paciente pasa a conuslta de control con medico')
        else:
            print('el paciente pasa a consulta de control con enfermera jefe')

    def verificar_pyp(self):
        if self.edad > 15:
            print('aplicar triple viral')
        else:
            print('aplicar tetanos')
    def verificar_odontologia(self):
        if self.edad < 8:
            print('se remite a higienen oral')
        else: 
            print('revision por odontologia')
    
    def verificar_diabetes(self):
        if self.edad == 'control mensula':
            print('debe estar encontrol mensual')
            print('debe recibir medicamentos de control')
    
    def verificar_ht(self):
        if self.edad >= 0:
            print('debe estar en continuo control')

paciente = Clinica('Polio', 'control mensual', 'higiene oral', 'control bimestral', 'control trimestral', 'control mensual')

paciente.aplicar_vacunas()
paciente.verificar_adulto_mayor()
paciente.verificar_pyp()
paciente.verificar_odontologia()
paciente.verificar_diabetes()
