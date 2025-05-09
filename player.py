import pygame
from sprite import Sprite
from teclado import is_key_pressed
from camera import camera
from entity import Entity, active_objs
from physics import Body

movement_speed = 6

class Player:
    def __init__(self):
        active_objs.append(self)
    
    def update(self):
        previous_x = self.entity.x
        previous_y = self.entity.y
        body = self.entity.get(Body)

        # Movimientos arriba y abajo:
        if is_key_pressed(pygame.K_UP):
            self.entity.y -= movement_speed
        
        if is_key_pressed(pygame.K_DOWN):
            self.entity.y += movement_speed

        if not body.is_position_valid():
            self.entity.y = previous_y
        
        # Movimientos izquierda y derecha:
        if is_key_pressed(pygame.K_LEFT):
            self.entity.x -= movement_speed
        
        if is_key_pressed(pygame.K_RIGHT):
            self.entity.x += movement_speed
        
        if not body.is_position_valid():
            self.entity.x = previous_x
        
        # Establecemos la posición de la cámara en la posición del jugador:
        camera.x = self.entity.x - 1280/2
        camera.y = self.entity.y - 720/2
