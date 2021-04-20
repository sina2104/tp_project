from FieldObject import FieldObject
from Globals import field


class Fruit(FieldObject):
    def __init__(self):
        self.name = ''
        self.x = 0
        self.y = 0
        super().__init__()

    def remove(self, fruits_list):
        import random

        for i in range(len(fruits_list)):
            self.x = fruits_list[i].x
            self.y = fruits_list[i].y
            self.name = fruits_list[i].name
            random_number = random.random()
            if random_number > 0.3:
                if self.name == 'W':
                    if random_number > 0.6:
                        field[self.x][self.y] = 0
                        fruits_list.pop(i)
                        return fruits_list
                else:
                    field[self.x][self.y] = 0
                    fruits_list.pop(i)
                    return fruits_list
                if field[self.x][self.y] == 1 or field[self.x][self.y] == 2:
                    fruits_list.pop(i)
                    return fruits_list
        return fruits_list


