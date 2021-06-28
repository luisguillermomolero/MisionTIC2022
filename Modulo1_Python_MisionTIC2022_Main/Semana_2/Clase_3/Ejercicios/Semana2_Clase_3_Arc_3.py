#Ejemplo 1

# Función para calcular el promedio de 4 notas

def promedioNotas(nota1, nota2, nota3, nota4):
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    return promedio
print('El promedio es de: ', promedioNotas(3.0, 2.1, 5.0, 4.7))

#Ejemplo 2

# Encapsulamiento con Diccionario


def promedioNotas2(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas['Nota1']
    sumatoria += dicNotas['Nota2']
    sumatoria += dicNotas['Nota3']
    sumatoria += dicNotas['Nota4']
    promedio = round(sumatoria / 4, 2)
    return promedio

dicNotas = {}
dicNotas ['Nota1'] = 3.0
dicNotas ['Nota2'] = 2.1
dicNotas ['Nota3'] = 5.0
dicNotas ['Nota4'] = 4.7
print('El promedio es de: ', promedioNotas2(dicNotas))

#Ejemplo 3

# Encapsulamiento con Diccionario - Otra notación

def promedioNotas3(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas['Nota1']
    sumatoria += dicNotas['Nota2']
    sumatoria += dicNotas['Nota3']
    sumatoria += dicNotas['Nota4']
    promedio = round(sumatoria / 4, 2)
    return promedio

dicNotas = {
    'Nota1' : 3.0,
    'Nota2' : 2.1,
    'Nota3' : 5.0,
    'Nota4' : 4.7
}

print('El promedio es de: ', promedioNotas3(dicNotas))

#Ejemplo 4

#Paso entre funciones

def reportePromedio(dicReporte):
    return dicReporte['estudiante'] + ' = ' + str(dicReporte['promedio'])

def generarReporteNotas(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas['Nota1']
    sumatoria += dicNotas['Nota2']
    sumatoria += dicNotas['Nota3']
    sumatoria += dicNotas['Nota4']
    promedio = round(sumatoria/4, 2)
    reporteNotas = {
        'promedio':promedio,
        'estudiante':dicNotas['estudiante']
    }
    return reporteNotas

dicNotas = {
    'estudiante': 'Beneficiario Rodriguez',
    'Nota1' : 3.0,
    'Nota2' : 2.1,
    'Nota3' : 5.0,
    'Nota4' : 4.7
}

print(reportePromedio(generarReporteNotas(dicNotas)))

