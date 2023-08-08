#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros

class CuentaBancaria:
    def __init__(self, numerocuenta: str, propietarios: str, balance: str):
        self.numerocuenta: str = numerocuenta
        self.propietarios: str = propietarios
        self.balance: str = balance