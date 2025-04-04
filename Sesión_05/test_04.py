"""Uso del condicional While"""

numero = int(input("¿Cuántos saludos desea enviar?:"))

while numero < 10:
    print(numero)
    numero = numero + 1
    #El número ya aumento de valor
    print("Número con un nuevo valor: {}".format(numero))