from vehiculo import Vehiculo

vehiculo_a = Vehiculo("ROJO")
vehiculo_b = Vehiculo("Violeta")

print("Vehiculos")
print(vehiculo_a)
print(vehiculo_b)

print("Series")
print(vehiculo_a.serie)
print(vehiculo_b.serie)

print("Folio") # atributo de clase
print(vehiculo_a.folio)
print(vehiculo_b.folio)
print(Vehiculo.folio)