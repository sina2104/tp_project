import random

class FieldObject:
    def __init__(self):
        self.x = 0
        self.y = 0

    def create(self):
        self.x = random.randint(-1, 14)
        self.y = random.randint(-1, 14)
        return [self.x, self.y]




