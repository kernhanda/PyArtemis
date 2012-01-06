from PyArtemis.ComponentMapper import ComponentMapper
from PyArtemis.EntityProcessingSystem import EntityProcessingSystem
from Components.Health import Health
from math import log, cos

class SingleHEAVYHealthBarRenderSystem(EntityProcessingSystem):
    """description of class"""
    def __init__(self):
        super(SingleHEAVYHealthBarRenderSystem, self).__init__(Health)
        self.healthMapper = None
    def Initialize(self):
        self.healthMapper = ComponentMapper(Health, self.world)
    def Process(self, entity = None):
        if not entity:
            return super(SingleHEAVYHealthBarRenderSystem, self).Process()

        health = self.healthMapper.Get(entity)
        health.AddDamage(10)

        for i in range(1,1001):
            x = log(i) * cos(i)
            x = log(i) * cos(i)
            x = log(i) * cos(i)
            x = log(i) * cos(i)
