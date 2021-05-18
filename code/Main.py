from Field import Field
from FruitCreator import FruitCreator
from BombCreator import BombCreator


def main():
    field = Field()
    fruit_creator = FruitCreator()
    bomb_creator = BombCreator()
    while not field.check() and not field.run() and not field.check_bomb():
        field.run()
        fruit = fruit_creator.create_obj()
        fruit.remove(field.field, field.field_objects_fruits)
        bomb = bomb_creator.create_obj()
        bomb.remove(field.field, field.field_objects_bombs)
        bomb.render(field.field)
        field.add_object_bomb(bomb)
        fruit.render(field.field)
        field.add_object_fruit(fruit)


main()
