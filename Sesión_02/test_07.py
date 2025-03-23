"""Reconocimiento de tipos de datos: type()"""

"""Creación de vaiables"""

nombre = "Luis"
ciudad = "Lima"
saldo = 5000
empresa = False
correo = "luish@gmail.com"
empleado = [nombre, saldo, empresa, ciudad]
empleado_d = {'nomb': nombre, 'cuid': ciudad, 'sald' : saldo, 'emp': empresa, 'corr': correo}

print("Tipo de dato de mi varible 'nombre' es:{}".format(type(nombre)))
print("Tipo de dato de mi varible 'ciudad' es:{}".format(type(ciudad)))
print("Tipo de dato de mi varible 'saldo' es:{}".format(type(saldo)))
print("Tipo de dato de mi varible 'empresa' es:{}".format(type(empresa)))
print("Tipo de dato de mi varible 'correo' es:{}".format(type(correo)))
print("Tipo de dato de mi varible 'empleado' es:{}".format(type(empleado)))
print("Tipo de dato de mi varible 'empleado_d' es:{}".format(type(empleado_d)))