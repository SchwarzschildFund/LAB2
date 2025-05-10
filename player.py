import pygame
from sprite import Sprite
from teclado import is_key_pressed
from camera import camera
from entity import Entity, active_objs
from physics import Body

movement_speed = 6

class Player:
    def __init__(self, sprite):
        active_objs.append(self)
        self.sprite = sprite

        # Cargar sprites según dirección
        self.images_DOWN = [
            pygame.image.load("images/Personaje/personaje3.png").convert_alpha(),
            pygame.image.load("images/Personaje/personaje7.png").convert_alpha()  
        ]

        self.images_UP = [
            pygame.image.load("images/Personaje/personaje4.png").convert_alpha(),
            pygame.image.load("images/Personaje/personaje8.png").convert_alpha()  
        ]

        self.images_RIGHT = [
            pygame.image.load("images/Personaje/personaje1.png").convert_alpha()
        ]

        self.images_LEFT = [
            pygame.image.load("images/Personaje/personaje2.png").convert_alpha(),
            pygame.image.load("images/Personaje/personaje6.png").convert_alpha()  
        ]

        self.images_DOWNLEFT = [
            pygame.image.load("images/Personaje/personaje5.png").convert_alpha()
        ]

        self.animation_index = 0
        self.animation_timer = 0
        self.animation_speed = 10

        self.sprite.image = self.images_DOWN[self.animation_index]

    
    def update(self):
        previous_x = self.entity.x
        previous_y = self.entity.y
        body = self.entity.get(Body)

        # Movimiento vertical
        if is_key_pressed(pygame.K_UP):
            self.entity.y -= movement_speed

            self.animation_timer += 1
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.animation_index = (self.animation_index + 1) % len(self.images_UP)

            self.sprite.image = self.images_UP[self.animation_index]

        elif is_key_pressed(pygame.K_DOWN):
            self.entity.y += movement_speed
            
            self.animation_timer += 1
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.animation_index = (self.animation_index + 1) % len(self.images_DOWN)

            self.sprite.image = self.images_DOWN[self.animation_index]

        if not body.is_position_valid():
            self.entity.y = previous_y


        # Movimiento horizontal
        if is_key_pressed(pygame.K_LEFT):
            self.entity.x -= movement_speed
            
            self.animation_timer += 1
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.animation_index = (self.animation_index + 1) % len(self.images_LEFT)

            self.sprite.image = self.images_LEFT[self.animation_index]

        elif is_key_pressed(pygame.K_RIGHT):
            self.entity.x += movement_speed
            self.animation_index = 0
            self.sprite.image = self.images_RIGHT[self.animation_index]

        if not body.is_position_valid():
            self.entity.x = previous_x
        

        # Movimientos diagonales:
        if is_key_pressed(pygame.K_DOWN) and is_key_pressed(pygame.K_LEFT):
            self.animation_index = 0
            self.sprite.image = self.images_DOWNLEFT[self.animation_index]

        
        # Centrar la cámara en el jugador
        camera.x = self.entity.x - 1280 // 2
        camera.y = self.entity.y - 720 // 2
        
        from map import map
        # Limitamos la cámara vertical y horizontalmente:
        if camera.x < 0:
            camera.x = 0
        elif camera.x > map.width - 1280:
            camera.x = map.width - 1280

        if camera.y < 0:
            camera.y = 0
        elif camera.y > map.height - 720:
            camera.y = map.height - 720
