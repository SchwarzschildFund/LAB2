import pygame
from pygame import Rect
from camera import camera

sprites = []
loaded = {}

class Sprite:
    def __init__(self, image):
        if image in loaded:
            self.image = loaded[image]
        
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image

        sprites.append(self)

    def delete(self):
        sprites.remove(self)
    
    def draw(self, ventana):
        ventana.blit(self.image, (self.entity.x - camera.x, self.entity.y - camera.y))
