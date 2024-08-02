def escribir(path, texto):
    with open(path, "w", encoding="utf-8") as archivo:
        archivo.write(texto)


def leer(path):
    texto = ""
    with open(path, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    return texto


"""
El programa o modulo desde el cual se hace 'play', es decir, el que se ejecuta, 
toma el nombre de __main__, de alli que se este verificando que en este caso solo 
se ejecute la prueba que esta abajo si este modulo manejo_archivos es el 
programa principal
"""
if __name__ == "__main__":
    escribir("Prueba.txt", "Esto es una prueba")
    print(leer("Prueba.txt"))