print(" ##### Combining conditions #####")

"""
Python une todas las condiciones con and bajo un mismo bloque.
Lo de abajo es como si tuviera en otro lenguaje:
if((true && true && false) || true)

De nuevo, la identacion es FUNDAMENTAL par aidentificar bloques de codigo en Pyhton
"""

if True and True and False or True:
    print("True")

# exercise
money_available = 100
hungry = True
bored = True

if money_available > 80 and hungry or bored:
    print("Comprar algo para almorzar")

print(" ##### Nested conditions #####")

x = 'a'
if x in ['a', 'b', 'c']:
    print("a is in the list")
    if x.isalpha():
        print('a is a letter')