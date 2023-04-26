caracter = input('Ingrese un caracter: ')
if caracter.isupper():
    print('El caracter ', str(caracter), ' es mayuscula.')
elif caracter.islower():
    print('El caracter ', str(caracter), ' es minuscula.')
elif caracter.isdigit():
    print('El caracter ', str(caracter), ' es un numero.')
else:
    print('El caracter ', str(caracter), ' es un caracter especial')