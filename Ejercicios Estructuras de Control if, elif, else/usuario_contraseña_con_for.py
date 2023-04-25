# Valida usuario y contraseña #
import sys
usuario_ = 'SkyB'
contrasenia_ = '12131411'

for i in range(2):
    usuario = input('Ingrese su usuario: ')
    if usuario == usuario_:
        for i in range(2):
            contrasenia = input('Ingrese su contraseña: ')
            if contrasenia == contrasenia_:
                print('Acceso correcto. Bienvenidx!')
                sys.exit()
            else: 
                print('Error de contraseña.')
    else:
        print('Error de usuario.')