"""
El equivalente con decorators de lo hecho en el archivo
PropertyDecorator
"""

class Generic:
    def __init__(self):
        self._x = 10

    @property # para el getter
    def x(self):
        print("Get x")
        return self._x

    @x.setter
    def x(self, value):
        print("Set x")
        self._x = value

    @x.deleter
    def x(self):
        print("Delete x")
        del self._x


generic = Generic()
generic.x = 5
print(generic.x)
del generic.x