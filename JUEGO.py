import pygame
import teclado
from player import Player
from sprite import sprites
from map import TileKind, Map

# Inicializar pygame
pygame.init()

# Creación de la ventana del juego en la pantalla:
pygame.display.set_caption("ReciclaMONDA!")
ventana = pygame.display.set_mode((1280, 720))

# Establecemos el color de la ventana:
COLOR_CALLE = (128, 128, 128)
jugando = True

# Creamos el jugador:
player = Player("images/personaje1.png", 0, 0)

# Establecemos los tipos de texturas que va a tener el mapa:
tile_kinds = [
    TileKind("agua", "images/agua.png", False),
    TileKind("anden", "images/anden.png", False),
    TileKind("carretera", "images/carretera.png", False),
    TileKind("edificio", "images/edificio.png", True),
    TileKind("pasto", "images/pasto.png", False)
]

# Procedemos a crear el mapa:
map = Map("maps/start.map", tile_kinds, 32)

# Bucle que controla la ejecución del juego:
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        
        # Condicionales para checkear si una tecla es oprimida:
        elif event.type == pygame.KEYDOWN:
            teclado.keys_down.add(event.key)
        
        elif event.type == pygame.KEYUP:
            teclado.keys_down.remove(event.key)
    
    player.update()

    # Dibujamos en la ventana el código:
    ventana.fill(COLOR_CALLE)

    map.draw(ventana)

    for s in sprites:
        s.draw(ventana)

    pygame.display.flip()

    pygame.time.delay(17)

pygame.quit()
