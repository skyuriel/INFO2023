palabra = input('Ingrese una palabra:')

for letra in range(len(palabra)-1, -1, -1):
    print(palabra[letra])