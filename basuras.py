from sprite import Sprite
from entity import active_objs
from physics import Body
from entity import Entity
import random 
imagenes_basura =   {
    "Inorganica": "",
    "Organica": "",
    "Reciclable": ""
}


class Basura:
    def __init__(self, sprite,trash_type):
        self.sprite = sprite
        self.trash_type = trash_type
        active_objs.append(self)

        
    def update(self):
        from player import Player
        player = self.entity.get(Player)
        if player:
            return
        
        from physics import Body
        body = self.entity.get(Body)
        player_entity = next((e for e in active_objs if e.has(Player)), None)

        if player_entity:   
            player_body = player_entity.get(Body)
            if body.is_colliding_with(player_body):
                player = player_entity.get(Player)
                if player.held_trash is None:
                    player.held_trash = self.trash_type
                    active_objs.remove(self.entity)

class Trashbin: 
    def __init__(self, sprite, trash_type):
        self.sprite = sprite
        self.trash_type = trash_type
        active_objs.append(self)


    def update(self):
        from entity import Entity
        from player import Player
        from physics import Body

        player_entity = next((e for e in active_objs if e.has(Player)), None)

        if player_entity:
            player = player_entity.get(Player)
            player_body = player_entity.get(Body)
            bin_body = self.entity.get(Body)

            if bin_body.is_colliding_with(player_body):
                if player.held_trash == self.trash_type:
                    player.delivered_trash[self.trash_type] += 1
                    print(f"Entregaste basura {self.trash_type}")
                    player.held_trash = None


def crear_basuras(x_min,x_max,y_min,y_max, cantidad = 10):

    tipos = list(imagenes_basura.keys())
    basuras = []
    for _ in range(cantidad):
       tipo = random.choice(tipos)
       sprite = Sprite(imagenes_basura[tipo],False)
       x = random.randint(x_min, x_max)
       y = random.randint(y_min, y_max)
       entidad = Entity(Basura(sprite,tipo),sprite,Body(0,0,32,32),x=x,y=y)
       basuras.append(entidad)
    return basuras
