from bala import Bala
import pygame

nave_img = pygame.image.load("./assets/spaceship.png")

class Nave:
    def __init__(self, x, y, salud=100):
        self.x = x
        self.y = y
        self.salud = salud
        self.img_nave = nave_img
        self.mascara = pygame.mask.from_surface(self.img_nave)
        self.balas = []
        self.contador_recarga = 0

    def dibujar(self, ventana):
        ventana.blit(self.img_nave, (self.x, self.y))
        for bala in self.balas:
            bala.dibujar(ventana)

    def mover_balas(self, vel, objs):
        self.recargar()
        for bala in self.balas:
            bala.mover(vel)
            if bala.fuera_de_pantalla():
                self.balas.remove(bala)
            else:
                if isinstance(objs, list):
                    for obj in objs:
                        if bala.colision(obj):
                            obj.salud -= 10
                            self.balas.remove(bala)
                            break
                else:
                    if bala.colision(objs):
                        objs.salud -= 10
                        self.balas.remove(bala)

    def recargar(self):
        if self.contador_recarga >= 20:
            self.contador_recarga = 0
        elif self.contador_recarga > 0:
            self.contador_recarga += 1

    def disparar(self):
        if self.contador_recarga == 0:
            bala = Bala(self.x, self.y)
            self.balas.append(bala)
            self.contador_recarga = 1
