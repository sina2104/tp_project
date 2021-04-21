import random

class FieldObject():
    def __init__(self):
        self.name = ''
        self.x = 0
        self.y = 0
        self.list_of_fruits = ['L', 'W']

    def create(self, name):
        
        if name == "fruit":
            self.name = random.choice(self.list_of_fruits)
        else:
            self.name = name
        self.x = random.randint(-1, 14)
        self.y = random.randint(-1, 14)
        return self.name, self.x, self.y


