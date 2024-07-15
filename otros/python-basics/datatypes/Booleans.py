# booleans and numbers
print(1 == 1)
print(1 != 10)
print(1 < 10)
print(1 <= 10)
print(1 > 10)
print(not 1 > 10)
print(10 >= 10)

# booleans and lists and strings
print(1 in [1,2,3])
print(1 in (1,2,3))
print("e" in "hello")
print(4 not in [1,2,3])

print(not True)

dict = {1: 'one', 2: 'two', 3: 'three'}
print(1 in dict) # revisa en las keys
print(1 in dict.keys())
print("four" in dict.values())

# bool function
# values that returns falsy: 0, 0.0, '', [], (), {}, None
print(bool(123))
print(bool(0))
print(bool(None))
