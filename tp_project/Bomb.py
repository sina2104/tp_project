from FieldObject import FieldObject


class Bomb(FieldObject):
    def __init__(self):
        self.name = ''
        self.x = 0
        self.y = 0
        super().__init__()
