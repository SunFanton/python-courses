class Generic:
    def __init__(self):
        self._x = 10

    def getter(self):
        print("Get x")
        return self._x

    def setter(self, value):
        print("Set x")
        self._x = value

    def deleter(self):
        print("Delete x")
        del self._x

    # se refiere al atributo privado x:
    x = property(getter, setter, deleter)


generic = Generic()
generic.x = 5
print(generic.x)
del generic.x