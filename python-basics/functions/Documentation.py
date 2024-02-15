def test(a:int = 10, b:int = 0) -> int:
    # el int indica el tipo de dato esperado y el tipo de dato devuelto, pero esto es solo informativo
    '''A simple function that print 2 parameters'''
    print(a)
    print(b)
    return a + b

test(1,2)
print(test.__doc__)
help(test)