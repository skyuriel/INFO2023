# Solicita al usuario su peso y su altura, calcula e imprime su indice de masa corporal (IMC) #

peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su altura en mts: '))
imc = peso / (altura ** 2)
print('Su indice de masa corporal es: ' + str(imc))