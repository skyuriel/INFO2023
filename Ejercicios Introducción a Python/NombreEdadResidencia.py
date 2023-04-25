# Pide al usuario su nombre, su edad y su ciudad de residencia, y lo muestra en pantalla #

nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
ciudad = input('Ingrese su ciudad de residencia: ')
nombre_edad_ciudad = [nombre, edad, ciudad]
print('Nombre: ' + nombre_edad_ciudad[0] + '\nEdad: ' + nombre_edad_ciudad[1] + '\nReside en: ' + nombre_edad_ciudad[2])