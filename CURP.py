print("Crea tu CURP")
NOMBRE = input("Ingresa tu nombre")
Primera_letra = NOMBRE[0]
segundo_nombre = input("Ingresa un segundo nombre si tienes")
segunda_letra = segundo_nombre[0]
EDAD = int(input("Ingresa tu edad"))
PATERNO = input("Ingresa tu apellido")
CURP = Primera_letra+segunda_letra+str(EDAD) + PATERNO
print("Tu CURP es:", CURP)
