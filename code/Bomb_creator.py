from Creator import Creator

from FieldObject import FieldObject

from Bomb import Bomb

class Bomb_creator(Creator):
    def __init__(self):
        self.name = "B"
        super().__init__()

    def create_obj(self):
        bomb = Bomb.render(self)
        Creator.create_obj(self, bomb.x, bomb.y, bomb.name)
        return bomb  
