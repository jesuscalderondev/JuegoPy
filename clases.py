import pygame

class Personaje(pygame.sprite.Sprite):
    def __init__(self, nombre:str):
        self.image = personaje = Cargador.cargarPersonajes(f"recursos/{nombre}/normal.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(50, 300)
        self.muerto = 0
        self.ki = 0
        self.nombre = nombre
        self.vida = 100
        

    def cargarKi(self):
        if self.ki < 500:
            #eliminar
            print(self.ki)
            self.ki += 5
            if self.ki < 500:
                self.image = personaje = Cargador.cargarPersonajes(f"recursos/{self.nombre}/recarga.png")

            

    def actualizar(self, pantalla):

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_SPACE]:
            if self.ki >= 0:
                self.image = personaje = Cargador.cargarPersonajes(f"recursos/{self.nombre}/dispara.png")
                self.ki -= 5

        elif teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.image = personaje = Cargador.cargarPersonajes(f"recursos/{self.nombre}/atras.png")
            if self.rect.x > 0:
                self.rect.x -= 10
        elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.image = personaje = Cargador.cargarPersonajes(f"recursos/{self.nombre}/delante.png")
            if self.rect.x < 740:
                self.rect.x += 10

        elif teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.image = personaje = Cargador.cargarPersonajes(f"recursos/{self.nombre}/sube.png")
            if self.rect.y > 100:
                self.rect.y -= 20

        elif teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            if self.rect.y < 530:
                self.image = personaje = Cargador.cargarPersonajes(f"recursos/{self.nombre}/baja.png")
                self.rect.y += 5
        
        elif teclas[pygame.K_q]:
            self.cargarKi()

        else:
            self.image = personaje = Cargador.cargarPersonajes(f"recursos/{self.nombre}/normal.png")
        
        self.actualizarMetricas(pantalla)

        
    def actualizarMetricas(self, pantalla):
        ancho = 200
        alto = 20

        # Calcular el ancho actual de la barra
        vida = int((self.vida / 100) * ancho)
        ki = int((self.ki/500) * (ancho - 50))

        carta = pygame.image.load(f"recursos/{self.nombre}/perfil.png")

        carta = pygame.transform.scale(carta, (int(carta.get_width() / 9), int(carta.get_height() / 9)))

        pantalla.blit(carta, (0,0))
        # Dibujar el fondo de la barra
        pygame.draw.rect(pantalla, (255, 0, 0), (50, 50, ancho, alto))

        # Dibujar la barra de vida actual
        pygame.draw.rect(pantalla, (0, 255, 0), (50, 50, vida, alto))

        pygame.draw.rect(pantalla, (250, 192, 1), (50, 70, ancho - 50, alto/4))

        # Dibujar la barra de vida actual
        pygame.draw.rect(pantalla, (0, 129, 250), (50, 70, ki, alto/4))

    
