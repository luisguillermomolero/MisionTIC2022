from abc import ABC
from .empleado import Empleado

class Nomina():
    SALARIO_BASE = 1000


    def __init__(self):
        self.empleados = []
        

    
    def registrar_empleado(self, empleado):
        self.empleados.append(empleado)


    

    