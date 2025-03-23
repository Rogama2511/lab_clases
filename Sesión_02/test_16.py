"""
Requisitos

1. Crear 2 variables enteras, 2 variables flotantes, 1 variable string (solamente caracteres), 1 variable string
con contenido solamente numérico y 1 variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica
(realizar conversiones si es necesario)
3. Obtener y mostar la suma de las 2 variables enteras más la variable string numérica y la
variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostarar el resultado entero o la parte entera de las 2 variables int: //
6. Obtener una pontencia usando una de las variables flotantes como base y la variable entera como potencia
"""

int_1= 34
int_2= 4

float_1= 3.14
float_2= 2.3

str_1 = "Curso"
str_2 = "748"

bool_1= True

#2 int + str
suma_1 = int_1 + int(str_2)
print("suma_1:{}".format(suma_1))

#3 int + int + str +flot
suma_2 = int_1 + int_2 + int(str_2) + float_1
print("suma_2:{}".format(suma_2))

#4 mod
mod_1 = int_1 % int_2
print("mod_1:{}".format(mod_1))

#5  resul int
part_ent = int_1 // int_2
print("part_ent:{}".format(part_ent))

#6 potencia
potencia_1 = float_2 ** int_2
print("potencia_1:{}".format(potencia_1))

