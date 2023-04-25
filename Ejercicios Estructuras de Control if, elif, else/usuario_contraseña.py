# Valida usuario y contraseña #

usuario_ = 'SkyB'
contrasenia_ = '12131411'

usuario = input('Ingrese su usuario: ')
contrasenia = input('Ingrese su contraseña: ')

if usuario == usuario_ and contrasenia == contrasenia_:
    print('Acceso correcto. Bienvenidx!')
else: print('Usuario o contraseña invalidos, intente nuevamente')