import pygame
from camera import camera
from math import ceil

map = None
pasto_tiles = []

class TileKind:
    def __init__(self, name, image, is_solid):
        self.name = name
        self.image = pygame.image.load(image)
        self.is_solid = is_solid

class Map:
    def __init__(self, archivo_mapa, tile_kinds, tile_size):
        global map
        map = self
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
        
        # Determinamos el tamaño de cada baldosa:
        self.tile_size = tile_size

        #Calculamos los límites del mapa:
        self.width = len(self.tiles[0]) * tile_size
        self.height = len(self.tiles) * tile_size
    
    def is_point_solid(self, x, y):
        x_tile = int(x / self.tile_size)
        y_tile = int(y / self.tile_size)

        # Verificamos que la baldosa esté adentro del mapa:
        if x_tile < 0 or y_tile < 0 or y_tile >= len(self.tiles) or x_tile >= len(self.tiles[0]):
            return False
        
        # Buscamos la baldosa en la matriz de baldosas que conforma el mapa y verificamos si es sólida o no:
        tile = self.tiles[y_tile][x_tile]
        return self.tiles_kinds[tile].is_solid
    
    
    def is_rect_solid(self, x, y, width, height):
        # Verificamos el tamaño del rectángulo y lo dividimos por el tamaño de cada pixel:
        x_checks = int(ceil(width / self.tile_size))
        y_checks = int(ceil(height / self.tile_size))

        for dim_y in range(y_checks):
            for dim_x in range(x_checks):
                check_x = x + dim_x * self.tile_size
                check_y = y + dim_y * self.tile_size

                # Usamos la función para verificar si la baldosa es sólida:
                if self.is_point_solid(check_x, check_y):
                    return True
            
        # Ahora verificamos las baldosas de las esquinas:
        if self.is_point_solid(x + width, y):
            return True
        if self.is_point_solid(x, y + height):
            return True
        if self.is_point_solid(x + width, y + height):
            return True
        return False


    def draw(self, ventana):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                if tile == 5:
                    x_pasto = x * self.tile_size
                    y_pasto = y * self.tile_size
                    pasto_tiles.append((x_pasto, y_pasto))

                location = (x * self.tile_size - camera.x, y * self.tile_size - camera.y)
                
                # Cargamos la imagen que va en esa determinada textura:
                image = self.tiles_kinds[tile].image
                ventana.blit(image, location)
