from ElementFlyWeight import ElementFlyWeight


class FlyWeightFactory:

    def __init__(self):
        self.flyweights = []

    def get_flyweight(self, shared_state) -> ElementFlyWeight:

        flyweights = list(filter(lambda x: x.shared_state ==
                                           shared_state, self.flyweights))
        if flyweights:
            return flyweights[0]
        else:
            flyweight = ElementFlyWeight(shared_state)
            self.flyweights.append(flyweight)
            return flyweight

    @property
    def total(self):
        return len(self.flyweights)

