total = 0

while True:
    print("Máquina expendedora")
    print("1. Café ($3.000)")
    print("2. Té ($2.500)")
    print("3. Jugo ($3.500)")
    print("0. Salir")

    opcion = int(input("Selecciona una opción (0-3): "))

    match opcion:
        case 1:
            print("Elegiste café - $3.000")
            total += 3000
        case 2:
            print("Elegiste té - $2.500")
            total += 2500
        case 3:
            print("Elegiste jugo - $3.500")
            total += 3500
        case 0:
            print(f"\nTotal a pagar: ${total}")
            print("Gracias por usar la máquina expendedora.")
            break