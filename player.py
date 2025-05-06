import pygame
from sprite import Sprite
from teclado import is_key_pressed
from camera import camera

class Player(Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        self.movement_speed = 4
    
    def update(self):
        if is_key_pressed(pygame.K_UP):
            self.y -= self.movement_speed
        
        if is_key_pressed(pygame.K_DOWN):
            self.y += self.movement_speed
        
        if is_key_pressed(pygame.K_LEFT):
            self.x -= self.movement_speed
        
        if is_key_pressed(pygame.K_RIGHT):
            self.x += self.movement_speed
        
        # Establecemos la posición de la cámara en la posición del jugador:
        camera.x = self.x - 1280/2
        camera.y = self.y - 720/2
