#Import.co
import random
import time  

# Diccionario 
preguntas = {
     1: [
        {'pregunta': '¿Cual es el oceano mas grande del mundo?', 
         'opciones': ['a) Atlantico', 'b) Indico', 'c) Pacifico', 'd) Artico'], 
         'respuesta': 'c'},
        {'pregunta': '¿Que planeta es conocido como el planeta rojo?', 
         'opciones': ['a) Venus', 'b) Marte', 'c) Jupiter', 'd) Saturno'], 
         'respuesta': 'b'}
    ],
    2: [
        {'pregunta': '¿Quien pinto la mona lisa?', 
         'opciones': ['a) Miguel angel', 'b) Vicent van gogh', 'c) Leonardo da vinci', 'd) Pablo picasso'], 
         'respuesta': 'c'},
        {'pregunta': '¿Cual es la capital de mexico?', 
         'opciones': ['a) Guadalajara', 'b) Monterrey', 'c) Ciudad de mexico', 'd) Cancun'], 
         'respuesta': 'c'}
    ],
    3: [
        {'pregunta': '¿En que pais se originaron los juegos olimpicos?', 
         'opciones': ['a) Italia', 'b) Egipto', 'c) Grecia', 'd) Turquia'], 
         'respuesta': 'c'},
        {'pregunta': '¿Que intrumento musical tiene teclas blancas y negras?', 
         'opciones': ['a) Violin', 'b) Piano', 'c) Guitarra', 'd) Flauta'], 
         'respuesta': 'b'}
    ],
    4: [
        {'pregunta': '¿Que gas es esencial para que respiremos?', 
         'opciones': ['a) Dioxido de carbano', 'b) Oxigeno', 'c) Hidrogeno', 'd) Nitrogeno'], 
         'respuesta': 'b'},
        {'pregunta': '¿En que continente esta egipto?', 
         'opciones': ['a) Asia', 'b) Europa', 'c) America', 'd) Africa'], 
         'respuesta': 'd'}
    ],
    5: [
        {'pregunta': '¿Cual es el metal mas utilizado para fabricar cables electronicos?', 
         'opciones': ['a) Oro', 'b) Plata', 'c) Cobre', 'd) Aluminio'], 
         'respuesta': 'c'},
        {'pregunta': '¿Que país tiene forma de bota en el mapa?', 
         'opciones': ['a) Grecia', 'b) Francia', 'c) Italia', 'd) Portugal'], 
         'respuesta': 'c'}
    ],
    6: [
        {'pregunta': '¿Que escritor creó el personaje de Sherlock Holmes?', 
         'opciones': ['a) Agatha Christie', 'b) Edgar Allan Poe', 'c) Arthur Conan Doyle', 'd) Oscar Wilde'], 
         'respuesta': 'c'},
        {'pregunta': '¿Cual es el río más largo del mundo (según algunos estudios)?', 
         'opciones': ['a) Amazonas', 'b) Nilo', 'c) Misisipi', 'd) Yangtsé'], 
         'respuesta': 'b'}
    ],
    7: [
        {'pregunta': '¿Cual es el símbolo químico del oro?', 
         'opciones': ['a) Go', 'b) Ag', 'c) Au', 'd) Or'], 
         'respuesta': 'c'},
        {'pregunta': '¿Cual fue la primera civilización que usó escritura?', 
         'opciones': ['a) Egipcios', 'b) Romanos', 'c) Sumerios', 'd) Persas'], 
         'respuesta': 'c'}
    ],
    8: [
        {'pregunta': '¿Que científico propuso la teoría del Big Bang?', 
         'opciones': ['a) Stephen Hawking', 'b) Georges Lemaître', 'c) Edwin Hubble', 'd) Albert Einstein'], 
         'respuesta': 'b'},
        {'pregunta': '¿Cual es la capital de Mongolia?', 
         'opciones': ['a) Taskent', 'b) Ulaanbaatar', 'c) Astana', 'd) Bakú'], 
         'respuesta': 'b'}
    ],
    9: [
        {'pregunta': '¿Que autor escribió “Cien años de soledad”?', 
         'opciones': ['a) Mario Vargas Llosa', 'b) Gabriel García Márquez', 'c) Pablo Neruda', 'd) Julio Cortázar'], 
         'respuesta': 'b'},
        {'pregunta': '¿Que órgano del cuerpo humano produce insulina?', 
         'opciones': ['a) Hígado', 'b) Riñón', 'c) Páncreas', 'd) Estómago'], 
         'respuesta': 'c'}
    ],
    10: [
        {'pregunta': '¿Que país tiene más premios Nobel de Literatura?', 
         'opciones': ['a) Alemania', 'b) Francia', 'c) Inglaterra', 'd) EE.UU.'], 
         'respuesta': 'b'},
        {'pregunta': '¿Que físico dijo “Dios no juega a los dados”?', 
         'opciones': ['a) Isaac Newton', 'b) Albert Einstein', 'c) Max Planck', 'd) Niels Bohr'], 
         'respuesta': 'b'}
    ]
}

