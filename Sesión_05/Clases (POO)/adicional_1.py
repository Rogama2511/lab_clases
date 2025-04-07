"""
Ejercicio resuelto (POO)

Requisitos:
- Se pide crear la clase Confeccionista.
- Deberá tener los métodos de:
* Prendas máxima por día
* Cobro por la cantidad de prendas ya terminadas
* Bolsa (recaudación que tienes en soles por la cantidad de prendas ya realizadas)
* Pagado (aquí se actualizará la cantidad que ya le pagaron al confeccionista)

Tomar en cuenta lo siguiente:
- El constructor iniciará con: cantidad_prendas, pago_total y pago_realizado
- En el método de prendas máximo por día tendrá la condicional que si se quiere hacer
 una prenda más al máximo el método indicará que está indispuesto

"""

class Confeccionista:
    def __init__(self, cantidad_prendas, pago_total, pago_realizado):
        self.cantidad_prendas = cantidad_prendas  # total de prendas terminadas
        self.pago_total = pago_total              # total que debería recibir por todas las prendas
        self.pago_realizado = pago_realizado      # lo que ya se le pagó
        self.maximo_diario = 10                   # puedes ajustar este valor según el caso

    def prendas_maximo_por_dia(self, prendas_hoy):
        if prendas_hoy > self.maximo_diario:
            return "Indispuesto: no se puede hacer más de {} prendas por día.".format(self.maximo_diario)
        else:
            return "Producción del día aceptada: {} prendas.".format(prendas_hoy)

    def cobro_por_prendas(self, precio_unitario):
        total = self.cantidad_prendas * precio_unitario
        return "Total por {} prendas terminadas: S/ {}".format(self.cantidad_prendas, total)

    def bolsa(self, precio_unitario):
        recaudacion = self.cantidad_prendas * precio_unitario
        return "Bolsa actual: S/ {}".format(recaudacion)

    def pagado(self, nuevo_pago):
        self.pago_realizado += nuevo_pago
        return "Pago actualizado. Total pagado: S/ {}".format(self.pago_realizado)


# Uso instanciando la clase:
conf = Confeccionista(cantidad_prendas=20, pago_total=300.0, pago_realizado=100.0)

# Usando sus respectivos métodos
print(conf.prendas_maximo_por_dia(12))  # Excede el máximo
print(conf.cobro_por_prendas(15))       # Supón que cada prenda vale S/15
print(conf.bolsa(15))                   # Mismo precio por prenda
print(conf.pagado(50))                  # Se le paga 50 soles de la deuda
