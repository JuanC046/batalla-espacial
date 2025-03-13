import pygame

bala_img = pygame.image.load("./assets/bullet.png")

class Bala:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = bala_img
        self.mascara = pygame.mask.from_surface(self.img)

    def dibujar(self, ventana):
        ventana.blit(self.img, (self.x, self.y))

    def mover(self, vel):
        self.y += vel

    def fuera_de_pantalla(self):
        return not (0 <= self.y <= 600)

    def colision(self, obj):
        return colisionar(self, obj)

def colisionar(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mascara.overlap(obj2.mascara, (offset_x, offset_y)) is not None
