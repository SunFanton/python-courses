from item import Item
import logging

try:
    item1 = Item("Phone", 1000.0, 5)
    item2 = Item("Laptop", 100.0, 3)

    print(item1.calculate_total_price()) # implicitamente Python pasa la instacia/objeto en si como primer parametro (que seria el self en la definicion del metoto en la clase)
    print(item2.calculate_total_price())

    print()

    print(item1.name)
    print(item1.__price)
    print(item1.quantity)
    print(item2.name)
    print(item2.__price)
    print(item2.quantity)

    print()

    print(Item.pay_rate)
    print(item1.pay_rate) # pay_rate es atributo de clase, Python primero revisa si esta entre los atributos del objeto, sino busca en los atributos de la clase Item
    print(item2.pay_rate)
    print(Item.__dict__) # dict es atributo magico que muestra los atributos, en este caso, de la clase
    print(item1.__dict__) # muestra los atributos de la instancia/objeto

    print()

    item1.apply_discount()
    print(item1.__price)
    item2.pay_rate = 0.7
    item2.apply_discount()
    print(item2.__price)

    print()

except Exception as e:
    logging.log(level=logging.ERROR, msg=e.args)

#print(type(item1))
#print(type(item1.name))
#print(type(item1.price))
#print(type(item1.quantity))