
"""1. Crear un módulo donde se va a tener que crear una función que obtiene
el impuesto que va a pagar una persona si el sueldo es mayor a 500 soles,
impuesto: 8%

2. Esta función usará una exception si el sueldo es tipo string"""

def cal_impuesto(sueldo):
    try:
        sueldo = int(sueldo)
        if sueldo > 500:
            impuesto = sueldo * 0.08
            print("Impuesto es de: {} ".format(impuesto))
        else:
            print("No paga impuesto")
    except ValueError or TypeError:
        print("Sueldo no puede ser un String")


