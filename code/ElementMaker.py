from FlyWeightFactory import FlyWeightFactory
from ElementContext import ElementContext


class ElementMaker:

    def __init__(self, flyweight_factory: FlyWeightFactory):
        self.flyweight_factory = flyweight_factory
        self.contexts = []

    def make_element(self, unique_state, shared_state) -> ElementContext:
        flyweight = self.flyweight_factory.get_flyweight(shared_state)
        context = ElementContext(unique_state, flyweight)
        self.contexts.append(context)

        return context

