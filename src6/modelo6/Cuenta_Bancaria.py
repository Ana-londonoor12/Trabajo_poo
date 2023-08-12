class CuentaBancaria:
    def __init__(self):
        self.numero_cuenta = "400876235-6"
        self.propietarios = "Andrea Ramírez"
        self.balance = 23000000

    def depositar(self, monto):
        self.balance += monto
        print(f"Se depositaron {monto} unidades en la cuenta {self.numero_cuenta}. Nuevo saldo: {self.balance}")

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
            print(f"Se retiraron {monto} unidades de la cuenta {self.numero_cuenta}. Nuevo saldo: {self.balance}")
        else:
            print("Fondos insuficientes.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se aplicó una cuota de manejo del 2% en la cuenta {self.numero_cuenta}. Nuevo saldo: {self.balance}")

    def mostrar_detalles(self):
        print(f"Detalles de la cuenta:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {self.propietarios}")
        print(f"Saldo actual: {self.balance}")
        