def base2base(numero, bS, bD):
    decimal = 0
    potencia = 0
    nvalor = ''
    for digito in reversed(str(numero)):
        decimal += int(digito) * (bS ** potencia)
        potencia += 1
    while decimal > 0:
        nvalor = str(decimal % bD) + nvalor
        decimal //= bD
    return int(nvalor) if nvalor else 0
# Menu
while True:
    print("1. Convertir numero.")
    print("2. Salir del programa.")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        numero = int(input("Ingrese el numero: "))
        base = int(input("Ingrese la base numérica actual: "))
        nueva_base = int(input("Ingrese la base numérica nueva: "))
        conversion = base2base(numero, base, nueva_base)
        print(f"La conversion es: {conversion}")

    elif opcion == 2:
        break
