# Solicita una temperatura en grados Celsius y la convierte a Farenheit #

grados_c = float(input('Ingrese temperatura en grados Celsius: '))
grados_f = (grados_c * 1.8) + 32
print('La temperatura ' + str(grados_c) + ' grados Celsius, es equivalente a ' + 
      str(grados_f) + ' grados Farenheit')