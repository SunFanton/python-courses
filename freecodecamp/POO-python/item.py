import csv


class Item:
    pay_rate = 0.8 # atributo de clase
    all = []
    def __init__(self, name: str, price: float, quantity: int = 0): # metodo magico
        # Validaciones de los parametros recibidos
        assert isinstance(name, str), f"Name {name} is not string"
        assert isinstance(price, float) or isinstance(price, int), f"Price {price} is not number value"
        assert isinstance(quantity, int), f"Quantity {quantity} is not integer value"
        assert price >= 0, f"Price {price} is negative"
        assert quantity >= 0, f"Quantity {quantity} is negative"

        # Asignacion
        self.__name = name # atributo privado
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        # primero se buscara si la instancia contiene el atributo pay_rate, si es asi, usara ese, sino usara el pay_rate de clase
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price += self.price * increment_value

    @property
    #indica que el atributo en cuestion es de solo lectura (si no tuviera un setter)
    #esto vendria ser como un getter
    def name(self):
        return self.__name

    @name.setter # setter para el atributo privado name
    def name(self, value):
        if len(value) > 20:
            raise Exception("Name too long!")
        self.__name = value

    def __str__(self): # se usa para una representacion en cadena de texto del objeto comprensible para un ser humano
        return f"Nombre: {self.name}, Precio: {self.__price}, Cantidad: {self.quantity}"

    def __repr__(self): # se usa para una representacion en cadena de texto del objeto para logging, depuracion, etc
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    # Metodo de clase que se accede a nivel de clase, no de instancia/objeto
    # el parametro que se pasa implicitamente es la clase en si, por eso el cls en lugar del self
    @classmethod
    def instantiate_from_csv(cls):
        '''
        - Crear métodos de fábrica que devuelven instancias de la clase
        - Realizar operaciones que afectan a la clase en sí misma, como cambiar un atributo de clase
        - tienen acceso a la clase en sí misma
        - reciben la clase como primer argumento (cls)
        - se utilizan cuando se necesita acceder a la clase en sí misma
        '''
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) # lee el archivo csv y devuelve lista de diccionarios
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )

    # Metodo estatico
    @staticmethod
    def is_integer(num):
        '''
        - Realizar operaciones que no dependen de la clase o la instancia
        - Proporcionar una función de utilidad que se puede utilizar en cualquier lugar
        - no tienen acceso a la clase o la instancia
        - no reciben ningún argumento adicional
        - se utilizan cuando se necesita una función de utilidad que no depende de la clase o la instancia
        '''
        if isinstance(num, float):
            return num.is_integer() # is_integer() en este caso es de la clase float, no confundir con el metodo que armamos
        elif isinstance(num, int):
            return True
        else:
            return False

    def calculate_total_price(self):
        return self.__price * self.quantity

    def __connect(self,  smtp_server): # metodo privado
        pass

    def __create_body(self): # metodo privado
        pass

    def __send(self): # metodo privado
        pass

    def send_email(self):
        self.__connect("server")
        self.__create_body()
        self.__send()
        print("Email was send!")
