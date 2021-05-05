from abc import ABC, abstractmethod
from FieldObject import FieldObject


class Creator(ABC):
    """
    Creator, abstract class
    """

    @abstractmethod
    def create_obj(self) -> FieldObject:
        """
        Тот самый фабричный метод,
        который будет переопределен
        у каждого конкретного Creator
        :return: готовый Product
        """
        raise NotImplementedError
