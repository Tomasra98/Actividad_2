#Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria

class CuentaBancaria:
    monto = 0

    def __init__(self, numerocuenta: str, propietarios: str, balance: str):
        self.numerocuenta: str = numerocuenta
        self.propietarios: str = propietarios
        self.balance: str = balance

    def depositar(self, dinero: float):
        print("Depósito Exitoso")
        self.monto += dinero

    def retirar(self, dinero: float):
        if(self.monto >= dinero):
            self.monto -= dinero
            print("Retiro Bien Realizado")
        else:
            print("Careces de fondos para hacer este retiro")
    def aplicar_cuota_de_manejo(self):
        self.balance = "2%"
    def mostrardetallesdelacuenta(self):
        print("Número de la cuenta: ", self.numerocuenta)
        print("Propietarios: ", self.propietarios)
        print("Balance: ", self.balance)
        print("Dinero en la cuenta: ", self.monto)

cuentadeahorro = CuentaBancaria("876403", "Tomas Ramírez", "20%")
cuentadeahorro.depositar(11256)
cuentadeahorro.retirar(1009)
cuentadeahorro.aplicar_cuota_de_manejo()
cuentadeahorro.mostrardetallesdelacuenta()