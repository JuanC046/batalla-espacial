import pygame
from nave import Nave
from nave_enemiga import NaveEnemiga
import random
import time


class Juego:
    def __init__(self):
        pygame.mixer.init()
        self.sonido_disparo = pygame.mixer.Sound("./assets/shoot2.mp3")
        self.sonido_explosion = pygame.mixer.Sound("./assets/explosion.mp3")
        self.game_over = pygame.mixer.Sound("./assets/game_over.mp3")

        self.background = pygame.image.load("./assets/background.jpg")
        
        self.ANCHO, self.ALTO = 800, 600
        self.VENTANA = pygame.display.set_mode((self.ANCHO, self.ALTO))
        self.jugador = Nave(400, 500)
        self.enemigos = []
        self.ejecutar = True
        self.ultimo_tiempo_enemigo = time.time()
        self.fuente = pygame.font.SysFont("comicsans", 30)

    def bucle_principal(self):
        reloj = pygame.time.Clock()
        while self.ejecutar:
            reloj.tick(60)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.ejecutar = False
                    return

            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] and self.jugador.x - 5 > 0:
                self.jugador.x -= 5
            if (
                teclas[pygame.K_RIGHT]
                and self.jugador.x + 5 + self.jugador.img_nave.get_width() < self.ANCHO
            ):
                self.jugador.x += 5
            if teclas[pygame.K_UP] and self.jugador.y - 5 > self.ALTO * 2 / 3:
                self.jugador.y -= 5
            if (
                teclas[pygame.K_DOWN]
                and self.jugador.y + 5 + self.jugador.img_nave.get_height() < self.ALTO
            ):
                self.jugador.y += 5
            if teclas[pygame.K_SPACE]:
                self.sonido_disparo.play()
                self.jugador.disparar()

            self.mover_enemigos()
            self.jugador.mover_balas(-5, self.enemigos)
            self.redibujar_ventana()

            if self.jugador.salud <= 0:
                self.game_over.play()
                self.ejecutar = False

    def mover_enemigos(self):
        if time.time() - self.ultimo_tiempo_enemigo > 3 and len(self.enemigos) < 5:
            enemigo = NaveEnemiga(random.randint(0, self.ANCHO - 50), 0, salud=50)
            self.enemigos.append(enemigo)
            self.ultimo_tiempo_enemigo = time.time()

        for enemigo in self.enemigos[:]:
            enemigo.mover()

            enemigo.mover_balas(5, self.jugador)
            if random.randint(0, 120) == 1:
                enemigo.disparar()
            if enemigo.salud <= 0:
                self.sonido_explosion.play()
                self.enemigos.remove(enemigo)

    def redibujar_ventana(self):
        self.VENTANA.blit(self.background, (0, 0))
        self.jugador.dibujar(self.VENTANA)
        for enemigo in self.enemigos:
            enemigo.dibujar(self.VENTANA)
        vida_texto = self.fuente.render(
            f"Vida: {self.jugador.salud}", 1, (255, 255, 255)
        )
        self.VENTANA.blit(vida_texto, (10, self.ALTO - 40))
        pygame.display.update()
