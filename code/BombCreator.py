from Bomb import Bomb
from Creator import Creator


class BombCreator(Creator):
    """
    Concrete creator
    """

    def create_obj(self):
        """
        :return: готовый объект бомба
        """
        return Bomb()
