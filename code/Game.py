from Rendzu import Rendzu

from Creator import Creator

from FieldObject import FieldObject

from Bomb import Bomb

from Bomb_creator import Bomb_creator

from Fruit import Fruit

from Fruit_Creator import Fruit_creator

from Globals import field


rendzu = Rendzu()
bomb_creator = Bomb_creator()
fruit_creator = Fruit_creator()
fruit = Fruit()
fruits_list = []
bombs_list = []
while not rendzu.check() and not rendzu.run() and not rendzu.check_bomb():
    rendzu.run()
    fruits_list.append(fruit_creator.create_Fruit())
    bomb_creator.create_Bomb()
    fruits_list = fruit.remove(fruits_list)
    for i in range(len(fruits_list)):
            print(fruits_list[i].x, fruits_list[i].y)
