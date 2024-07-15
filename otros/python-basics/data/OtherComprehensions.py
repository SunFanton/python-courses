my_set_comp = {num for num in range(100)}
print(my_set_comp)

dict_comp = {num: num**2 for num in range(10)}
print(dict_comp)

tuple_comp = tuple(num for num in range(100))
print(tuple_comp)

# Exercise
exercise_dict = {letter: [num for num in range(1,6)] for letter in 'ABCDE'}
print(exercise_dict)