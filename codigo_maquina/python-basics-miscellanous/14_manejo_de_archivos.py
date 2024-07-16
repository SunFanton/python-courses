print("*** PRIMERA PRUEBA ***")

archivo = open("datos.txt", encoding="utf-8")

#texto = archivo.read() # lee todo el contenido del archivo
#print(texto)

#caracteres = archivo.read(5) # lee 5 caracteres a partir de donde este posicionado el flujo archivo
#print(caracteres)
#caracteres = archivo.read(5) 
#print(caracteres)

"""
linea = archivo.readline() # lee una linea
print(linea)
linea = archivo.readline() 
print(linea)
linea = archivo.readline() 
print(linea)
"""

lineas = archivo.readlines() # devuelve una lista con cada linea
print(lineas)

archivo.close() # para liberar la memoria ram del flujo de datos del archivo

print("*** SEGUNDA PRUEBA ***")

# modo apertura lectura (puede ir r tambien)
with open("datos.txt", encoding="utf-8") as archivo: # esto evita tener que usar el close, lo que es menos propenso a errores ya que es automatico
    lineas = archivo.readlines() 
    print(lineas)

print("*** TERCER PRUEBA ***")

# modo apertura write
with open("personas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Juan Perez Esquivel 18\n")
    archivo.write("María Ordoñez 22\n")
    
print("*** CUARTA PRUEBA ***")

# modo apertura append (para agregar al final)
with open("personas.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Raul Gomez 45\n")
    archivo.write("francisco García 22")
