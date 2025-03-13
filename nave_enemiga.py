from nave import Nave
import random
import time
import pygame

nave_img_roja = pygame.transform.rotate(pygame.image.load("./assets/spaceship_red.png"), 180)

class NaveEnemiga(Nave):
    def __init__(self, x, y, salud=100):
        super().__init__(x, y, salud)
        self.img_nave = nave_img_roja
        self.mascara = pygame.mask.from_surface(self.img_nave)
        self.velocidad_x = 1
        self.velocidad_y = 1
        self.cambio_direccion_tiempo = time.time()
        self.mover_en_x = True

    def mover(self):
        # Cambiar dirección de movimiento ocasionalmente
        if time.time() - self.cambio_direccion_tiempo > 3:
            self.velocidad_x *= random.choice([-1, 1])
            self.velocidad_y *= random.choice([-1, 1])
            self.mover_en_x = not self.mover_en_x
            self.cambio_direccion_tiempo = time.time()

        if self.mover_en_x:
            self.x += self.velocidad_x
        else:
            self.y += self.velocidad_y

        if self.y < 0:
            self.y = 0
            self.velocidad_y *= -1
        if self.y + self.img_nave.get_height() > 300:  # Limitar movimiento vertical
            self.y = 300 - self.img_nave.get_height()
            self.velocidad_y *= -1
        if self.x < 0:
            self.x = 0
            self.velocidad_x *= -1
        if self.x + self.img_nave.get_width() > 800:  # Limitar movimiento horizontal
            self.x = 800 - self.img_nave.get_width()
            self.velocidad_x *= -1
