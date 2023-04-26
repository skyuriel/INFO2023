n1 = int(input('Ingrese un numero: '))
n2 = int(input('Ingrese otro numero: '))
if n1 % 2 == 0 and n2 % 2 == 0:
    print('Ambos numeros son par, el resultado de su suma es: ', str(n1 + n2))
else:
    print('Uno o ambos numeros son impares, la suma no se realizó.')