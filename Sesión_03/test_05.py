"""Listas en Python"""

"""Listas -> count(): Cantidad de veces que aparece un elemento que se repite en la lista"""

var_1 = ["Python", "JAVA", "php", "Javascript", "Typescript"]

var_1.append("Python")
var_1.append("Python")
var_1.append("Python")
var_1.append("Python")
var_1.append("NodeJS")

print("Mi lista var_1: {}".format(var_1))

print("La cantidad de veces que se repite 'Python' es: {}".format(var_1.count("Python")))
print("La cantidad de veces que se repite 'NodeJS' es: {}".format(var_1.count("NodeJS")))
