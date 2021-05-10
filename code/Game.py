from Field import Field

from FieldObject import FieldObject

from ElementMaker import ElementMaker

from FlyWeightFactory import FlyWeightFactory

import random
flyweight_factory = FlyWeightFactory()
element_maker = ElementMaker(flyweight_factory)
field = Field()
shared_states = ["W", "L", "B"]
while not field.check() and not field.run() and not field.check_bomb():
    field.run()
    unique_states = FieldObject.render(FieldObject)
    element = element_maker.make_element(unique_states, random.choice(shared_states))
    element_maker.put_element(element, field.field)
