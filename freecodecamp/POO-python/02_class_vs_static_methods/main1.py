from item import Item

Item.instantiate_from_csv()

print(Item.is_integer(7))
print(Item.is_integer(7.0))
print(Item.is_integer(6.5))