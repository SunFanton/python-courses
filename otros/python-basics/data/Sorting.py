my_list = [4,3,1,2,5]
# print(sorted(my_list))
# my_list.sort()
# print(my_list)

# print(sorted(my_list, reverse=True))

list2 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]
def sort_func(item):
    return item[1]

print(sorted(list2, key = sort_func))
print(sorted(list2, key = lambda item: item[1]))

# exercise
inventory_names = ["Lapiz", "Cuaderno", "Papel"]
inventory_numbers = [23, 45, 34]
combined_list = list(zip(inventory_names, inventory_numbers))
print(sorted(combined_list, key = lambda item: item[1]))
print(sorted(combined_list, key = lambda item: len(item[0])))