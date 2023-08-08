#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta

class CuentaBancaria:
    monto = 0

    def __init__(self, numerocuenta: str, propietarios: str, balance: str):
        self.numerocuenta: str = numerocuenta
        self.propietarios: str = propietarios
        self.balance: str = balance

    def depositar(self, dinero: float):
        print("Depósito Exitoso")
        self.monto += dinero

cuentadeahorro = CuentaBancaria("876403", "Tomas Ramírez", "20%")
cuentadeahorro.depositar(11256)