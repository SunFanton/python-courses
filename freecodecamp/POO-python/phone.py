from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones: int = 0):  # metodo magico
        super().__init__(
            name,
            price,
            quantity
        )

        # Validaciones de los parametros recibidos
        assert isinstance(broken_phones, int), f"Broken phones quantity {broken_phones} is not integer value"
        assert broken_phones >= 0, f"Broken phones {broken_phones} is negative"

        # Asignacion
        self.broken_hones = broken_phones

