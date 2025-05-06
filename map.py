import pygame
from camera import camera

class TileKind:
    def __init__(self, name, image, is_solid):
        self.name = name
        self.image = pygame.image.load(image)
        self.is_solid = is_solid

class Map:
    def __init__(self, archivo_mapa, tile_kinds, tile_size):
        self.tiles_kinds = tile_kinds

        # Cargamos el archivo del mapa:
        archivo = open(archivo_mapa, "r")
        data = archivo.read()
        archivo.close()

        # Establecemos las diferentes texturas del mapa cargado:
        self.tiles = []

        for line in data.split("\n"):
            row = []
            
            for tile_number in line:
                row.append(int(tile_number))
        
            self.tiles.append(row)
        
        # Determinamos el tamaño del mapa:
        self.tile_size = tile_size

    def draw(self, ventana):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size - camera.x, y * self.tile_size - camera.y)
                
                # Cargamos la imagen que va en esa determinada textura:
                image = self.tiles_kinds[tile].image
                ventana.blit(image, location)
