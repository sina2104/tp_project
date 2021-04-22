from FieldObject import FieldObject

class Bomb(FieldObject):
    def __init__(self):
        self.name = ''
        self.x = 0
        self.y = 0
        super().__init__()

    def render(self):
        obj = FieldObject()
        name, x, y = obj.create('B')
    
        self.name = 'B'
        self.x = x
        self.y = y
        return self
