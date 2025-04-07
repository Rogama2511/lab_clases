"""
Ejercicio propuesto (POO)

Crear una clase CajeroAutomatico que permita simular las operaciones básicas
de un cajero automático, como consultar saldo, depositar dinero, retirar dinero
y mostrar historial de transacciones.

Requisitos:
- Deberá tener los métodos de: consultar_saldo, depositar(monto), retirar(monto), mostrar_historial()
- Inicializa el cajero con los atributos de saldo inicial y un historial vacío (lista).
- En el método depositar() debe indicar que "El monto a depositar debe ser mayor a cero"
si ingresa un monto negativo
- Si se logra realizar el depósito mostrará un mensaje de "Depósito exitoso de S/ 'monto'"


Tomar en cuenta lo siguiente:
- historial será un tipo de datos list para que puedan ingresar todo el historial
- Recorrer el historial con un for para poder mostrar el historial completo en el método
mostrar_historial()
- Si self.historial está vacío indicar que "no hay transacciones registradas"
- Si en el método retirar(monto) el monto es mayor a self.saldo indicar que hay saldo insuficiente
para poder realizar el retiro
- Cada vez que e haga un depósito se irá actualizando el self.historial (append(Depósito: S/ {monto}))

"""

class CajeroAutomatico:
    def __init__(self, saldo):
        self.saldo = saldo   #Saldo inicial
        self.historial = []     #Lista para guargar las transacciones

    def consultar_saldo(self):
        return "Salso actual: S/ {}".format(self.saldo)

    def depositar(self, monto):
        if monto <= 0:
            return "El monto a depositar debe ser mayor a cero"
        else :
            self.saldo += monto
            self.historial.append("Depósito: S/ {}".format(monto))
            return "Depósito exitoso de S/ {}". format(monto)

    def retirar(self, monto):
        if monto > self.saldo:
            return "Saldo insuficiente para realizr el retiro"
        elif monto <= 0:
            return "El monto a retirar debe ser mayor a cero"
        else :
            self.saldo -= monto
            self.historial.append("Retiro: S/ {}".format(monto))
            return "Retiro exitoso de S/ {}". format(monto)

    def mostrar_historial(self):
        if self.historial == 0:
            return "No hay transacciones registradas"
        else:
            print("Historial de transacciones: ")
            for item in self.historial:
                print( "-{}".format(item))

operacion = CajeroAutomatico(1550)   #Instanciar clase

print(operacion.consultar_saldo())  #Consultar saldo
print(operacion.depositar(110))      #Deposita s/ 55
print(operacion.retirar(250))       #Retira s/ 200
print(operacion.depositar(50))     #Deposita s/ 100
print(operacion.consultar_saldo())  #Saldo luego de las transacciones

print(" ")
#Mostrar historial de transacciones
operacion.mostrar_historial()