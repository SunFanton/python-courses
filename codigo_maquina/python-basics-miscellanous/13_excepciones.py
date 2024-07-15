# Listado completo de errores y excepciones predefinidas en Python:
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# Posibles errores a partir de este codigo: ZeroDivisionError, ValueError

pagos_max = 12
monto_max = 100000

try:
    monto = float(input("Indica el monto del crédito:"))
    num_pagos = int(input("Indica el número de pagos:"))
    if monto < 0 or num_pagos < 0:
        raise Exception("Ingresa valores positivos para el monto y el número de pagos")
    if monto > monto_max:
        raise Exception("Monto excedido", f"El monto del crédito no puede ser mayor a ${monto_max}")
    if num_pagos > pagos_max:
        raise Exception("Número de pagos inválido", f"El número de pagos debe ser menor o igual a {pagos_max} meses")
    pago_mensual = monto / num_pagos
    print("El pago mensual será de: $ ", pago_mensual)
except ValueError:
    print("Hubo un error de conversión")
except ZeroDivisionError:
    print("No puedes indicar 0 pagos. Por favor, intenta nuevamente")
except Exception as error:
    for arg in error.args:
        print(arg)
else: # este bloque se ejecuta al final solo si no se produjo ninguna excepcion
    print("La solicitud de tu crédito se ha realizado exitosamente")
finally: # se ejecuta siempre, ya sea que hubiera error o no
    print("Gracias por participar")

  