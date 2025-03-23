"""Listas en Python"""

"""Listas -> sort(): Ordena los elementos de una lista"""

var_1 = ["sQLServer", "RDS", "MySQL", "Postgresql", "MongoDB"]
var_2 = [40, 2, 600, 36, 40.8, 2]

var_1.sort()
var_2.sort()

print(var_2)
print(var_1)

suma_lista = var_1 + var_2
print(suma_lista)

#No es permitido un orden de datos numéricos y string cuando están dentro de una sola lista
#print(suma_lista.sort())