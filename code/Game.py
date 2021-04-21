from Rendzu import Rendzu

from Creator import Creator

from FieldObject import FieldObject

from Bomb import Bomb

from Bomb_creator import Bomb_creator

from Fruit import Fruit

from Fruit_Creator import Fruit_creator

from Globals import field

class Game():

    a = Rendzu()
    b = Bomb_creator()
    c = Fruit_creator()
    d = Fruit()
    fruits_list = []
    bombs_list = []
    while not a.check() and not a.run() and not a.check_bomb():
        a.run()
        fruits_list.append(c.create_Fruit())
        b.create_Bomb()
        fruits_list = d.remove(fruits_list)


b = Game()
