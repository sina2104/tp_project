from Rendzu import Rendzu

from Creator import Creator

from FieldObject import FieldObject

from ElementMaker import ElementMaker

from FlyWeightFactory import FlyWeightFactory

from Globals import field

import random
flyweight_factory = FlyWeightFactory()
element_maker = ElementMaker(flyweight_factory)
rendzu = Rendzu()
shared_states = ['W', 'L', 'B']
while not rendzu.check() and not rendzu.run() and not rendzu.check_bomb():
    rendzu.run()
    unique_states = FieldObject.create(FieldObject)
    element = element_maker.make_element(unique_states, random.choice(shared_states))
    Creator.create_obj(Creator, element.unique_state[0], element.unique_state[1], element.flyweight)