#from funciones import *  #No se realiza esto porque sobrecarga la memoria
from funciones import suma as opera_1, multiplicacion as opera_2

var_1 = int(input("Primer valor: "))
var_2 = int(input("Segundo valor: "))

#sum = suma(var_1, var_2)
sum = opera_1(var_1, var_2)
print(sum)

#multi = multiplicacion(var_1, var_2)
multi = opera_2(var_1, var_2)
print(multi)




