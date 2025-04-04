"""Usando las propiedades de cadenas o string"""

"""
Requisitos:
 - Ingresar tu nombre y apellido por consola 
 (cada valor tiene que estar en una variable distinta)
 - Obtener el tamaño de tu nombre y apeellido completo luego de concatenarlos
 y mostrar en consola
 - Imprimir el resultado de la concatenación final todo en mayúsculas
 - Indicar mediante condicionales si el tamaño del nombre es mayor 
 o no al del apellido ingresado
 (Ingresar solo en este caso el apellido paterno)
 """

#Ingresar datos
nombre = input("Ingresar tu nombre: ")
apellido = input("Ingresar tu apellido: ")

#Tamaño de datos concatenados
nombre_completo = nombre + " " + apellido
tamaño_nom = len(nombre_completo)
print("El tamaño del nombre completo es: {}".format(tamaño_nom))

#Nombre mayúsculas
print("El nombre completo en mayúsculas es: {}".format(nombre_completo.upper()))

#Compara tamaño del nombre y apellido
if len(nombre) > len(apellido):
    print("El nombre es más largo que el apellido")
elif len(nombre) < len(apellido):
    print("El apellido es más largo que el nombre")
else:
    print("El nombre y el apellido tienen el mismo tamaño")

