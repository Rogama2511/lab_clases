"""Listas en Python"""

"""
Requisitos:

- Crear dos lista de personas vacías
- Agregar los datos de nombre, edad y profesión para ambas listas
- Obtener y mostrar la suma de las edad // por índica
- Sumar ambas listas y mostrar el resultado en la terminal
- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando las edades de ambas personas
- Mostrar la lista vacía de la segunda persona aplicando el método respectivamente

"""

#Crear listas
person_1 = []
person_2 = []

#Agregar datos
person_1.append("Oscar")
person_1 .append(48)
person_1.append("Biologo")

person_2.append("Rocio")
person_2.append(45)
person_2.append("Obstreta")

print(person_1)
print(person_2)
print(" ")

#Suma edades
suma_edad = person_1[1] + person_2[1]
print("La suma de las edades es :{}".format(suma_edad))

#Suma listas
sum_lists = person_1 + person_2
print("La suma de la lista: {}" .format(sum_lists))

#Lista Inversa
sum_lists.reverse()
print("Lista en reverso:{}".format(sum_lists))

#Elimina edades
sum_lists.pop(1)
sum_lists.pop(3)
print("Lista sin las edades:{}".format(sum_lists))

#Vaciar lista 2
person_2.clear()
print("Lista de la segunda persona vacia: {}".format(person_2))


fecha_actualizada = "23/03/2025"