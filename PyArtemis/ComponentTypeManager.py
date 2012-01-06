from PyArtemis.Component import Component
from PyArtemis.ComponentType import ComponentType
from PyArtemis.Utils import GetClass

class ComponentTypeManager(object):
    _componentTypes = {}

    @classmethod
    def GetTypeFor(cls, component):
        receivedType = GetClass(component)
        if not issubclass(receivedType, Component):
            raise TypeError
        t = cls._componentTypes.get(receivedType)
        if not t:
            t = ComponentType()
            cls._componentTypes[receivedType] = t
        return t
    
    @classmethod
    def GetBit(cls, component):
        return cls.GetTypeFor(component).GetBit()

    @classmethod
    def GetId(cls, component):
        return cls.GetTypeFor(component).GetId()
