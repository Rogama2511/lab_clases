"""Cadenas o string"""
"""Concatenación"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

nombre_completo = "El nombre completo del usuario es: " + nombre + "" + apellido
print(nombre_completo)

print("El nombre completo del usuario es: {} {}".format(nombre,apellido))
