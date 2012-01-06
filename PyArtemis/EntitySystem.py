from PyArtemis.ComponentTypeManager import ComponentTypeManager

class EntitySystem(object):
    def __init__(self, *types):
        self.systemBit = self.typeFlags = 0
        self.enabled = True
        self.world = None
        self.actives = {}
        for t in types:
            ct = ComponentTypeManager.GetTypeFor(t)
            self.typeFlags |= ct.GetBit()
    def SetSystemBit(self, bit):
        self.systemBit = bit
    def Begin(self):
        pass
    def Process(self):
        if self.CheckProcessing():
            self.Begin()
            self.ProcessEntities(self.actives)
            self.End()
    def End(self):
        pass
    def ProcessEntities(self, entities):
        raise NotImplementedError        
    def CheckProcessing(self):
        return self.enabled
    def Initialize(self):
        pass
    def Added(self, entity):
        pass
    def Removed(self, entity):
        pass
    def Change(self, entity):
        contains = (self.systemBit & entity.GetSystemBits()) == self.systemBit
        interest = (self.typeFlags & entity.GetTypeBits()) == self.typeFlags

        if interest and not contains and self.typeFlags > 0:
            self.actives[entity.GetId()] = entity
            entity.AddSystemBit(self.systemBit)
            self.Added(entity)
        elif not interest and contains and self.typeFlags > 0:
            self.Remove(entity)
    def Remove(self, entity):
        del self.actives[entity.GetId()]
        entity.RemoveSystemBit(self.systemBit)
        self.Removed(entity)
    def SetWorld(self, world):
        self.world = world
    def Toggle(self):
        self.enabled = not self.enabled
    def Enable(self):
        self.enabled = True
    def Disable(self):
        self.enabled = False
    @classmethod
    def GetMergedTypes(cls, requiredType, *otherTypes):
        types = [requiredType]
        types.extend(otherTypes)
        return types
