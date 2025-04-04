"""Uso del bucle for"""

ingenieria = ["Software", "Sistemas", "Industrial", "Quimica", "Mecánica","Mecatrónica"]

print("El tamaño de la lista es {}".format(len(ingenieria)))

i = 0
for ing in ingenieria:
    print("Ingenieria {}".format(ing))
    print("Valor de i: {}".format(i))

    ingenieria[i] = "Estadística"
    i = i + 1

print("La lista actualizada es: {}".format(ingenieria))

