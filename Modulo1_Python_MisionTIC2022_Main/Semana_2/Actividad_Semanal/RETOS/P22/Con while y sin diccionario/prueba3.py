aMat = aFis = aPro = aGeo = aHis = 0.0   # Acumulador de aprobados 
aMmat = aMfis = aMpro = 0                # Número Aprobados por materia
apMmat = apMfis = apMpro = 0             # Número aplazados por materia
aT = 0                                   # Número de alumnos que aprobaron todas las materias
aU = aUa = aUb = aUc = 0                 # Número de alumnos que aprobaron una sola materia
aDos = aDd = aDe = aDf = 0               # Número de alumnos que aprobaron dos materias
i = 1

var = int(input('ingrese alumnos '))

while i <= var:
    cMat = float(input('Ingrese calificación matematica '))
    cFis = float(input('Ingrese calificación Física '))
    cPro = float(input('Ingrese calificación Programación '))
    
    
    aMat += cMat
    pMat = aMat/var
    aFis += cFis
    pFis = aFis/var
    aPro += cPro
    pPro = aPro/var
    
    i +=1

    # Cantidad alumnos aprobados/aplazados matemática
    if cMat >= 3:
        aMmat += 1
    else:
        apMmat += 1
    
    # Cantidad alumnos aprobados/aplazados física
    if cFis >= 3:
        aMfis += 1
    else:
        apMfis += 1
    
    # Cantidad alumnos aprobados/aplazados programación
    if cPro >= 3:
        aMpro += 1
    else:
        apMpro += 1
    
    # Cantidad de alumnos que aprobaron todas las materias
    if cMat >= 3 and cFis >= 3 and cPro >= 3:
        aT += 1

    # alumnos que aprobaron al menos una materia
    a = cMat >= 3 and cFis <= 2 and cPro <= 2
    b = cMat <= 2 and cFis >= 3 and cPro <= 2
    c = cMat <= 2 and cFis <= 2 and cPro >= 3

    if a:
        aUa +=1
    elif b:
        aUb += 1
    elif c:
        aUc +=1
    aU = aUa + aUb +aUc

# alumnos que aprobaron dos materia

    d = cMat >= 3 and cFis >= 3 and cPro <= 2
    e = cMat >= 3 and cFis <= 2 and cPro >= 3
    f = cMat <= 2 and cFis >= 3 and cPro >= 3

    if  d:
        aDd += 1
    elif e:
        aDe += 1
    elif f:
        aDf += 1
    aDos = aDd + aDe + aDf

# Nota promedio de cada materia.
print(pMat, pFis, pPro)

# Número de alumnos aprobados y aplazados en cada materia.
print('cantidad aprobados matematica ' + str(aMmat) + ' cantidad aplazados ' + str(apMmat))
print('cantidad aprobados física ' + str(aMfis) + ' cantidad aplazados ' + str(apMfis))
print('cantidad aprobados programación ' + str(aMpro) + ' cantidad aplazados ' + str(apMpro))

# Número de alumnos que aprobaron todas las materias
print('Alumnos que aprobaron todas ' + str(aT))

# Número de alumnos que aprobaron una sola materia
print('Alumnos que aprobaron 1 materia ' + str(aU))

# Número de alumnos que aprobaron dos materias
print('Alumons que aprobaron dos materias : ' + str(aDos))
