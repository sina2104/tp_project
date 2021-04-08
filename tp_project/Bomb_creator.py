from Creator import Creator, field

class Bomb_creator(Creator):

    def __init__(self):

        self.name = ''

        self.x = 0

        self.y = 0

        super().__init__()



    def create_Bomb(self):

        import random

        name = random.random()

        if name > 0.5:

            name = "B"

            x = random.randint(-1, 14)

            y = random.randint(-1, 14)

            Creator.create_obj(self, x, y, name)



