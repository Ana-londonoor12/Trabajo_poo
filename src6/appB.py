from modelo6.Cuenta_Bancaria import CuentaBancaria

mi_cuenta = CuentaBancaria()

mi_cuenta.depositar(5000000)
mi_cuenta.retirar(2000000)
mi_cuenta.aplicar_cuota_manejo()

mi_cuenta.mostrar_detalles()