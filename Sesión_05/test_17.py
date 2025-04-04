"""Uso de método ramdom"""

import random

numero = random.randint(1, 100)
print(numero)

mi_lista = []

for elemento in range(10):
    #le concedemos un valor aleatorio entre el 1 y 30
    elemento = random.randint(1, 30)
    #agregamos el numero aleatorio a la lista
    mi_lista.append(elemento)

print("Mi lista actualizada tiene los siguientes elementos: {}".format(mi_lista))
