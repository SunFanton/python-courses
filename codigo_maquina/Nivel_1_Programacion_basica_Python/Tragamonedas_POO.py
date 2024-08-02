from random import randint

# el nombre de la clase NO debe ser igual al nombre del archivo .py

class Tragamonedas:
    # todos los metodos de una clase deberan tener el self en los parametros cuando se definen
    
    # constructor de la clase:
    def __init__(self, id, premio, color="Rojo"):
        self.id = id
        self.premio = premio
        self.color = color
        self.monedas = 0
        self.jackpots = 0

    
    def __str__(self): # metodo que se llama al ejecutar print de mi objeto (como el toString)
        return "ID: " + str(self.id) + " - Premio: " + str(self.premio)

    
    def __eq__(self, otro): # metodo que seria el equals que indica con respecto a que dos objetos de la misma clase son iguales o no
        return self.monedas == otro.monedas


    def __lt__(self, otro): # less than
        return self.monedas < otro.monedas


    def __gt__(self, otro): # greater than
        return self.monedas > otro.monedas

    
    def jugar(self):
        self.monedas += 1
        numeros = randint(0, 9), randint(0, 9), randint(0, 9)
        mensaje = ""
        if numeros[0] == numeros[1] == numeros[2]:
            self.jackpots += 1
            mensaje = "Jackpot! Has ganado %0.2f, felicidades!" % self.premio
        else:
            mensaje = "Suerte para la próxima..."
        return numeros, mensaje




    