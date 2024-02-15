print('***** List comprehension basics *****')
my_list = []
for num in range(0, 100):
    my_list.append(num)

print(my_list)

# otra forma de hacer lo mismo pero en una sola linea:
my_list_comp = [num for num in range(0,100)]
print(my_list_comp)

my_list_comp2 = [num for num in range(0,100) if num < 20]
print(my_list_comp2)

my_list_comp3 = [num if num < 20 else 0 for num in range(0,100)]
print(my_list_comp3)

print('\n***** List comprehension more *****')
inventory_names = ["Lapiz", "Papel", "Cuaderno", "Birome", "Sacapuntas"]
inventory_numbers = [23, 45, 34, 12, 9]
replenish_list = [(name, number) for name, number in zip(inventory_names, inventory_numbers) if number < 25]
print(replenish_list)

print('\n***** Combine list comprehension *****')
combined_comp = [[x for x in range(5)] for y in range(10)]
print(combined_comp)
for row in combined_comp:
    print(row)

combined_comp2 = [[(x,y) for x in range(5)] for y in range(10)]
print(combined_comp2)
for row in combined_comp2:
    print(row)

# Exercise
print("\nExercise")
chess_board = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH'[::-1]]
print(chess_board)
for row in chess_board:
    print(row)

