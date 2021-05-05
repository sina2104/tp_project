class Field:
    def __init__(self):
        self.field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for x in range(15)]
        # здесь, например, можно задать список объектов, которые есть на поле
        self.field_objects_fruits = []

        self.field_objects_bombs = []

        self.last_point = (0, 0)

        self.move = 0

        self.win_strike_lenth = 5

    def is_empty(self, x, y):
        """
        Проверяет, лежит ли что-нибудь в ячейке x, y
        :return:
        """
        if isinstance(self.field[x][y], int) and self.field[x][y] != 0:
            return False
        else:
            return True

    def add_object_fruit(self, obj):
        """
        :param obj: FieldObject - фрукт или бомба
        :return: ничего
        """
        self.field_objects_fruits.append(obj)

    def add_object_bomb(self, obj):
        """
        :param obj: FieldObject - фрукт или бомба
        :return: ничего
        """
        self.field_objects_bombs.append(obj)

    def render_all(self):
        """
        Отрисовывает все объекты на поле
        :return: ничего
        """
        for obj in self.field_objects_fruits:
            obj.render(self.field)

    def try_remove(self, field, x, y):
        """
        Можно удалять объекты с поля или еще что-нибудь, как хотите
        :return:
        """
        field[x][y] = 0

    def run(self):

        for i in range(15):

            print(self.field[i])

        if not self.check() and not self.check_bomb():
            print(f"Player {self.move % 2 + 1}, enter coodinates of your point")
            x = int(input())
            y = int(input())
            self.last_point = (x, y)

            if self.check_bomb():
                return True
            if not self.check_fruit():
                your_move_again = 0
            else:
                your_move_again = 1
            self.field[self.last_point[0]][self.last_point[1]] = self.move % 2 + 1
            self.move = self.move + 1 - your_move_again

    def check(self):
        field_len = 14

        minimum = min(self.last_point)

        start = (self.last_point[0] - minimum, self.last_point[1] - minimum)

        diagonal_arr1 = [self.field[start[0] + i][start[1] + i] for i in range(15 - max(start))]
        # diagonal_arr1 - массив элементов в поле, которые стоят по диагонали
        # (по направлению сверху слева - снизу справа), переменная создается для
        # проверки не закончилась ли игра. Если в этом массиве 5 единиц или 5 двоек подряд -
        # игра закончилась
        if self.last_point[0] + self.last_point[1] < field_len:
            start = (0, self.last_point[0] + self.last_point[1])

        if self.last_point[0] + self.last_point[1] > field_len:
            start = ((self.last_point[0] + self.last_point[1]) % field_len, field_len)

        if self.last_point[0] + self.last_point[1] == field_len:
            start = (0, field_len)

        diagonal_arr2 = [self.field[start[0] + i][start[1] - i] for i in range(start[1] - start[0] + 1)]
        # аналогично diagonal_arr1, только направление сверху справа - снизу слева

        vertical_arr = [self.field[self.last_point[0]][i] for i in range(field_len + 1)]
        # аналогично diagonal_arr1, только направление по вертикали

        horizontal_arr = [self.field[i][self.last_point[1]] for i in range(field_len + 1)]
        # аналогично diagonal_arr1, только направление по горизонтали

        all_arr = diagonal_arr1 + [0] + diagonal_arr2 + [0] + vertical_arr + [0] + horizontal_arr
        # все массивы вместе, в которых ищем [1, 1, 1, 1, 1] или [2, 2, 2, 2, 2]. Если находим - игра заканчивается

        for i in range(len(all_arr) - self.win_strike_lenth):

            if all_arr[i: i + self.win_strike_lenth] == [1, 1, 1, 1, 1] or \
                    all_arr[i: i + self.win_strike_lenth] == [2, 2, 2, 2, 2]:
                return True

        return False

    def check_bomb(self):

        if self.field[self.last_point[0]][self.last_point[1]] == 'B':

            print("Fail")

            return True

        else:

            return False

    def check_fruit(self):
        if self.field[self.last_point[0]][self.last_point[1]] == 'W' or \
           self.field[self.last_point[0]][self.last_point[1]] == 'L':
            import random
            your_turn_again = random.random()
            if your_turn_again > 0.5:
                print("your turn again!")
                return True
        return False
