from PyArtemis.ComponentMapper import ComponentMapper
from PyArtemis.EntityProcessingSystem import EntityProcessingSystem
from Components.Health import Health
from math import log, cos

class DummySystem(EntityProcessingSystem):
    """description of class"""
    def __init__(self):
        super(DummySystem, self).__init__(Health)
        self.healthMapper = None
    def Initialize(self):
        self.healthMapper = ComponentMapper(Health, self.world)
    def Process(self, entity = None):
        if not entity:
            return super(DummySystem, self).Process()
        for i in range(1,11):
            x = log(i) * cos(i)
