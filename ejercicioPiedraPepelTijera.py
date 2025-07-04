import random

# Pedir número de rondas
totalRondas = int(input("¿Cuántas rondas deseas jugar?: "))
rondaActual = 1
puntosJugador = 0
puntosComputadora = 0

print("\nOpciones: piedra, papel, tijera")

while rondaActual <= totalRondas:
    print("\nRonda:", rondaActual, "de", totalRondas)

    jugador = input("Tu jugada: ").lower()
    pc = random.randint(1, 3)

    # Traducir número a jugada
    if pc == 1:
        computadora = "piedra"
    elif pc == 2:
        computadora = "papel"
    else:
        computadora = "tijera"

    print("Jugador:", jugador)
    print("Computadora:", computadora)

    # Verificar quién gana la ronda
    if jugador == computadora:
        print("Empate en esta ronda.")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("Jugador ha ganado esta ronda.")
        puntosJugador += 1
    elif (computadora == "piedra" and jugador == "tijera") or \
         (computadora == "papel" and jugador == "piedra") or \
         (computadora == "tijera" and jugador == "papel"):
        print("Computadora ha ganado esta ronda.")
        puntosComputadora += 1
    else:
        print("Jugada inválida. No se cuenta la ronda.")
        continue  

    # Mostrar puntaje
    print("Puntaje:\n", puntosJugador, "(Jugador) \n", puntosComputadora, "(Computadora)")
    rondaActual += 1

# Resultado final
print("\n--- Resultado Final ---")
print("Jugador:", puntosJugador)
print("Computadora:", puntosComputadora)

if puntosJugador > puntosComputadora:
    print("¡Ganaste el juego!")
elif puntosJugador < puntosComputadora:
    print("Perdiste el juego.")
else:
    print("El juego terminó en empate.")