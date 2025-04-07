"""
Ejercicio de intervención

Requisitos:
- Agregar una exepción donde se va a considerar una lista con 4 valores,
todos sus datos serán string
- Al querer modificar una de las posiciones no existentes
crear un nuevo índice y darle el valor de "0"
- Mostrar la lista final
"""

#Lista inicial
lista = ["Lima","Huanuco","Arequipa","Loreto"]

def modf_lista(indice, valor):
    try:
        lista[indice] = valor

    except IndexError:
        print("Índice no existente")
        lista.append(0)
        print("Lista = {}".format(lista))

    else:
        print("Lista modificada:{} ".format(lista))


print("Lista inicial: {}".format(lista))

#Indice correcto
modf_lista(2,"San Martin")

print(" ")
#Indice incorrecto
modf_lista(6,"Ancash")