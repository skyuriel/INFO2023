# Para saber tipo de dato #
from datetime import date
from datetime import datetime

fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
fecha_nacimiento = fecha_nacimiento.split('/', 2)
print(type(fecha_nacimiento[2]))
