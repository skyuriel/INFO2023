# Solicita informacion personal e imprime por pantalla #
nombre_completo = input('Ingrese su nombre completo: ')
edad = input('Ingrese su edad: ')
estatura = input('Ingrese su estatura en cm: ')
peso = input('Ingrese su peso en kg: ')
direccion = input('Ingrese su direccion: ')
nro_telefono = input('Ingrese su numero de telefono: ')
info_personal = [nombre_completo, edad, estatura, peso, direccion, nro_telefono]
print('La informacion ingresada es la siguiente: ' + '\nNombre completo: ' + info_personal[0] + 
      '\nEdad: ' + info_personal[1] + '\nEstatura: ' + info_personal[2] + 'cm' + 
      '\nPeso: ' + info_personal[3] + '\nDireccion: ' + info_personal[4] +
      '\nNumero de telefono: ' + info_personal[5])