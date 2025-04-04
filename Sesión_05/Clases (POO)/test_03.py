"""Programacion orientada a objetos

Ulitizacion de métodos"""

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
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

carro_1 = Carro('Azul', 70)
print(carro_1.velocidad)
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()

print("La velocidad actual en el carro 1 es: {}".format(carro_1.velocidad))

carro_1.frenar()
carro_1.frenar()
print("La velocidad del carro 1 es: {}".format(carro_1.velocidad))
