"""
El match vendria a ser como el switch de otro lenguajes
"""

mood = "bored"

match mood:
    case "hungry":
        print("Buy food")
    case "thirsty":
        print("Drink water")
    case "tired":
        print("Go to rest")
    case _: # seria el equivalente al default en otros lenguajes
        print("any other mood")