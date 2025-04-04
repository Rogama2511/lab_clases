"""
Programación funcional con Python (POO)

Requisitos:
    - Solicitar al usuario 4 números por consola
    - Crear una función que devuelva cuál es el número mayor de los 4
      ingresados por el usuario
    - Finalmente asignar a una variable el valor de esta función
      para elevar al cubo este resultado y mostrarlo en la terminal
"""

#Ingresar datos
a = float(input("Ingresar el primer número:"))
b = float(input("Ingresar el segundo número:"))
c = float(input("Ingrear el tercer número:"))
d = float(input("Ingresar el cuarto número:"))

#Definir función
def funcion(a, b, c, d):
    return max(a, b, c, d)

#Definir número mayor
mayor_num = funcion(a, b, c, d)

resultado = mayor_num ** 3

print("El mayor número es:", mayor_num)
print("El cubo del mayor es:", resultado)