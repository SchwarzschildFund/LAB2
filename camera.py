import pygame

camera = pygame.Rect(0, 0, 0, 0)

def crear_ventana(ancho, alto, titulo):
    pygame.display.set_caption(titulo)

    ventana = pygame.display.set_mode((ancho, alto))

    return ventana