externa = "EXTERNA" # variable global

def funcion(parametro): # parametro es variable local de la funcion
    interna = "INTERNA" # variable local de la funcion
    print("Adentro", externa, parametro, interna)

funcion("PARAMETRO")

print("Afuera", externa, interna, parametro) # da error porque interna y parametro son variables que solo viven dentro de funcion(), cuando dicha funcion se esta ejecutando
