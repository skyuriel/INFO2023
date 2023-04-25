# Solicita al usuario su fecha de nacimiento en formato dd/mm/aaaa y luego imprime su edad en años #
from datetime import date
from datetime import datetime

fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
fecha_nacimiento = fecha_nacimiento.split('/', 2)
edad = datetime.now().year - int(fecha_nacimiento[2])
print("Tu edad es: " + str(edad) + ' años')