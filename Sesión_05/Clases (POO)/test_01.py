"""Programacion orientada a objetos"""

class Carro:
     """Atributo"""
     rueda = 4

     """Constructor: Valores que van a tomar por defecto mi clase que se instancia a una variables"""
     def __init__(self, color, aceleracion):
         self.color = color
         self.aceleracion = aceleracion
         self.velocidad = 0

     """Métodos: son las funciones de las clases"""

     def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

     def frenar(self):
        self.velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = self.velocidad


"""Instanciamos nuestra clase"""
carro_1 = Carro('Negro', 60)
print("El color del primer carro es:{}".format(carro_1.color))
print("La aceleración del primer carro es:{}".format(carro_1.aceleracion))
print("La cantidad de ruedad que tiene el carro 1: {}".format(carro_1.rueda))


carro_2 = Carro('Azul', 80)
print("El color del segundo carro es:{}".format(carro_2.color))
print("La aceleración del segundo carro es:{}".format(carro_2.aceleracion))
print("La cantidad de ruedad que tiene el carro 2: {}".format(carro_2.rueda))

