"""
Las funciones lambda se definen asi:
lambda param: expression
Y esto siempre retorna el resultado

Razones para usar lambdas:
- Hay funciones que requieren que se pasen por argumento otras funciones
(los argumentos serian las lambdas). Ej, la funcion sort()
- Para interfaces graficas de usuarios. Por ej, para una funcionalidad sencilla
de un boton
"""

a = lambda x: x + 1
simple_cal = lambda a,b: a + b
print(a(10))
print(simple_cal(10,2))

# exercise
exercise = lambda x: "hello" if x > 5 else "bye"
print(exercise(6))