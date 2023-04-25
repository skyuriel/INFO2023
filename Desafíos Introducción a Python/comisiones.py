# Solicita nombre y total vendido, devuelve monto de comision #
nombre = input('Ingrese su nombre: ')
ventas_tot = float(input('Ingrese el monto vendido: '))
comision = (ventas_tot * 6) / 100
print('Hola ' + nombre + ' tus comisiones fueron de: ' + str(comision))