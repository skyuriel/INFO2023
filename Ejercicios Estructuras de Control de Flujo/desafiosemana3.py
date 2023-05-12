from random import randint
n = randint(1,100)
intentos = 8
name = input('Ingresa tu nombre: ')
print(f'{name}, tenés que adivinar un número entre 1 y 100, podés intentarlo 8 veces')
while intentos > 0:
     print('Te quedan ', intentos, ' intentos')
     intento = input('Ingresa un número entero: ')
     if intento.isdigit() == False:
            print('El número ingresado no es entero')
            continue
     intento = int(intento)
     if intento == n:
         print('Ganaste!')
         break
     elif intento < n: 
        print('El número a adivinar es mayor al que ingresaste')
        intentos -= 1
     elif intento > n:
        print('El número a adivinar es menor al que ingresaste')
        intentos -= 1
else:
    print('Se acabaron los intentos :( \nEl número a adivinar era: ', n)   

