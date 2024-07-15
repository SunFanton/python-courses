# quotes for strings:
test_var = "Test 1"
test_var2 = 'Test 2'
print(test_var)
print(test_var2)

# quotes inside strings
test_var3 = 'He said "there is no problem"'
test_var4 = '\"\'' # simple escape character
print(test_var3)
print(test_var4)

# escape characters
test_var5 = "Line 1: some text \nLine 2: some other text"
test_var6 = "Some text \tSome ohter text"
print(test_var5)
print(test_var6)

# multiple lines
'''Python toma los espacios y saltos de linea de los strings que tienen 
triple comillas, sin necesidad de agregar caracteres especiales de escape'''
test_var7 = '''Hola, esta es una linea.
Y esta es otra linea'''
print(test_var7)

# math and strings
test_var8 = "Hello" + ' ' + "world!"
print(test_var8)
test_var9 = "copy"
print(test_var9 * 10)

# values into strings
name = "Tom"
age = 40
greeting_message = "Hello {}, you are {} years old".format(name, age)
print(greeting_message)
# otra forma:
greeting_message = "Hello {one}, you are {two} years old".format(one = name, two = age);
print(greeting_message);
# otra forma mas eficiente (agregando las variables y la f):
greeting_message = f"Hello {name}, you are {age} years old"
print(greeting_message)

# exercise
example_name = "Sol"
example_hobby = "draw"
example = f"Hello, my name is {example_name} \nand my hobby is {example_hobby}"
example2 = f'''Hello, my name is {example_name} 
and my hobby is {example_hobby}'''
print(example)
print(example2)