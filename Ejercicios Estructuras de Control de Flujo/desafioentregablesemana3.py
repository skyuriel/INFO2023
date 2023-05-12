from random import randint
n = randint(1,100)
intentos = 8
name = input('Ingresa tu nombre: ')
print(f'{name}, tenés que adivinar un número entre 1 y 100, podés intentarlo 8 veces')
for i in range(0,9):
    if intentos <= 8:
        print('Te quedan ', intentos, ' intentos')
        intento = input('Ingresa un número entero: ')
        if intento.isdigit() == False:
            print('El número ingresado no es entero')
            continue
        else:
            if int(intento) == n:
                print('Ganaste!')
                break
            elif int(intento) < n:
                print('El número a adivinar es mayor al que ingresaste')
                intentos -= 1
            elif int(intento) > n:
                print('El número a adivinar es menor al que ingresaste')
                intentos -= 1
            else:
                print('Se acabaron los intentos :( \nEl número a adivinar era: ', n)
        
    
