def TarjetaAlumnos (Tarjetas:dict)-> dict:
    
    #Variables
    aT = 0                                     # Número de alumnos que aprobaron todas las materias
    aU = aUa = aUb = aUc = 0                   # Número de alumnos que aprobaron una sola materia
    aDos = aDd = aDe = aDf = 0                 # Número de alumnos que aprobaron dos materias
    aId  = Tarjetas['idAlumno']                # idAlumno
    cMat = Tarjetas['cMatematica']             # Calificacion Matemática
    cFis = Tarjetas['cFisica']                 # Calificacion Física
    cPro = Tarjetas['cProgramacion']           # Calificacion Programación
    a = cMat >= 3 and cFis <= 2 and cPro <= 2  # P/Tabla de verdad 1
    b = cMat <= 2 and cFis >= 3 and cPro <= 2  # P/Tabla de verdad 1
    c = cMat <= 2 and cFis <= 2 and cPro >= 3  # P/Tabla de verdad 1
    d = cMat >= 3 and cFis >= 3 and cPro <= 2  # P/Tabla de verdad 2
    e = cMat >= 3 and cFis <= 2 and cPro >= 3  # P/Tabla de verdad 2
    f = cMat <= 2 and cFis >= 3 and cPro >= 3  # P/Tabla de verdad 2
    g = cMat >= 3 and cFis >= 3 and cPro >= 3  # P/Tabla de verdad 3

    # alumnos que aprobaron al menos una materia

    if a:
        aUa +=1
    elif b:
        aUb += 1
    elif c:
        aUc +=1
    aU = aUa + aUb +aUc

    # alumnos que aprobaron dos materia
    if  d:
        aDd += 1
    elif e:
        aDe += 1
    elif f:
        aDf += 1
    aDos = aDd + aDe + aDf

    # Cantidad de alumnos que aprobaron todas las materias
    if g:
        aT += 1
    
   
    diccionario_respuesta = {
        'idAlumno': aId,
        'aproboUna': aU,
        'aproboDos': aDos,
        'aproboTodas': aT
    }
    
    return diccionario_respuesta

Tarjetas = {
    'idAlumno': 1001,
    'cMatematica': 3,
    'cFisica': 4,
    'cProgramacion': 3
}

print(TarjetaAlumnos(Tarjetas))

Tarjetas = {
    'idAlumno': 1002,
    'cMatematica': 3,
    'cFisica': 2,
    'cProgramacion': 2
}

print(TarjetaAlumnos(Tarjetas))

Tarjetas = {
    'idAlumno': 1003,
    'cMatematica': 1,
    'cFisica': 2,
    'cProgramacion': 2
}

print(TarjetaAlumnos(Tarjetas))

Tarjetas = {
    'idAlumno': 1004,
    'cMatematica': 3,
    'cFisica': 3,
    'cProgramacion': 2
}

print(TarjetaAlumnos(Tarjetas))

Tarjetas = {
    'idAlumno': 1005,
    'cMatematica': 2,
    'cFisica': 2,
    'cProgramacion': 3
}

print(TarjetaAlumnos(Tarjetas))

Tarjetas = {
    'idAlumno': 1006,
    'cMatematica': 2,
    'cFisica': 3,
    'cProgramacion': 2
}

print(TarjetaAlumnos(Tarjetas))

Tarjetas = {
    'idAlumno': 1007,
    'cMatematica': 2,
    'cFisica': 3,
    'cProgramacion': 3
}

print(TarjetaAlumnos(Tarjetas))

Tarjetas = {
    'idAlumno': 1008,
    'cMatematica': 3,
    'cFisica': 3,
    'cProgramacion': 3
}

print(TarjetaAlumnos(Tarjetas))