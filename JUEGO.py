import pygame
import teclado
from player import Player
from sprite import Sprite, sprites_structures
from map import TileKind, Map
from camera import crear_ventana
from entity import Entity, active_objs
from physics import Body

# Inicializar pygame
pygame.init()

# Creación de la ventana del juego en la pantalla:
ventana = crear_ventana(1280, 720, "ReciclaMONDA!")

# Establecemos el color de la ventana:
COLOR_CALLE = (128, 128, 128)
jugando = True

# Establecemos los tipos de texturas que va a tener el mapa:
tile_kinds = [
    TileKind("agua", "images/agua.png", True),
    TileKind("anden", "images/anden.png", False),
    TileKind("carretera", "images/carretera.png", False),
    TileKind("lineacarretera", "images/lineascarretera.png", False),
    TileKind("lineacarretera2", "images/lineascarretera2.png", False),
    TileKind("pasto", "images/pasto.png", False),
    TileKind("senderopeatonal", "images/senderopeatonal.png", False),
    TileKind("senderopeatonal2", "images/senderopeatonal2.png", False),
    TileKind("arena", "images/arena.png", False),
    TileKind("senderoparque", "images/senderoparque.png", False)
]

# Procedemos a crear el mapa:
map = Map("maps/start.map", tile_kinds, 32)

# Agregamos los sprites del personaj
player_sprite = Sprite("images/Personaje/personaje1.png", False)
player_sprite.add()

#Creamos el sprite para el jugador
player = Entity(Player(player_sprite), player_sprite, Body(8, 24, 16, 5), x=32*32, y=32*32)

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
    
    for a in active_objs:
        a.update()

    # Dibujamos en la ventana el código:
    ventana.fill(COLOR_CALLE)

    map.draw(ventana)

    for s in [player_sprite]:
        s.draw(ventana)

    pygame.display.flip()

    pygame.time.delay(17)

pygame.quit()