class Ataque(pygame.sprite.Sprite):
    def __init__(self, personaje):
        self.image = ataque =  Cargador.cargarAtaques(f"recursos/{personaje.nombre}/ataque.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(900, 700)
        self.personaje = personaje

    def actualizar(self, enemigo):
        teclas = pygame.key.get_pressed()
        if self.rect.x > 740:
            if teclas[pygame.K_SPACE]:
                if self.personaje.ki > 0:
                    self.rect.x = (self.personaje.rect.x + 60)
                    self.rect.y = (self.personaje.rect.y + 14)
        if self.rect.x < 770:
            self.rect.x += 20

        if self.rect.y >= enemigo.rect.y:
            if self.rect.y <= (enemigo.rect.y + 70):
                if self.rect.x >= enemigo.rect.x + 20 and self.rect.x <= (enemigo.rect.x + 43):
                    enemigo.vida -= 5
                    self.rect.x = 900


class Enemigo(pygame.sprite.Sprite):
    def __init__(self, nombre:str):
        self.image = enemigo = Cargador.cargarPersonajes(f"recursos/{nombre}/normal.png", invertido=True)
        self.rect = self.image.get_rect()
        self.rect.move_ip(640, 300)
        self.bandera = 0
        self.muerto = 0
        self.ki = 500
        self.vida = 100
        self.nombre = nombre

    def actualizar(self):
        if self.rect.y == 40:
            self.bandera = 0
        elif self.rect.y == 540:
            self.bandera = 1

        if self.bandera == 0:
            self.rect.y += 10
        elif self.bandera == 1:
            self.rect.y -= 10

        
        if 0 <= self.ki < 50:
            print(self.ki, "Ki enemigo")
            self.image = Cargador.cargarPersonajes(f"recursos/{self.nombre}/recarga.png", True)
            self.ki += 5
        else:
            self.image = Cargador.cargarPersonajes(f"recursos/{self.nombre}/normal.png", True)

            

    def dificil(self):
        if self.rect.x < 0:
            self.rect.x = 800
        if self.rect.y > 600:
            self.rect.y = 0
        self.rect.x -= 10
        self.rect.y += 10

    def actualizarMetricas(self, pantalla):
        ancho = 200
        alto = 20

        # Calcular el ancho actual de la barra
        vida = int((self.vida / 100) * ancho)
        ki = int((self.ki/500) * (ancho - 50))

        carta = pygame.image.load(f"recursos/{self.nombre}/perfil.png")

        carta = pygame.transform.scale(carta, (int(carta.get_width() / 9), int(carta.get_height() / 9)))

        pantalla.blit(carta, (640,0))
        # Dibujar el fondo de la barra
        pygame.draw.rect(pantalla, (255, 0, 0), (450, 50, ancho, alto))

        # Dibujar la barra de vida actual
        pygame.draw.rect(pantalla, (0, 255, 0), (450, 50, vida, alto))
        
        pygame.draw.rect(pantalla, (250, 192, 1), (500, 70, ancho - 50, alto/4))
        pygame.draw.rect(pantalla, (0, 129, 250), (500, 70, ki, alto/4))

        # Dibujar la barra de vida actual
        


class AtaqueEnemigo:
    def __init__(self, enemigo):
        self.image = ataqueEnemigo = Cargador.cargarAtaques(f"recursos/{enemigo.nombre}/ataque.png", invertido=True)
        self.rect = self.image.get_rect()
        self.rect.move_ip(-400, -400)

    def update(self, personaje, enemigo):


        if self.rect.x == -400:
            if enemigo.rect.y == personaje.rect.y:
                self.rect.x = (enemigo.rect.x - 60)
                self.rect.y = (enemigo.rect.y - 14)
                enemigo.ki -= 5
        if self.rect.x > -400:
            self.rect.x -= 5
            enemigo.ki -= 5
        
        if self.rect.y >= (personaje.rect.y - 56):
            if self.rect.y <= (personaje.rect.y + 62):
                if self.rect.x >= personaje.rect.x:
                    if self.rect.x <= (personaje.rect.x + 43):
                        personaje.vida -= 10
                        self.rect.x = -400

        if enemigo.rect.y >= (personaje.rect.y - 56):
            if enemigo.rect.y <= (personaje.rect.y + 62):
                if enemigo.rect.x >= personaje.rect.x:
                    if enemigo.rect.x <= (personaje.rect.x + 43):
                        personaje.vida -= 10
                        self.rect.x = -400

class Cargador:

    def cargarPersonajes(ruta, invertido = False):
        personaje = pygame.image.load(ruta).convert_alpha()
        personaje = pygame.transform.scale(personaje, (int(personaje.get_width() / 6), int(personaje.get_height() / 6)))
        if invertido:
            return pygame.transform.flip(personaje, True, False)
        return personaje
    
    def cargarAtaques(ruta, invertido = False):
        ataque = pygame.image.load(ruta).convert_alpha()
        ataque = pygame.transform.scale(ataque, (int(ataque.get_width() / 6), int(ataque.get_height() / 6)))
        if invertido:
            return pygame.transform.flip(ataque, True, False)
        return ataque