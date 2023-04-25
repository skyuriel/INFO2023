# Solicita al usuario su fecha de nacimiento en formato dd/mm/aaaa y luego imprime su edad en años #
from datetime import date
from datetime import datetime

fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
edad = datetime.now().year - fecha_nacimiento.year
print("Tu edad es: " + str(edad) + ' años')