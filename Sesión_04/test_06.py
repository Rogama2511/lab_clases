"""Asignación múltiple"""
"""Referencia a dos o más variables con su respectivos datos"""

var_1 = input("Ingrese nombre de usuario: ")
var_2 = input("Ingrese nombre: ")
var_3 = input("Ingrese edad: ")

#usuario = var_1
#nombre = var_2
#edad = var_3

usuario, nombre, edad = var_1, var_2, var_3
print("Su nombre de usuario es {} y tiene {} años".format(nombre, edad))
