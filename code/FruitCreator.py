from Fruit import Fruit
from Creator import Creator


class FruitCreator(Creator):
    """
    Concrete creator
    """

    def create_obj(self):
        """
        :return: готовый объект фрукта
        """
        return Fruit()
