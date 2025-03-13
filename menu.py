import pygame
import sys


class Menu:
    def __init__(self, ventana):
        self.background = pygame.image.load("./assets/menu.jpg")
        self.ventana = ventana
        self.ANCHO, self.ALTO = ventana.get_size()
        self.fuente_titulo = pygame.font.SysFont("comicsans", 60)
        self.fuente_boton = pygame.font.SysFont("comicsans", 40)
        self.titulo = self.fuente_titulo.render(
            "BATALLA ESPACIAL", True, (255, 255, 255)
        )
        self.boton_jugar = pygame.Rect(
            self.ANCHO // 2 - 100, self.ALTO // 2 - 50, 200, 60
        )
        self.boton_cerrar = pygame.Rect(
            self.ANCHO // 2 - 100, self.ALTO // 2 + 20, 200, 60
        )

    def mostrar_menu(self):
        ejecutando = True
        while ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_jugar.collidepoint(evento.pos):
                        ejecutando = False
                    if self.boton_cerrar.collidepoint(evento.pos):
                        pygame.quit()
                        sys.exit()

            self.ventana.blit(self.background, (0, 0))
            self.ventana.blit(
                self.titulo, (self.ANCHO // 2 - self.titulo.get_width() // 2, 100)
            )
            pygame.draw.rect(self.ventana, (255, 20, 30), self.boton_jugar)
            pygame.draw.rect(self.ventana, (255, 20, 30), self.boton_cerrar)
            texto_jugar = self.fuente_boton.render("JUGAR", True, (255, 255, 255))
            texto_cerrar = self.fuente_boton.render("CERRAR", True, (255, 255, 255))
            self.ventana.blit(
                texto_jugar,
                (
                    self.boton_jugar.x
                    + self.boton_jugar.width // 2
                    - texto_jugar.get_width() // 2,
                    self.boton_jugar.y + 10,
                ),
            )
            self.ventana.blit(
                texto_cerrar,
                (
                    self.boton_cerrar.x
                    + self.boton_cerrar.width // 2
                    - texto_cerrar.get_width() // 2,
                    self.boton_cerrar.y + 10,
                ),
            )
            pygame.display.update()
