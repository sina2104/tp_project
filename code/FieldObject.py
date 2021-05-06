from abc import ABC, abstractmethod


class FieldObject(ABC):
    """
    Product, abstract class
    Это интерфейс работы со всеми FieldObject.

    Объекты этого класса не создаются,
    но мы гарантируем, что со всеми его детьми
    можно работать через методы, которые мы тут пропишем
    """

    @abstractmethod
    def render(self, field):
        """
        Может быть переопределен у ребенка.
        Отрисовывает объект на поле.
        :return: ничего
        """
        pass

    @abstractmethod
    def remove(self, field, field_objects_fruits):
        """
        Удаляет объект с поля.
        :return: ничего
        """
        pass
