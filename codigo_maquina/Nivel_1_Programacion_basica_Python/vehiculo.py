class Vehiculo:

    # vemos como definir atributos de clase:
    folio = 0

    # Constante (como tupla, porque es inmutable):
    COLORES = ("BLANCO", "ROJO", "VERDE")

    
    def __init__(self, color):
        Vehiculo.folio += 1 # asi se debe acceder a un atributo de clase, incluso aqui
        self.serie = Vehiculo.folio
        self.set_color(color)
        

    def __str__(self):
        return f"Nro de serie: {int(self.serie)} - Color: {self.color}"

    
    def set_color(self, color):
        color = color.upper().strip()
        if color in Vehiculo.COLORES:
            self.color = color
        else:
            self.color = Vehiculo.COLORES[0] # default

        
        