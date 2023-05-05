letras = []
txt = input('Ingrese texto a elección: ')
txt = txt.lower()

for i in range(3):
    letra = input('Ingrese una letra a elección: ') 
    letra = letra.lower()
    letras.append(letra)


contador1 = txt.count(letras[0])
contador2 = txt.count(letras[1])
contador3 = txt.count(letras[2])

txt_list = txt.split()
dic = {}
if 'python' in txt:
    dic = {'Python': True}
else:
    dic = {'Python': False}

print(f'El texto ingresado es: {txt}, las letras ingresadas son: {letras}')
print(f'La cantidad de veces que aparece la primer letra es: {contador1}, \nla cantidad de veces que aparece la segunda letra es: {contador2}, \nla tercer letra aparece {contador3} veces.')
print(f'El texto contiene {len(txt_list)} palabras.')
print(f'La primer palabra es: {txt_list[0]}, y la última es: {txt_list[-1]}')
print(f'El texto invertido es: {txt_list[::-1]}')
print(f'El resultado de la búsqueda de "Python" es: ', dic['Python'])