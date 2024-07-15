inventory_names = ["Lapiz", "Papel", "Cuaderno"]
inventory_numbers = [23, 45, 34]

print("\n ***** Zip *****")
print(list(zip(inventory_names, inventory_numbers)))

"""
con zip(iterable, iterable...) se convierte por ej el item del indice 0
de la primer lista y el item del indice 0 de la otra lista en una tupla 
con ambos valores.
Y en esta iteracion se hace un unpacking de cada tupla
"""
for name, number in zip(inventory_names, inventory_numbers):
    print(f'{name} con stock de {number}')

# enumerate function:
print("\n ***** Enumerate *****")
print(list(enumerate(inventory_names)))
for index, name in enumerate(inventory_names):
    print(f'Indice: {index} - Item: {name}')
    if index == len(inventory_names) // 2:
        print('halfway done')

# Exercise
print(list(zip(enumerate(inventory_names), inventory_numbers)))
for index, inventory_tuple in enumerate(zip(inventory_names, inventory_numbers)):
    name, stock = inventory_tuple
    print(f'{name} [id: {index}] - Stock: {stock}')