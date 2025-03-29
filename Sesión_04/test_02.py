"""Diccionarios en Python"""

"""del: elimina a un key y su valor del diccionario"""

var_1 = {"nombre": "Susana", "edad": 29, "promedio": 18.9}

var_1["distrito"] = "Lince"
del var_1["edad"]
del var_1["promedio"]

print(var_1)