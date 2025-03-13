import pygame
from juego import Juego
from menu import Menu

def main():
    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    menu = Menu(ventana)
    
    while True:
        menu.mostrar_menu()
        juego = Juego()
        juego.bucle_principal()
    

if __name__ == "__main__":
    main()
