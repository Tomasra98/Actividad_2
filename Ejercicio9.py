#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta

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

cuentadeahorro = CuentaBancaria("876403", "Tomas Ramírez", "20%")
cuentadeahorro.depositar(11256)
cuentadeahorro.retirar(1009)