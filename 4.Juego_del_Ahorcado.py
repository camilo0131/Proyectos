import random

def obtener_palabra():
    palabras = ["python", "programacion", "computadora", "inteligencia", "tecnologia", "desarrollo"]
    return random.choice(palabras)

def mostrar_tablero(palabra_oculta, letras_correctas):
    print("\nPalabra: ", end="")
    for letra in palabra_oculta:
        if letra in letras_correctas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

def ingresar_letra():
    letra = input("Ingrese una letra: ").lower()
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingrese una sola letra válida.")
        return ingresar_letra()
    return letra

def jugar_ahorcado():
    palabra = obtener_palabra()
    palabra_oculta = "_" * len(palabra)
    letras_correctas = set()
    intentos = 7

    print("¡Bienvenido al juego del Ahorcado!")
    print("Tienes que adivinar la palabra secreta. ¡Buena suerte!")

    while intentos > 0:
        mostrar_tablero(palabra_oculta, letras_correctas)
        print("Intentos restantes:", intentos)

        letra = ingresar_letra()

        if letra in letras_correctas:
            print("Ya has ingresado esa letra. Intenta con otra.")
            continue

        if letra in palabra:
            letras_correctas.add(letra)
            palabra_oculta = "".join([letra if letra in letras_correctas else "_" for letra in palabra])

            if palabra_oculta == palabra:
                print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
                print("La palabra era:", palabra)
                break
        else:
            print("¡Letra incorrecta!")
            intentos -= 1

    else:
        print("¡Oh no! Te has quedado sin intentos. La palabra era:", palabra)

if __name__ == "__main__":
    jugar_ahorcado()