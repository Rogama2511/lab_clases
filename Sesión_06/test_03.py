"""Control o gestión de excepciones"""

"""
Requisitos:
    - Crear una función aplicando exceptions donde el bloque except
    va a considerar a los errors de división entre cero y el tipo de error
    - Los valores tienen que ser mayor a 0
    - Los valores tienen que ser ingresado por consola
"""

def opera(a,b):
    try:
        # Ingresar números
        a = int(input("Ingresar el primer número: "))
        b = int(input("Ingresar el segundo número: "))

        if a >= 0 and b >= 0:
            result = a / b
        else:
            print("Ingresar valores mayores a cero")
    except ValueError or TypeError:
        return print("No se puede usar un String en la operacion")
        resultado = None
        print("Resultado = {}".format(resultado))
    except ZeroDivisionError:
        return print("No se puede dividir por zero")
        resultado = None
        print("Resultado = {}".format(resultado))
    else:
        print("Resultado: ", result)

opera(0,0)

