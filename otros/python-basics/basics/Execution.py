"""
En Python no se utiliza el ; excepto cuando se quiere colocar en una misma linea fisica dos o mas lineas logicas
Por otra parte, en Python es FUNDAMENTAL la identacion 
Por ultimo, si tenemos en una misma linea una operacion muy larga y compleja, tanto que convendria visualmente tenerla en lineas separadas, 
eso es posible a traves de '\'
"""

print("Linea 1")
print("Linea 2")
print("Linea 3"); print("Linea 4")

a = 1 + 2 + 3 + 4 + 5 \
    + 6 + 7 + 8
print(a)