import random
from FieldObject import FieldObject


class Fruit(FieldObject):
    """
    Concrete product
    В нем определяем методы,
    описанные в FieldObject
    """

    def __init__(self):
        self.list_of_fruits = ["W", "L"]
        self.name = random.choice(self.list_of_fruits)  # рисунок на поле

        # координаты на поле:
        self.x = random.randint(-1, 14)
        self.y = random.randint(-1, 14)

    def render(self, field):
        """

        :param field: поле игры
        :return: ничего
        """
        field[self.x][self.y] = self.name
        return None

    def remove(self, field, field_objects_fruits):
        """
        Реализуйте тут свой remove
        """
        import random
        for i in range(len(field_objects_fruits)):
            current_fruit = field_objects_fruits[i].name
            random_number = random.random()
            if random_number > 0.4:
                if current_fruit == 'W':
                    if random_number > 0.7:
                        field[field_objects_fruits[i].x][field_objects_fruits[i].y] = 0
                        field_objects_fruits.pop(i)
                else:
                    field[field_objects_fruits[i].x][field_objects_fruits[i].y] = 0
                    field_objects_fruits.pop(i)
            return 0
