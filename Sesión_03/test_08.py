"""Listas en Python"""

"""Listas -> copy(): Obtener todos los valores de una lista en otra variable"""

var_1 = ["sQLServer", "RDS", "MySQL", "Postgresql", "MongoDB"]

var_2 = var_1.copy()

print("Los valores de mi var_2 son: {}".format(var_2))

var_2.append("MaríaDB")
var_2.append("SQLite3")

print("Los valores actualizados de mi var_2 son: {}".format(var_2))

print(var_1)