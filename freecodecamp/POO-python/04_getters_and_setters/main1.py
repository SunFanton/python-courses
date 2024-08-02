from item import Item


item1 = Item("MyItem", 500)

print(item1.name)
#print(item1._Item__name) # asi se accede al atributo privado name pero esto no es correcto en cuanto a buenas practicas
item1.name = "NewName"
print(item1.name)

item1.apply_increment(0.5)
print(item1.price)

item1.send_email()