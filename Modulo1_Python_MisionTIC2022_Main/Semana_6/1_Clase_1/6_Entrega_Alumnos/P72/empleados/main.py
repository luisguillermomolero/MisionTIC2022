from modelos.nomina import Nomina
from modelos.empleado import Empleado
import os
import json


def mostrar_menu():

    print('====== Entrada de Empleados ======\n')

    print('1. Registro de Empleados.')
    print('2. Mostrar Empleados.')
    print('0. Salir')

def capturar_entero(mensaje):
    while True:
        try:
            numero = int(input(f'{mensaje}: '))
            return numero
        except ValueError:
            print('*** Digite correctamente el número.\n')

def capturar_string(mensaje):
    while True:
        cadena = input(f'{mensaje}: ').strip()

        if len(cadena):
            return cadena
        else:
            print('*** Debe digitar los datos.')

def listar_empleados(empleados):
    dict_empleados = {}
    dict_empleados['empleados'] = []

    for i in empleados:
        dict_empleados['empleados'].append({'Documento': i.documento, 'Nombre': i.nombre, 'Correo': i.correo, 'Especialidad': i.especialidad})

    if len(dict_empleados['empleados']):
        return dict_empleados
    else:
        print('No hay registros...')
    
    
def cargar_nomina():
    with open('data.json') as file:
        data = json.load(file)
        return data

    for i in data['clients']:
        print('First name:', i['first_name'])
        print('Last name:', i['last_name'])
        print('Age:', i['age'])
        print('Amount:', i['amount'])
        print('')


def main():
    print('======================\n')

    nomina = Nomina()
    

    if os.path.isfile('nomina.json'):
        resultado = cargar_nomina()
        nomina.empleados = resultado
        
        
    while True:
        while True:
            try:
                mostrar_menu()
                opcion = int(input('\nDigite la operación a realizar: '))
                if 0 <= opcion <= 4:
                    break
                else:
                    print('\n*** Digite una opción entre 0 y 4\n')
            except ValueError():
                print('\n*** Debe digitar una opcion valida.\n')
        
        if opcion == 0:
            break

        elif opcion == 1:
            print('\n--- Registrar empleado. ---\n')

            documento = capturar_entero('Digite el documento')
            nombre = capturar_string('Digite el nombre')
            correo = capturar_string('Digite el correo')
            especialidad = capturar_string('Digite la especialidad')
            print()

            nuevo_empleado = Empleado(nombre, documento, correo, especialidad)

            nomina.registrar_empleado(nuevo_empleado)

            with open('data.json', 'w') as file:
                json.dump(listar_empleados(nomina.empleados), file, indent=4)

            
            
        elif opcion == 2:
            print('\n--- Mostrar empleados. ---\n')

            if os.path.isfile('data.json'):
                with open('data.json') as file:
                    data = json.load(file)

                    for i in data['empleados']:
                        print('Documento:', i['Documento'])
                        print('Nombre:', i['Nombre'])
                        print('Correo:', i['Correo'])
                        print('Especialidad:', i['Especialidad'])
                        print('')
                
            else: 
                print('No hay registros...\n')


    print('\n=== El programa ha finalizado ===')
    
    print('\n======================')

if __name__ == '__main__':
    main()