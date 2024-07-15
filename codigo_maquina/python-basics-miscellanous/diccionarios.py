persona = { "nombre": "Juan", "edad": 33, "direccion": "Reforma 333" }

print(persona["nombre"])
print(persona.get("nombre"))

print(persona.keys())
print(persona.items())
print(persona.values())

for valor in persona.values():
    print(valor)

for llave in persona.keys():
    print(llave)

for elemento in persona.items():
    print(elemento)

for llave,valor in persona.items(): # aplicamos unpacking
    print(llave, ":", valor)

persona["direccion"] = "Reforma 300"

