"""Usando los métodos de cadenas o strings"""

"""Métodos de string"""

cadena = "Conexión a Base de Datos con python"

cadena_2 = cadena.replace(cadena[0:8],"Nueva conexión")

print("Cadena con reemplazo, tiene el siguiente valor actualizado: {}".format(cadena_2))

"""Elimicación de espacios en blanco de mi cadenca (después)"""

cadena_3 = "Conexión a base de datos con python    "
cadena_4 = cadena_3.rstrip()
print(cadena_3)
print("Mi cadena actualizada sin espacios en blanco: {}".format(cadena_4))



"""Eliminación de espacios en blanco de mi cadena (antes)"""

cadena_5 = "          Conexión a base de datos con python"
cadena_6 = cadena_5.lstrip()
print(cadena_5)
print("Mi cadena actualizada sin espacios en blanco de mi cadena: {}".format(cadena_6))


