#  Solicita al usuario dos palabras y las imprime en orden inverso #

palabra_1= input('Ingrese la primer palabra: ')
palabra_2 = input('Ingrese la segunda palabra: ')
lista = [palabra_1, palabra_2]
lista.reverse()
print(' '.join(lista))