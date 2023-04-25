#  Pide al usuario el radio de un circulo y muestra su diametro, su circunferencia y su area #
radio = int(input('Ingresa el valor del radio: '))
pi = 3.14159
area = pi * (radio**2)
diametro = radio * 2
circunferencia = pi * diametro
print('El diametro del circulo es ' + str(diametro) + ', la circunferencia es ' + str(circunferencia) + ' y el area es ' + str(area))