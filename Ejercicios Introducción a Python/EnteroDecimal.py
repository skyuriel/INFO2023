# Solicita un numero decimal e imprime la parte entera y decimal por separado #

import math
numero = float(input('Ingrese un numero decimal: '))
decimal, entero = math.modf(numero)
print("Su parte entera es {} y su parte decimal es {}".format(
    entero, decimal))
