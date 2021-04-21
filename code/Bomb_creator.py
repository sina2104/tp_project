from Creator import Creator

from FieldObject import FieldObject

from Bomb import Bomb

class Bomb_creator(Creator):
    def __init__(self):
        super().__init__()

    def create_Bomb(self):
        obj = FieldObject()
        name, x, y = obj.create('B')
        bomb = Bomb()
        bomb.name = 'B'
        bomb.x = x
        bomb.y = y
        Creator.create_obj(self, x, y, name)
        return bomb
