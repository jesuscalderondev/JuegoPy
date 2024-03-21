# Proyecto DBPY

### Clases

Las clases que se usaron para el proyecto fueron 4 clases instansiadas y 1 estática.

#### Personaje

Esta clase consta de un método constructor en donde se incia con el nombre del personaje, se crea la imagen para dicho personaje basados en las carpetas con los recursos, además de colocarlo en una posición inicial, para empezar con el combate

Tiene un método actualizar, que lo que hace es en cada llamada validar el estado de cada metrica, sea la vida, el ki o las teclas que se han pulsado para generar movimiento

Un metodo cargarKi, que lo que hace es llenar la barra de energía de nuestro personaje para poder utilizar el poder de ataque, ya que si este no tiene energiá no podrá realizar ataques

El método de actualizar metricas lo que hace es actualizar los valores de las barras, tanto de vida como de energía

### Enemigo

Esta clase guarda mucha similitud con el anterior, sólo que este es un objeto que tednrá acciones automaticas, para poder combatir contra nuestro personaje

### Ataque y AtaqueEnemigo

Esta clase es utilizada para poder llamar al ataque como un onjeto y así poder también validar su posición, compararla con la del objetivo y de esta manera poder determinar si le causa daño o no

### Cargador

Una clase estática, para redimensionar a los personajes, con dos métodos, cargarPersonajes y cargarAtaques, ambos métodos tienen un parametro opcional, que lo que hace es invertir en horizontal la imagen, ya que sirve para crear la imagen tanto del personaje como del enemigo

## Main

En el módulo main, creamos la funcionabilidad del juegon, el algoritmo con el que nuestro juego va a ejecutarse, como actualizar cada uno de los objetos

## Menu

En este tenemos un apartado para seleccionar nuestro personaje y su contrincante, dandole click en la carta, cambiaremos el personaje o enemigo. Presionando enter, comienza el juego