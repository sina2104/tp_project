from Fruit_creator import Fruit_creator, field


class Remove_fruit(Fruit_creator):

    def __init__(self):

        super().__init__()



    def remove(self):

        import random



        for i in range(len(self.fruits_list)):

            current_fruit = field[self.fruits_list[i][0]][self.fruits_list[i][1]]

            random_number = random.random()

            if random_number > 0.4:

                if current_fruit == 'W':

                    if random_number > 0.7:

                        field[self.fruits_list[i][0]][self.fruits_list[i][1]] = 0

                        self.fruits_list.pop(i)

                else:

                    field[self.fruits_list[i][0]][self.fruits_list[i][1]] = 0

                    self.fruits_list.pop(i)

                if current_fruit == 1 or current_fruit == 2:

                    self.fruits_list.pop(i)

            return 0


