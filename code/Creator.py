from Rendzu import Rendzu

from Globals import field

class Creator(Rendzu):

    def __init__(self):
        self.x = 0
        self.y = 0
        super().__init__()

    def check(self, x, y):
        if isinstance(field[x][y], int) and field[x][y] != 0:
            return False
        else:
            return True

    def create_obj(self, x, y, *args):
        if self.check(x, y):
            field[x][y] = args[0]


