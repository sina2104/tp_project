from Creator import Creator

from Fruit import Fruit

from FieldObject import FieldObject

class Fruit_creator(Creator):
    def __init__(self):
        self.name = "fruit"
        self.fruit_type = ''
        super().__init__()

    def create_obj(self):

        fruit = Fruit.render(self)
        Creator.create_obj(self, fruit.x, fruit.y, fruit.name)
        return fruit

