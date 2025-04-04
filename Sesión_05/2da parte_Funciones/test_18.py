"""Programación funcional con Python"""

var_1 = 80
var_2 = 100

"""input: dos variable que pasaran como parametro de la función
a, b: parametros de la función"""

def sumar(a, b):
    return a + b

def potencia(a, b):
    suma = a + b
    var_1 = pow(suma, 3)
    return var_1


result = sumar(var_1, var_2)
"""Output: lo que va a retornar la función"""
print(result)

resultado_2 = sumar(90.7, 150)
print(resultado_2)

resultado_3 = potencia(3, 5)

print(resultado_3)