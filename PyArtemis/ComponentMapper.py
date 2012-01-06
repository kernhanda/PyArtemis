from PyArtemis.Component import Component
from PyArtemis.ComponentTypeManager import ComponentTypeManager
from PyArtemis.Utils import GetClass

class ComponentMapper(object):
    def __init__(self, component, world = None):
        self.typeOfComponent = GetClass(component)
        if not issubclass(self.typeOfComponent, Component):
            raise TypeError
        if world:
            self.em = world.GetEntityManager()
            self.componentType = ComponentTypeManager.GetTypeFor(self.typeOfComponent)
        else:
            self.em = self.type = None
    def SetEntityManager(self, em):
        self.em = em
    def Get(self, entity):
        return self.em.GetComponent(entity, self.componentType)