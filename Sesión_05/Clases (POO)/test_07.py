"""
Polimorfismo
"""

class Perro():
    def sonido(self):
        print("Guauu")

class Gato():
    def sonido(self):
        print("Miau")

class Vaca(Perro):
    def sonido(self):
        print("Muuu")

gato = Gato()
perro = Perro()
vaca = Vaca()

lista_animals = [perro, gato, vaca]

def canto(animales):
    for animal in animales:
        animal.sonido()

canto(lista_animals)

