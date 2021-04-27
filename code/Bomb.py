from FieldObject import FieldObject

class Bomb(FieldObject):
    def __init__(self):
        self.name = 'B'
        self.x = 0
        self.y = 0
        super().__init__()


    def render(self):
        
        obj = FieldObject()
        self.name, self.x, self.y = obj.create(self.name)
        
        
        return self
