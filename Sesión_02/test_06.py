"""
Requisitos

1. Creando variables para los valores nombre, profesión y ciudad
2. Crear 2 variables para la remuneración de Enero y Febrero (más de 1000)
3. Crear una variable donde se sumaran los ingresos de enero y febrero
4. Mostrar en pantalla el mensaje:
    "Hola soy 'nombre', mi profesión es 'profesión' y mi remuneración acumulada es 'remuneración'"
"""
from sqlparse.utils import LINE_MATCH

nombre = "Collet"
profesión = "Doctora"
cuidad = "Lima"

enr= 1350
feb = 1900
rem_tot= enr + feb

print("Hola soy {} mi profesión es {} y mi remuneración acumulada es de {} en total".format(nombre, profesión, rem_tot))