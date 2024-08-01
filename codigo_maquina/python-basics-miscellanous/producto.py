class Producto:
    # clase padre

    def __init__(self, id: str, descripcion: str, costo: float):
        self.id = id
        self.descripcion = descripcion
        self.costo = costo
        
    def crear_etiqueta(self):
        return "%s\n%s\n%0.2f\n" % (self.id, 
                                  self.descripcion, 
                                  self.costo)


class Perecedero(Producto):
    # clase hija de Producto

    def __init__(self, id, descripcion, costo, caducidad):
        super().__init__(id, descripcion, costo) # llamamos al contructor de la clase padre
        self.caducidad = caducidad

    def crear_etiqueta(self): # sobreescritura de metodos (ya que ya esta en la clase padre)
        return super().crear_etiqueta() + "%s\n" % self.caducidad


class Electronico(Producto):
    # clase hija de Producto

    def __init__(self, id, descripcion, costo, marca):
        super().__init__(id, descripcion, costo) # llamamos al contructor de la clase padre
        self.marca = marca
    


        
    