"""
Requisitos:

- Dentro de una empresa se va a solicitar pedir nombre y apellido del empleado (input)
- Distrito de residencia y su sueldo actual (inputs)
- Sueldo y calculo del bono final del año, que será el triple del sueldo mensualmenos el 10% del sueldo
- Todos estos datos van a ingresar en un diccionario
- Asignar a 3 variables usando asignación múltiple los valores del diccionario
- Mostrar por la terminal el mensaje de: "'Nombre' 'apellido', recibirá 'bono' soles de bono de fin de año"
"""
#Datos usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
distrito = input("Ingrese distrito de residencia:")
sueldo = input("Ingrese su sueldo: ")

#calculo del bono final
bono_final = (float(sueldo) * 3) - (float(sueldo) * 0.1)

#Diccionario
dic = {"nombre": nombre,
    "apellido": apellido,
    "distrito": distrito,
    "sueldo": sueldo,
    "bono_final": bono_final}
print(dic)

#Asignación multiple de valores
nombre, apellido, distrito = dic["nombre"], dic["apellido"], dic["distrito"]
print(nombre, apellido, distrito)

#Mensaje final
print("{} {}, recibirá {} soles de bono de fin de año".format(nombre, apellido, bono_final))
