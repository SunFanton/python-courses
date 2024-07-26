from Cuenta import CuentaBancaria

cuenta = CuentaBancaria("Juan Perez", "Av de los Reyes 123")

print(cuenta.direccion)
cuenta.direccion = "Av de los Papas 123"
print(cuenta.direccion)
print(cuenta.id)

# print(cuenta._CuentaBancaria__balance) # forma de acceder a atributo privado (Python ha sido criticado por esto)
#print(cuenta.__balance)

cuenta.depositar(1000)
cuenta.retirar(100)

