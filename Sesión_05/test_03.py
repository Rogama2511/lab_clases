"""Uso del condicional if"""

edad_1 = int(input("Ingrese una primera edad por favor: "))
edad_2 = int(input("Ingrese una segunda edad por favor: "))

if edad_1 < 0 or edad_2 < 0:
    print("Debe ingresar edades positivas")
# elif type(edad_1) != int or type(edad_2) != int:
#    print("Debe ingresar datos tipo enter")
elif edad_1 > edad_2:
    print("La edad 1 es mayor a la edad 2 que ha ingresado")
elif edad_1 == edad_2:
    print("Las edades ingresadas son iguales")
else:
    print("La edad 1 es menor a la edad 2 que ha ingresado")

