#liquidación de pago semanal por horas
# Esta clase calcula el neto a pagar semanal para los trabajadopres por horas
# teniendo en cuenta las horas extras si trabaja mas de 40 horas semanales y los descuentos aplicables.

class nomina:
    def __init__(self, nombre, apellido, horas, vlr_hora, total, descuentos):

        self.nombre = nombre
        self.apellido = apellido
        self.horas = horas
        self.vlr_horas = vlr_hora
        self.total = total
        self.descuentos = descuentos

    def valor_horas_ (self):
        if self.horas <= 40:
            self.total = self.horas * self.vlr_horas
            print ("Valor a pagar " + str(self.total))
        else:
            self.total = (40 * self.vlr_horas) + ((self.horas-40) * (self.vlr_horas * 1.5))
            print ("Valor a pagar " + str(self.total))

    def deducciones_ (self):
        self.descuentos = self.total * 0.12 + self.total * 0.20
        print("Descuentos " + str(self.descuentos))

    def neto_pagar_ (self):
        print("Neto a pagar " + str(self.total - self.descuentos))


pago = nomina("Juan", "Perez", 40, 100000, 0, 0)
print(pago.nombre + " " + pago.apellido)
pago.valor_horas_()
pago.deducciones_()
pago.neto_pagar_()



