# Proyecto Programacion Ahorcado
### Integrantes de codigo concreto: 
Susan Loraine Galindo Gomez
Martin David Monroy Bautista

## Introducción del proyecto

El Ahorcado es un juego tradicional de palabras que consiste en adivinar una palabra oculta, letra por letra. Cada error cometido acerca al jugador a completar el dibujo de una figura humana, lo que representa el límite de intentos permitidos. El objetivo es descubrir la palabra completa antes de que se termine el dibujo.

En este proyecto desarrollaremos este entretenido juego utilizando Python, aplicando conceptos ya vistos en clase y otros que iremos aprendiendo a lo largo del curso. Este ejercicio nos permitirá practicar la lógica de programación, mejorar nuestras habilidades en Python y fortalecer nuestro conocimiento general del lenguaje.

## Elementos de nuestro codigo

* ### Lectura del diccionario de palabras:
Usamos varios archivos .txt para las categorias de las palabras tenemos 13 categorias:  


* ### Selección aleatoria de la palabra:

  Una vez que el diccionario de palabras ha sido cargado, el programa selecciona una palabra al azar para que el jugador la adivine. Esta selección aleatoria garantiza que cada partida sea diferente, lo que hace que el juego sea más dinámico y entretenido.

  Podemos utilizar la función "choice()" de la biblioteca random de Python. Esta función toma una lista como argumento y devuelve un elemento aleatorio de la misma. para el (.txt) se tiene que abrir el archivo y de ahi se escoje la palabra.

* ### Interfaz por consola:
  El juego se desarrollará a través de la consola, donde se mostrará al usuario toda la información relevante de forma clara. En cada turno, el jugador verá:

  #### Los espacios en blanco que representan las letras de la palabra oculta.

  la palabra : gato
  
  se veria asi: _ _ _ _
  
  #### Un historial de letras ingresadas.

  Letras usadas: n, m, e, l

  #### La cantidad de intentos restantes.

  Intentos restantes: 4

  

* ### Control de errores y validaciones:
  El código incluirá mecanismos para validar que el usuario solo introduzca letras (y no números ni símbolos), evitar letras repetidas ya ingresadas y manejar errores de entrada, todo con el objetivo de garantizar una experiencia fluida y sin fallos.

## Funcion de la logica de letras

Cuando el jugador escribe una letra, el programa revisa si esa letra está dentro de la palabra secreta. Si la letra sí está, se muestra en el lugar o lugares correctos. Si no está, se le resta un intento al jugador.

El juego muestra la palabra con guiones bajos (_) en lugar de las letras como se mostro anteriormente, y va revelando las letras correctas a medida que el jugador las adivina.

#### Ejemplo:
Palabra secreta: perro

Estado inicial: _ _ _ _ _

El jugador escribe: r

Resultado en pantalla: _ _ r r _

El programa seguira mostrando esta palabra parcialmente completada en cada turno, hasta que el jugador adivine toda la palabra o se le acaben los intentos.
Si se acaban los intentos se le dice al jugador cual era la respuesta correcta.

## Dibujo del ahorcado

se puede usar dibujo con texto.
Por ejemplo:

![Imagen de WhatsApp 2025-06-17 a las 21 21 05_d198c20a](https://github.com/user-attachments/assets/c89c5bf6-5f63-49ee-b96f-1908b25857ef)


Cada intento fallido va mostrando una parte más del cuerpo.

Sin embargo el profesor dijo de hacerlo en interfaz grafica ( no sabemos hacer eso todavia :(  )

## Ideas adicionales

Tenemos varias ideas que nos gustaria implememtar:

* Categorias de palabras: tener diferentes categorias como por ejemplo programacion, animales, paises, tecnologia, palabras en ingles, etc

  Si decidimos esto lo mas probable es que debamos crear mas archivos (.txt) cada uno para cada categoria.

* Puntaje: por ejemplo por cada letra adivinada se ganan 20 puntos, por letras seguidaa adivinadas 5 puntos más ( o sea adivina 1 letra +20, si adivina 2 seguidas +25 y asi). en el caso de fallar en alguna letra -7. o ahi vamos viendo como seria lo del puntaje.

* Se pueden hacer niveles de dificultad ya sea con las categorias o con las palabras (categorias más dificiles que otras o nivel de dificultad por la cantidad de letras de las palabras).
