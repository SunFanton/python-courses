"""
las funciones eval y exec se utilizan para convertir un string
que se pasa como parametro a codigo Python que se puede ejecutar.
eval es mas basico, por ejemplo no se pueden crear nuevas variables,
ni evaluar if, etc. exec en cambio es mucho mas poderoso.
Sin embargo, se debe tener cuidado con ambos porque pueden dar
lugar a la ejecucion de codigo malicioso inyectado por un atacante
externo a nuestro programa
"""

print(eval('1 + 5'))
print(eval('"test".upper()'))

exec('a = 10')
print(a)

for operation in ["upper","title","lower","casefold"]:
    print(eval(f'"test".{operation}()'))