import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "ordenador", "desarrollador", "inteligencia"]
    return random.choice(palabras)

def mostrar_tablero(palabra_oculta, letras_adivinadas):
    tablero = ""
    for letra in palabra_oculta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero

def jugar_ahorcado():
    palabra_oculta = seleccionar_palabra()
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del ahorcado!")
    print(mostrar_tablero(palabra_oculta, letras_adivinadas))

    while True:
        if intentos == 0:
            print("¡Has perdido! La palabra correcta era:", palabra_oculta)
            break

        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("¡Ya has intentado con esa letra! Prueba con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_oculta:
            print("¡Letra correcta!")
        else:
            print("¡Letra incorrecta!")
            intentos -= 1

        tablero = mostrar_tablero(palabra_oculta, letras_adivinadas)
        print(tablero)

        if "_" not in tablero:
            print("¡Felicidades! ¡Has ganado!")
            break

def main():
    jugar_ahorcado()

if __name__ == "__main__":
    main()