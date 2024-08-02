# Conceptos de encapsulamiento

class CuentaBancaria:

    
    def __init__(self, nombre, direccion):
        self.id = self.__generar_id(nombre)
        self.nombre = nombre
        self.direccion = direccion
        self.__balance = 0.00 # atributo privado, no se puede acceder publicamente, aunque en realidad Python lo pone como sugerencia y sí existen formas de acceder a dicho atributo


    # Ejemplo de metodo privado, que solo se puede acceder dentro de la clase
    def __generar_id(self, nombre):
        # Convierte cada carácter del nombre a su valor ASCII y concatena los valores
        ascii_values = ''.join(str(ord(char)) for char in nombre)
        
        # Convierte la cadena de valores ASCII concatenados a un número entero
        id_number = int(ascii_values)
        
        # Limita el tamaño del número a 10 dígitos (0 a 9999999999)
        max_id = 10**10 - 1
        id_number = id_number % (max_id + 1)
        
        return id_number
    
    
    def retirar(self, monto):
        if self.__balance >= monto:
            self.__balance -= monto


    def depositar(self, monto):
        if monto > 0:
            self.__balance += monto
        