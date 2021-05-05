import random
from FieldObject import FieldObject


class Bomb(FieldObject):
    """
    Concrete product
    В нем определяем методы,
    описанные в FieldObject
    """

    def __init__(self):
        self.name = 'B'  # рисунок на поле

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

    def remove(self, field, field_objects_bombs):
        """
        Удаляет объект с поля.
        :return: ничего
        """
        import random
        for i in range(len(field_objects_bombs)):
            random_number = random.random()
            if random_number > 0.4:
                field[field_objects_bombs[i].x][field_objects_bombs[i].y] = 0
                field_objects_bombs.pop(i)
            return 0
