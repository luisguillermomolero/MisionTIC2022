def datosPersonales (Ficha:dict)-> dict:
    
    uCe  = Ficha['Cedula']
    uNom = Ficha['Nombre']
    uApe = Ficha['Apellido']
    uCor = Ficha['Correo']
    
    # Condición de fealdad

    if uCe <= 500000:
        condicion = 'Feo'
    else:
        condicion = 'Buena persona'        


    dicSalida =  {
        'Cedula': uCe,
        'Condicion': condicion
    }
    
    return dicSalida

Ficha = {
    'Cedula': 102000,
    'Nombre': 'Luis',
    'Apellido': 'Molero',
    'Correo': 'elsabroso@gmail.com'
}

print(datosPersonales(Ficha))

Ficha = {
    'Cedula': 10200300,
    'Nombre': 'Calos',
    'Apellido': 'Perdomo',
    'Correo': 'batequebrado@yahoo.es'
}

print(datosPersonales(Ficha))