import random

ganadas = 0
perdidas = 0

print("Bienvenido al juego contra la banca ")

while True:
    if ganadas == 5:
        print("¡Felicidades! Ganaste 5 veces. Has ganado el juego.")
        break
    if perdidas == 3:
        print("Perdiste 3 veces. Fin del juego.")
        break

    decision = input("\n¿Quieres jugar esta ronda? (s/n): ").lower()
    if decision == 'n':
        print("Te retiraste del juego.")
        break
    elif decision != 's':
        print("Opción inválida. Escribe 's' para seguir o 'n' para retirarte.")
        continue

    cartasJugador = random.randint(1, 13)
    cartaBanca = random.randint(1, 13)

    print(f"Tu carta: {cartasJugador}")
    print(f"Carta de la banca: {cartaBanca}")

    if cartasJugador > cartaBanca:
        ganadas += 1
        print("¡Ganaste esta ronda!")
    elif cartasJugador < cartaBanca:
        perdidas += 1
        print("Perdiste esta ronda.")
    else:
        print("Empate. No cuenta para ganar o perder.")

    print(f"Marcador -> Ganadas: {ganadas} | Perdidas: {perdidas}")