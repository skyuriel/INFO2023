# Solicita al usuario dos numeros e imprime su suma, resta, multiplicacion y division #
nro_1 = int(input('Ingrese el primer numero: '))
nro_2 = int(input('Ingrese el segundo numero: '))
suma = nro_1 + nro_2
resta = nro_1 - nro_2
multiplicacion = nro_1 * nro_2
division = nro_1 / nro_2
print('La suma entre ambos numeros da: ' + str(suma) + ', la resta da: ' + str(resta) + 
      ', \nla multiplicacion resulta en: ' + str(multiplicacion) + ' y la division en: ' + str(division)
      )