import pygame
from pygame import Rect
from camera import camera

sprites_structures = []
loaded = {}

class Sprite:
    def __init__(self, image, is_structure):
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        
        self.is_structure = is_structure


    def add_sprite(self, y):
        if self.is_structure == True:
            sprite = self, y
            sprites_structures.append(sprite)


    def delete(self):
        if self.is_structure == True: 
            sprites_structures.remove(self)

    
    def draw(self, ventana):
        if not hasattr(self, 'entity'):
            raise ValueError("Este sprite no está asociado a una entidad.")

        self_sprite = self.entity.get(Sprite)
        
        if self_sprite.image.get_height() <= 32:
            ventana.blit(self_sprite.image, (self.entity.x - camera.x, self.entity.y - camera.y))
        else:
            ventana.blit(self_sprite.image, (self.entity.x - camera.x, self.entity.y - self_sprite.image.get_height() - camera.y))
