frase = input("Por favor ingrese una frase cualquiera: ")
letraUno = input("Por favor ingrese una letra: ")
letraDos = input("Por favor ingrese una segunda letra: ")
letraTres = input("Por favor ingrese una tercer letra: ")

frase = frase.lower()
letraUno = letraUno.lower()
letraDos = letraDos.lower()
letraTres = letraTres.lower()

cuentaLetraUno = frase.count(letraUno)
cuentaLetraDos = frase.count(letraDos)
cuentaLetraTres = frase.count(letraTres)
print(f"La primer letra {letraUno} aparece {cuentaLetraUno} veces.")
print(f"La segunda letra {letraDos} aparece {cuentaLetraDos} veces.")
print(f"La tercer letra {letraTres} aparece {cuentaLetraTres} veces.")

palabras = frase.split()
cantidadPalabras = len(palabras)
print(f"La frase contiene un total de {cantidadPalabras} palabras.")

primerLetra = frase[0]
ultimaLetra = frase[-1]
print(f"La primer letra de la frase es {primerLetra} y la ultima frase es {ultimaLetra}.")

fraseInversa = frase[::-1]
print(f"En orden inverso la frase seria: {fraseInversa}")

diccionario = {True: "sí", False: "no"}
pythonAparece = "python" in frase.lower()
print(f"La palabra 'python' {diccionario[pythonAparece]} aparece en la frase.")