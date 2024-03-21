import pygame
import sys
from clases import Personaje, Ataque, Enemigo, AtaqueEnemigo
# Variables.

ALTO = 400
ANCHO = 700


    # Posición y tamaño de la barra




class Juego:
    def iniciar(personaje, enemigo):
        salir = False
        pygame.init()
        # Establezco la pantalla.
        pantalla = pygame.display.set_mode((ANCHO, ALTO))

        # Establezco el título.
        pygame.display.set_caption("COMBATE")

        # Creo dos objetos surface.
        fondo = pygame.image.load("recursos/fondo.jpeg").convert()
        # .convert() convierten la superficie a un formato de color
        # que permite imprimirlas mucho mas rápido.

        # Objetos
        temporizador = pygame.time.Clock()
        personaje = Personaje(personaje)
        ataque = Ataque(personaje)
        enemigo = Enemigo(enemigo)
        ataqueEnemigo = AtaqueEnemigo(enemigo)

        # Movimiento del personaje.
        while not salir:

            

            

            # actualizacion grafica
            pantalla.blit(fondo, (0, 0))
            pantalla.blit(personaje.image, personaje.rect)
            pantalla.blit(ataque.image, ataque.rect)
            pantalla.blit(enemigo.image, enemigo.rect)
            pantalla.blit(ataqueEnemigo.image, ataqueEnemigo.rect)
            personaje.actualizar(pantalla)
            if enemigo.vida > 50:
                enemigo.actualizar()
            else:
                enemigo.dificil()

            ataqueEnemigo.update(personaje, enemigo)
            ataque.actualizar(enemigo)
            enemigo.actualizarMetricas(pantalla)
            print(enemigo.vida)

            pygame.display.update()

            
            temporizador.tick(60)
            if personaje.vida <= 0:
                pantalla.blit(fondo, (0, 0))
                texto = pygame.font.SysFont("Verdana", 48).render(f"{enemigo.nombre.title()} te ha derrotado", True, (255, 255, 255))
                pantalla.blit(texto, (20, 200))
                pygame.display.update()
                pygame.time.delay(1500)
            elif enemigo.vida <= 0:
                pantalla.blit(fondo, (0, 0))
                texto = pygame.font.SysFont("Verdana", 48).render(f"{personaje.nombre.title()} has ganado la batalla", True, (255, 255, 255))
                pantalla.blit(texto, (20, 200))
                pygame.display.update()
                pygame.time.delay(1500)
                salir = True

            # gestion de eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
        pygame.quit()
        print("Gracias por jugar...")
        print("Creditos (Jesús Calderón)")
        sys.exit()