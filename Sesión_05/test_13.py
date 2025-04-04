"""Usando los métodos de cadenas o strings"""

"""Métodos de separación de strings: split()"""

cadena = "Python para la predicción de fraudes bancarios."

cadena_sin_espacios = cadena.split()
print("Cadena separada por espacios en blanco dentro del string: {}".format(cadena_sin_espacios))

for palabra in cadena_sin_espacios:
    print(palabra)
