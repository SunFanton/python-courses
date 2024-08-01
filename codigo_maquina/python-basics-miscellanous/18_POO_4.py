from producto import Producto, Perecedero, Electronico

p_1 = Producto("g", "Generico", 100)
p_2 = Perecedero("p", "Tomate", 200, "2003")
p_3 = Electronico("e", "Lavadora", 1100.50, "Sony")


#print(p_1.crear_etiqueta())
#print(p_2.crear_etiqueta())
#print(p_3.crear_etiqueta())

objetos = (p_1, p_2, p_3)

for obj in objetos:
    print(obj.crear_etiqueta(), type(obj))
    print(isinstance(obj, Producto))