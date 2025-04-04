"""
Programación funcional con Python (POO)

Requisitos:
    - Crear una función que multiplicará 3 valores y luego restará el segundo parámetro
    - Para esta función el tercer parámetro contendrá un valor
    - Mostrar 2 casos donde se ingrese los valores donde uno no afectará
    el valor del parámetro que ya contiene un valor
    y otro donde si lo estará afectando
"""

#Definir la Función
def operacion(var1, var2, var3=7):
    resultado = (var1 * var2 * var3) - var2
    return resultado

#Casi 1: Sin afectar el valor por defecto de var3
resultado_1 = operacion(10,2)
print("Resultado sin afectar el valor por defecto: {}".format(resultado_1))

#Caso 2: Cambiando el valor por defecto de var3
resultado_2 = operacion(4, 3, 5)
print("Resultado cambiando el valor por defecto: {}".format(resultado_2))

