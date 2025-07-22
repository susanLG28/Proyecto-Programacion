
import random

ahorcado_5 = [
    " ------\n |    |\n |     \n |      \n |      \n |\n--------",
    " ------\n |    |\n |    O\n |    | \n |      \n |\n--------",
    " ------\n |    |\n |    O\n |   /| \n |      \n |\n--------",
    " ------\n |    |\n |    O\n |   /|\\\n |      \n |\n--------",
    " ------\n |    |\n |    O\n |   /|\\\n |   /  \n |\n--------",
    " ------\n |    |\n |    O\n |   /|\\\n |   / \\\n |\n--------",    
]

ahorcado_7 = [
    "       \n       \n       \n        \n        \n  \n--------",
    " ------\n |    |\n |     \n |      \n |      \n |\n--------",
    " ------\n |    |\n |    O\n |      \n |      \n |\n--------",
    " ------\n |    |\n |    O\n |    | \n |      \n |\n--------",
    " ------\n |    |\n |    O\n |   /| \n |      \n |\n--------",
    " ------\n |    |\n |    O\n |   /|\\\n |      \n |\n--------",
    " ------\n |    |\n |    O\n |   /|\\\n |   /  \n |\n--------",
    " ------\n |    |\n |    O\n |   /|\\\n |   / \\\n |\n--------",   
]

ahorcado_9 = [
    "       \n       \n       \n        \n        \n  \n        ",
    "       \n       \n       \n        \n        \n  \n--------",
    " ------\n |    |\n |     \n |      \n |      \n |\n--------",
    " ------\n |    |\n |    o\n |      \n |      \n |\n--------",
    " ------\n |    |\n |    O\n |      \n |      \n |\n--------",
    " ------\n |    |\n |    O\n |    | \n |      \n |\n--------",
    " ------\n |    |\n |    O\n |   /| \n |      \n |\n--------",
    " ------\n |    |\n |    O\n |   /|\\\n |      \n |\n--------",
    " ------\n |    |\n |    O\n |   /|\\\n |   /  \n |\n--------",
    " ------\n |    |\n |    O\n |   /|\\\n |   / \\\n |\n--------",   
]

def mostrar_ahorcado(vidas_restantes, vidas_totales):
    if vidas_totales == 5:
        etapas = ahorcado_5
    elif vidas_totales == 7:
        etapas = ahorcado_7
    elif vidas_totales == 9:
        etapas = ahorcado_9
    else:
        print("(No hay dibujo para estas vidas)")
        return

    indice = vidas_totales - vidas_restantes
    indice = min(indice, len(etapas) - 1)
    print(etapas[indice])

def cargar_palabras(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    palabras = [linea.strip().lower() for linea in lineas if linea.strip()]
    return palabras

def clasificar_por_dificultad(palabras):
    dificultad = {
        'facil': [p for p in palabras if len(p.replace(" ", "")) <= 5],
        'media': [p for p in palabras if 6 <= len(p.replace(" ", "")) <= 9],
        'dificil': [p for p in palabras if len(p.replace(" ", "")) > 9],
    }
    return dificultad

def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ''
    for letra in palabra:
        if letra == ' ':
            resultado += '   '
        elif letra in letras_adivinadas:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado.strip()

def obtener_vidas(dificultad):
    if dificultad == 'facil':
        return 5
    elif dificultad == 'media':
        return 7
    elif dificultad == 'dificil':
        return 9

def jugar_ahorcado():
    categorias = {
        "1": "animales.txt",
        "2": "frutas.txt",
        "3": "paises.txt",
        "4": "verduras.txt",
        "5": "comida.txt",
        "6": "deportes.txt",
        "7": "hogar.txt",
        "8": "peliculas.txt",
        "9": "series.txt",
        "10": "profesiones.txt",
        "11": "tecnologia.txt",
        "12": "razas.txt",
        "13": "ingles.txt"

    }

    print("Categorías disponibles:")
    for clave, nombre in categorias.items():
        print(f"{clave}: {nombre.replace('.txt', '')}")

    opcion = input("Selecciona una categoría (1, 2, 3): ")
    if opcion not in categorias:
        print("Categoría inválida.")
        return

    palabras = cargar_palabras(categorias[opcion])
    dificultad_palabras = clasificar_por_dificultad(palabras)

    dificultad = input("Selecciona dificultad (facil, media, dificil): ").lower()
    if dificultad not in dificultad_palabras or not dificultad_palabras[dificultad]:
        print("Dificultad inválida o sin palabras.")
        return

    palabra = random.choice(dificultad_palabras[dificultad])
    vidas = obtener_vidas(dificultad)
    vidas_totales = vidas
    letras_adivinadas = set()
    letras_incorrectas = set()

    print("\n¡Comienza el juego!")
    while vidas > 0:
        print("\nPalabra:", mostrar_palabra(palabra, letras_adivinadas))
        print(f"Vidas restantes: {vidas}")
        mostrar_ahorcado(vidas, vidas_totales)
        if letras_incorrectas:
            print("Letras incorrectas:", ', '.join(sorted(letras_incorrectas)))

        intento = input("Adivina una letra: ").lower()

        if len(intento) != 1 or not intento.isalpha():
            print("Solo se permiten letras.")
            continue

        if intento in letras_adivinadas or intento in letras_incorrectas:
            print("Ya usaste esa letra.")
            continue

        if intento in palabra:
            letras_adivinadas.add(intento)
        else:
            letras_incorrectas.add(intento)
            vidas -= 1
            print("Letra incorrecta.")

        if all(letra in letras_adivinadas or letra == ' ' for letra in palabra):
            print("\n¡Felicidades! Adivinaste la palabra:", palabra)
            return

    print("\nPerdiste. La palabra era:", palabra)
    mostrar_ahorcado(0, vidas_totales)

jugar_ahorcado()