# Variables
dinero = 0
recompensa = 1000000
comodinUsado1 = False
comodinUsado2 = False
comodinUsado3 = False
usandoC2 = False

# Tiempo de inicio y límite
tiempoInicio = time.time()
tiempoFinal = 15 * 60  

# Bienvenida
print("🧠Bienvenido a ¡Quién Quiere Ser Millonario!\n")
nombre = input("¿Cómo te llamas?😊: ")
print("Iniciemos el juego", nombre, "\n")

# Selección de preguntas 
for nivel in range(1, 11):

# Verificar si se acabó el tiempo
    tiempoActual = time.time()
    if tiempoActual - tiempoInicio >= tiempoFinal:
        print("⏰ ¡Se acabó el tiempo! Fin del juego.😢")
        exit()

# Mostrar tiempo antes de la pregunta
    tiempoRestante = int((tiempoInicio + tiempoFinal) - time.time())
    minutos = tiempoRestante // 60
    segundos = tiempoRestante % 60
    print(f"⏳ Tiempo restante:                                        {minutos}m {segundos}s\n💀")

#Seleccion de pregunta
    print(f"Nivel {nivel}")
    indicePregunta = random.choice([0, 1])
    preguntaActual = preguntas[nivel][indicePregunta]
    usadaAlternativa = False  

# Mostrar pregunta con sus opciones
    while True:
        if not usandoC2:    
            print(preguntaActual['pregunta'])
            for opcion in preguntaActual['opciones']:
                print(opcion)
        if usandoC2:
            usandoC2 = False

        correcta = preguntaActual['respuesta']
        respuesta = input('¿Cuál es tu respuesta? (o escribe "comodines"): ').lower()

# Verificar tiempo antes de continuar
        if time.time() - tiempoInicio >= tiempoFinal:
            print("⏰ ¡Se acabó el tiempo! Fin del juego.🤨")
            exit()

# Comodines
        if respuesta == 'comodines':
            print("Comodines disponibles:")
            if not comodinUsado1:
                print("1. Llamar a un amigo👨🏿‍🤝‍👨🏿")
            if not comodinUsado2:
                print("2. 50/50 (eliminar dos incorrectas)🥱")
            if not comodinUsado3:
                print("3. Cambiar de pregunta \n🐤")

            eleccion = input("¿Cuál comodín quieres usar? (1, 2 o 3)😂: ")

            if eleccion == '1' and not comodinUsado1:
                sugerencia = random.choice(['a', 'b', 'c', 'd'])
                print("Tu amigo sugiere que la respuesta es:", sugerencia)
                comodinUsado1 = True

            elif eleccion == '2' and not comodinUsado2:
                incorrectas = [letra for letra in ['a', 'b', 'c', 'd'] if letra != correcta]
                incorrecta_elegida = random.choice(incorrectas)
                print("Opciones posibles después del 50/50:\n")
                for letra in [correcta, incorrecta_elegida]:
                    for x in preguntaActual['opciones']:
                        if x.startswith(letra + ')'):
                            print(x)
                comodinUsado2 = True
                usandoC2 = True

            elif eleccion == '3' and not comodinUsado3:
                if not usadaAlternativa:
                    indice_alterna = 1 if indicePregunta == 0 else 0
                    preguntaActual = preguntas[nivel][indice_alterna]
                    usadaAlternativa = True
                    comodinUsado3 = True
                    print("\nCambiando a otra pregunta...\n")
                else:
                    print("Ya cambiaste esta pregunta una vez. No puedes usar este comodín de nuevo.🙄")
            else:
                print("Ese comodín ya fue usado o no es válido.😖🥱")

        else:
            if respuesta == correcta:
                dinero += recompensa
                print("¡Correcto! Llevas acumulado🤑:", dinero, "\n")
                if dinero == 10000000:
                    print("🎉 ¡Felicidades has ganado el juego! Tienes un nivel intelectual de 500.🤯💀")
            else:
                print("❌ Respuesta incorrecta. Fin del juego.❌")
                exit()
            break