"""Control o gestión de excepciones"""
"""
TyperError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
ImportError
OverFlowError
"""

"""
Estructura y uso:
"""
"""
try:
    bloque código 1
except 'excepción 1':
    bloque código 2
else:
    bloque código 3
"""

def division(a, b):
    try:
        resultado = a/b
        print("Division correcta")
        #print(resultado)
    except ZeroDivisionError:
        print("No es posible dividir estos valores")
        resultado = None
        print("Resultado: {}".format(resultado))
    else:
        print("Resultado: {}".format(resultado))


print("___________________________")
division(1000, 10)
print("___________________________")
division(400, 0)
print("___________________________")
division(2, 500)
