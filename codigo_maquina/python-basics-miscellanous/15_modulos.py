# Dentro de un modulo puede haber, entre otros, constantes, variables, funciones...

#import math # importar modulo
#import math as m # importar modulo bajo un alias
#from math import ceil, floor # importar funcionalidades especificas del modulo
from math import * # importar todas las funcionalidades del modulo

#help(math) # muestra toda la documentacion del modulo

#print(math.ceil(2.1), math.floor(2.1))
#print("ceil: ", m.ceil(2.1), ", floor: ", m.floor(2.1))
print("ceil: ", ceil(2.1), ", floor: ", floor(2.1))