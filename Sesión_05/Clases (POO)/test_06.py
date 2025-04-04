"""
POO en python: Encapsulamiento
"""


class A:
    def __init__(self):
        self.inicial = 10
        self._contador = 0 #Definiendo mi atributo privado

    def incrementa(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador
class B:
    """Encapsulamiento """
    def __init__(self):
        self.inicial = True
        self.__contador = 0 #Definiendo encapsulamiento fuerte

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador

var_1 = A()
var_1._contador
var_1.inicial = 20

var_1.incrementa()
var_1.incrementa()

print("El valor actual de mi atributo _contador es: {}".format(var_1._contador))
print("El valor inicial de A: {}".format(var_1.inicial))
print("Contador de A: {}".format(var_1._contador))

var_2 = B()
var_2.inicial = False

var_2.incrementa()
var_2.incrementa()
var_2.incrementa()
var_2.incrementa()

print("Valor del contador B es: {}".format(var_2.cuenta()))
print("Valor inicial de B es: {}".format(var_2.inicial))

"""IMPORTANTE: No es posible invocar a una variable porque su encapsulamiento es fuerte por los dos guiones"""
#print(var_2.__contador)