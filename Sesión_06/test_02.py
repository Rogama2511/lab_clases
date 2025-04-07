"""Control o gestión de excepciones"""

"""
    Crear una aplicación usando exepciones donde no se pueda
    realizar la suma entre diferentes tipos de datos
"""


def operaciones(a, b):
    try:
        #resultado = a + b
        resultado = a/b
    except TypeError:
        print("No se puede usar un string como un dato int")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        resultado = None
        print(resultado)
    else:
        print(resultado)

print("___________________________")
operaciones(40, "Lima")
print("___________________________")
operaciones(40, 0)
