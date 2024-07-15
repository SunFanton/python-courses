x = 0
if x > 10:
    print("La condición if es cierta")
    print("otra linea")
elif x != 0:
    print("La condición elif es correcta")
else:
    print("La condición else es cierta")
print("Codigo fuera del bloque del if por no estar identado")

# exercise
money_available = 100
if money_available >= 85:
    print("Eat something expensive")
elif money_available > 45:
    print("Eat something nice")
elif money_available > 15:
    print("Eat something okay")
else:
    print("Eat something cheap")