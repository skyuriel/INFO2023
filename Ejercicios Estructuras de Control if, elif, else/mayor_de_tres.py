n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el tercer numero: '))
if n1 > n2 and n1 > n3:
    print('El mayor de los numeros ingresados es el: ', str(n1))
elif n2 > n1 and n2 > n3:
    print('El mayor de los numeros ingresados es el: ', str(n2))
else:
    print('El mayor de los numeros ingresados es el: ', str(n3))