from Creator import Creator

from Fruit import Fruit

from FieldObject import FieldObject

class Fruit_creator(Creator):
    def __init__(self):
        self.fruit_type = ''
        super().__init__()

    def create_Fruit(self):

        obj = FieldObject()
        name, x, y = obj.create("fruit")

        fruit = Fruit()
        fruit.name = name
        fruit.x = x
        fruit.y = y
        Creator.create_obj(self, x, y, name)
        return fruit

