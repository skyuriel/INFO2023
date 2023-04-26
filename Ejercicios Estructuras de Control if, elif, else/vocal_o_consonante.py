letra = input('Ingresa una letra: ')
letra = letra.lower()
vocales = ['a', 'e', 'i', 'o', 'u']
if letra in vocales:
    print('La letra ', letra, ' es una vocal.')
else:
    print('La letra ', letra, ' es una consonante.')