from Creator import Creator, field

from FieldObject import FieldObject


class Fruit_creator(Creator):

    def __init__(self):

        self.name = ''

        self.x = 0

        self.y = 0

        self.fruits_list = []

        super().__init__()



    def create_Fruit(self):

        import random

        name = random.random()

        if name > 0.1:

            if name > 0.4:

                name = "W"

            else:

                name = "L"

            x = random.randint(-1, 14)

            y = random.randint(-1, 14)

            self.fruits_list.append([x, y])

            Creator.create_obj(self, x, y, name)
