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


    def add(self):
        if self.is_structure == True:
            sprites_structures.append(self)


    def delete(self):
        if self.is_structure == True: 
            sprites_structures.remove(self)

    
    def draw(self, ventana):
        if self.entity is None:
            return

        ventana.blit(self.image, (self.entity.x - camera.x, self.entity.y - camera.y))
