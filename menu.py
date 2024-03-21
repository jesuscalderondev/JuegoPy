import pygame
import sys
from main import Juego

personajes = ["jiren", "vegeta"]
enemigos = ["vegeta", "jiren"]


import pygame

# Definir las opciones del menú
opciones = ["Jugar", "Opciones", "Salir"]

ALTO = 400
ANCHO = 700


class Menu():
    def __init__(self):
        pygame.init()
        self.personajes = 0
        self.enemigos = 0
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))


    def cambiarEnemigo(self):
        print(self.enemigos)

        if self.enemigos == 1:
            self.enemigos = 0
        elif self.enemigos == 0:
            self.enemigos = 1

    def cambiarPersonaje(self):
        print(self.personajes)

        if self.personajes == 1:
            self.personajes = 0
        elif self.personajes == 0:
            self.personajes = 1
    

    def mostrarMenu(self):

        texto = pygame.font.SysFont("Verdana", 48).render("VS", True, (255, 255, 255))
        personaje = pygame.image.load(f"recursos/{personajes[self.personajes]}/perfil.png")

        personaje = pygame.transform.scale(personaje, (int(personaje.get_width() / 5), int(personaje.get_height() / 5)))

        iniciar = pygame.font.SysFont("Verdana", 48).render("INCIAR", True, (255, 255, 255))

        enemigo = pygame.image.load(f"recursos/{enemigos[self.enemigos]}/perfil.png")
        enemigo = pygame.transform.scale(enemigo, (int(enemigo.get_width() / 5), int(enemigo.get_height() / 5)))
        fondo = pygame.image.load("recursos/fondo.jpeg").convert_alpha()

        self.pantalla.blit(fondo, (0, 0))
        self.pantalla.blit(personaje, (100, 100))
        self.pantalla.blit(enemigo, (450, 90))
        self.pantalla.blit(texto, (300, 150))
        self.pantalla.blit(iniciar, (250, 300))

# Ejecutar la función principal
if __name__ == "__main__":
    menu = Menu()
    while True:
        menu.mostrarMenu()
        pygame.display.set_caption("Hola")
        pygame.display.update()
        eventos = pygame.event.get()
        
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
            # Obtener la posición del mouse
                x, y = pygame.mouse.get_pos()
                print(x,y)

                if x in range(100, 220) and y in range(100, 260):
                    menu.cambiarPersonaje()
                elif x in range(400, 585) and y in range(100, 260):
                    menu.cambiarEnemigo()

            if evento.type == pygame.KEYDOWN:
                teclas = pygame.key.get_pressed()
                
                if teclas[pygame.K_RETURN]:
                    Juego.iniciar(personajes[menu.personajes], enemigos[menu.enemigos])

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
