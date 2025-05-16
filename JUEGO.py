import pygame
import teclado
from basuras import Basura, Trashbin, crear_basuras
from player import Player
from sprite import Sprite, sprites_structures
from map import TileKind, Map, pasto_tiles
from camera import crear_ventana
from entity import Entity, active_objs
from physics import Body


# Inicializar pygame
pygame.init()
pygame.font.init()
fuente = pygame.font.SysFont("Arial", 24)

# Creación de la ventana del juego en la pantalla:
ventana = crear_ventana(1280, 720, "ReciclaMONDA!")

# Establecemos el color de la ventana:
COLOR_VERDE = (110, 160, 50)
jugando = True

# Establecemos los tipos de texturas que va a tener el mapa:
tile_kinds = [
    TileKind("agua", "images/mapa/agua.png", True),
    TileKind("anden", "images/mapa/anden.png", False),
    TileKind("carretera", "images/mapa/carretera.png", False),
    TileKind("lineacarretera", "images/mapa/lineascarretera.png", False),
    TileKind("lineacarretera2", "images/mapa/lineascarretera2.png", False),
    TileKind("pasto", "images/mapa/pasto.png", False),
    TileKind("senderopeatonal", "images/mapa/senderopeatonal.png", False),
    TileKind("senderopeatonal2", "images/mapa/senderopeatonal2.png", False),
    TileKind("arena", "images/mapa/arena.png", False),
    TileKind("senderoparque", "images/mapa/senderoparque.png", False),
    TileKind("pasto2", "images/mapa/pasto2.png", False)
]


# Procedemos a crear el mapa:
map = Map("maps/start.map", tile_kinds, 32)
map.selection_tiles()

# Agregamos los sprites del personaje:
player_sprite = Sprite("images/Personaje/personaje1.png", False)

#Creamos el sprite para el jugador
player = Entity(Player(player_sprite), player_sprite, Body(8, 24, 16, 5), x=32*7, y=32*6 + player_sprite.image.get_height())


# Agregamos los sprites de los árboles:
for pos in pasto_tiles:
    structure_sprite = Sprite("images/Structures/tree.png", True)
    structure = Entity(structure_sprite, Body(8, -35, 24, 35), x=pos[0], y=pos[1] + 15)
    y = structure.y + structure_sprite.image.get_height()
    structure_sprite.add_sprite(y)

# Agregamos los sprites de las canecas:
bin_sprite_org = Sprite("images/Structures/Organico.png", True)
bin_organica = Entity(bin_sprite_org, Body(6, 22, 20, 10), x=32*19, y=32*3)
bin_sprite_org.add_sprite(bin_organica.y)

bin_sprite_inorg = Sprite("images/Structures/Inorganico.png", True)
bin_inorganica = Entity(bin_sprite_inorg, Body(6, 22, 18, 9),x=32*38, y=32*32)
bin_sprite_inorg.add_sprite(bin_inorganica.y)

bin_sprite_reciclable = Sprite("images/Structures/Reciclable.png", True)
bin_reciclable = Entity(bin_sprite_reciclable, Body(4, 22, 20, 10),x=32*57, y=32*20)
bin_sprite_reciclable.add_sprite(bin_reciclable.y)

edificio_sprite = Sprite("images/Structures/edificio.png", True)
edificio = Entity(edificio_sprite, Body(0, 52, 32, 20), x=32*48, y=32*2)
edificio_sprite.add_sprite(edificio.y)

for s in sprites_structures:
    sprites_structures.sort(key=lambda s: s[1])


""""
# Creamos el sprite para la basura y basureros
trash_sprite_org = ("", False)
trash_sprite_inorg = ("", False)
trash_sprite_reciclable = ("", False)

#Creamos las entidades de las basuras:

Entity(Basura(trash_sprite_org,"Organica"), trash_sprite_org, Body(),x=??, y=??)
Entity(Basura(trash_sprite_inorg,"Inorganica"),trash_sprite_inorg,body(),x=??, y=??)
Entity(Basura(trash_sprite_reciclable,"Reciclable"),trash_sprite_reciclable,body(),x=??, y=??)

basuras = crear_basuras(0,map.width - 32, map.height - 32 , cantidad=15)
"""

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
    ventana.fill(COLOR_VERDE)

    map.draw(ventana)

    player_component = player.get(Player)

    dibujables = []

    # Añadir estructuras
    for s in sprites_structures:
        sprite = s[0]
        y = s[1]
        y_draw = y + sprite.image.get_height()

        dibujables.append(("structure", sprite, y_draw))


    # Añadir jugador solo una vez (ya tiene el sprite correcto)
    player_y_draw = player.y + player_sprite.image.get_height()
    dibujables.append(("player", player_component, player_y_draw))

    # Ordenar por eje Y
    dibujables.sort(key=lambda x: x[2])

    # Dibujar todo en orden
    for tipo, obj, _ in dibujables:
        if tipo == "structure":
            obj.draw(ventana)
        elif tipo == "player":
            obj.draw_player(ventana)

 
    if player_component:
        texto_inventario = f"INVENTARIO: {player_component.inventario if player_component.inventario else "Nada"}"
        texto_entregado = f"BASURA RECOGIDA: {player_component.entregado}"

        texto1 = fuente.render(texto_inventario, True, (0, 0, 0))
        texto2 = fuente.render(texto_entregado, True, (0, 0, 0))
        ventana.blit(texto1, (10, 10))
        ventana.blit(texto2, (10, 40))
  

    pygame.display.flip()

    pygame.time.delay(17)

pygame.quit()
