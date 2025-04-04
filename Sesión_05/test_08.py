"""if ternarios"""

"""
Requisitos: 
 - Ingresar por teclado el sueldo de un empleado
 - Si el sueldo es mayor a 2500 y menor a 3500, imprimir "Su sueldo no tiene bonificación"
 y se le agregará el 10%, para luego mostrar el sueldo final con la bonificación
 - Caso contrario: "Su sueldo tiene bonificación este año y será de: 
 'sueldo_final'", sueldo_final= sueldo + 2% sueldo
"""

#Ingresar sueldo
sueldo = float(input("Ingresar sueldo de empleado: "))

#Verificar bonificación
if sueldo > 2500 and sueldo < 3500:
    print("Su sueldo no tiene bonificación")
    sueldo_fin = sueldo +  (sueldo * 0.10)
    print("Su sueldo final es: {}".format(sueldo_fin))
else:
    sueldo_fin = sueldo + (sueldo * 0.02)
    print(f"Su sueldo tiene bonificación este año y será de: {sueldo_fin} ")


