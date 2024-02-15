x = 0
while x < 10:
    x += 1
    if x == 5:
        #break # esto es para salir directamente del loop del while
        continue # esto se saltea la iteracion actual y pasa a la siguiente
    print("Iteracion ", x)

# exercise
my_list = []
x = 0
while x <= 100:
    if x % 2 == 0 and x != 58:
      my_list.append(x)
    x += 1

print(my_list)