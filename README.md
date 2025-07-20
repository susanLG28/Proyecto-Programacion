# Proyecto Programacion Ahorcado
### Integrantes de codigo concreto: 
Susan Loraine Galindo Gomez

Martin David Monroy Bautista

# Juego del Ahorcado en Python

Este proyecto es una versión del clásico **Ahorcado**, desarrollada en Python. Permite practicar lógica de programación, manejo de archivos, estructuras de datos y validación de entradas, todo mientras juegas.

---

## ¿Qué es el Ahorcado? 

El Ahorcado es un juego tradicional de palabras que consiste en adivinar una palabra oculta, letra por letra. Cada error cometido acerca al jugador a completar el dibujo de una figura humana, lo que representa el límite de intentos permitidos. El objetivo es descubrir la palabra completa antes de que se termine el dibujo.

---

## ¿Qué hace nuestro juego ?

- Usa **archivos `.txt`** para cargar palabras clasificadas por categorías.
- Tiene **más de 1000 palabras**, distribuidas en 13 categorías.
- Permite elegir entre **tres niveles de dificultad**:
  - Fácil: palabras de hasta 5 letras (5 vidas)
  - Media: palabras de 6 a 9 letras (7 vidas)
  - Difícil: palabras de más de 9 letras (9 vidas)
- Muestra la palabra con rayas `_ _ _ _` e indica las letras adivinadas.
- Dibuja el ahorcado según el número de errores.
- Valida la entrada del usuario (solo letras, vocales con tilde, sin repetir, sin símbolos ni números).

---

## Categorías de palabras

El juego incluye 13 categorías, cada una con su propio archivo de palabras:

- Animales  
- Frutas  
- Países  
- Verduras  
- Tecnología  
- Profesiones  
- Deportes  
- Series  
- Películas  
- Razas de perros  
- Hogar  
- Palabras en inglés

---

## diagrama de flujo del juego

1. El usuario elige una categoría.
2. Selecciona una dificultad: fácil, media o difícil.
3. El programa elige una palabra aleatoria del archivo correspondiente.
4. Se inicia el juego: el usuario adivina letra por letra.
5. El juego termina al adivinar la palabra o perder todas las vidas.

---

## Lógica implementada

- Las palabras se leen desde archivos `.txt` con `open()`.
- Se usa `random.choice()` para seleccionar la palabra.
- Se muestran las letras acertadas en su posición.
- El número de vidas depende de la dificultad.
- Se dibuja el ahorcado progresivamente en texto.
- Se validan entradas: letras únicas, sin símbolos, sin repetir, acepta tildes

---

## Ejemplo visual del juego

![Imagen de WhatsApp 2025-07-20 a las 12 54 23_d28a4907](https://github.com/user-attachments/assets/34d46fdb-d71c-4792-bc8f-d87d2553606d)


