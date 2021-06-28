class Empleado:

    def __init__(self,nombre:str,sueldo:float,edad:int,cargo:str) -> None:
        self.nombre = nombre
        self.sueldo = sueldo
        self.edad = edad
        self.cargo = cargo
    
    def getNombre(self):
        print(f'El empleado se llama {self.nombre}')
    
    def getSueldo(self):
        print(f'El empleado devenga {self.sueldo}')
    
    def getEdad(self):
        print(f'El empleado tiene {self.edad} años')
    
    def getCargo(self):
        print(f'El empleado es {self.cargo}')    

    
    def pagarImpuestos(self):
        if self.sueldo>3000:
            print('Debe pagar impuestos')
        else:
            print('No debe pagar impuestos')


cont: bool = True
empleados = dict()
while cont:
    nombre: str = input('Ingrese el nombre de un empleado: ')
    sueldo: float = float(input(f'Ingrese el salario de {nombre}: '))
    edad: int = int(input(f'Ingrese la edad de {nombre}: '))
    cargo: str = input(f'Ingrese el cargo de {nombre}: ')

    emple = Empleado(nombre,sueldo,edad,cargo)
    emple1 = {nombre:emple}
    empleados.update(emple1)

    print('\n')

    cont2= True

    while cont2:
        print('Presione 1 para ingresar un nuevo empleado')
        print('Presione 2 para dejar de ingresar empleado')

        opc: str = input('Seleccione una opción: ')

        if opc == '1':
            cont = True
            cont2 = False
        elif opc == '2':
            cont = False
            cont2 = False
        else:
            print('Ingrese una opción válida \n')
            cont2 = True
    
    print('\n')

cont = True
while cont:
    nombre = input('Digite el nombre un Empleado para Consultar: ')

    try:
        emple:Empleado = empleados.get(nombre)
        emple.getNombre()
        emple.getSueldo()
        emple.getEdad()
        emple.getCargo()
        emple.pagarImpuestos()

        print('\n')

        cont2 = True

        while cont2:
            opc: str = input('Desea salir (S/N): ')
            opc = opc.lower()

            if opc=='s':
                print('Hasta pronto \n')
                cont = False
                cont2 = False
            elif opc=='n':
                cont = True
                cont2 = False
            else:
                print('Ingrese una opción válida \n')
                cont2 = True
    except:
        print('Nombre no encontrado, intente de nuevo \n')