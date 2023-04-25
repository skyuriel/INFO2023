# Solicita al usuario su nombre e imprime un mensaje que indica cuantos años tendra el usuario en 10 años mas #
nombre = input("Ingrese su nombre: ")
edad = int(input('Ingrese su edad: '))
edad += 10
print(nombre.capitalize() + ' en diez años tendrás ' + str(edad) + ' años de edad')