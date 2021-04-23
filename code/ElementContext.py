from ElementFlyWeight import ElementFlyWeight

class ElementContext:

    def __init__(self, unique_state, flyweight: ElementFlyWeight):
        self.unique_state = unique_state
        self.flyweight = flyweight

    def __repr__(self):
        return f"уникальное состояние: {self.unique_state} \n" \
               f"разделяемое состояние: {self.flyweight}"