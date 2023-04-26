n = int(input('Ingrese un numero: '))
if n % 2 == 0 and n % 3 == 0:
    print('El numero ', str(n), ' es multiplo de 2 y de 3 a la vez.')
else:
    print('El numero ', str(n), ' no es multiplo de 2 y de 3 a la vez.')
