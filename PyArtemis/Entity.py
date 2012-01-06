from PyArtemis.Component import Component

class Entity(object):
    def __init__(self, world, id):
        self.world = world
        self.entityManager = world.GetEntityManager()
        self.id = id
        self.uniqueId = self.typeBits = self.systemBits = 0
    def GetId(self):
        return self.id
    def SetUniqueId(self, uniqueId):
        self.uniqueId = uniqueId
    def GetUniqueId(self):
        return self.uniqueId
    def GetTypeBits(self):
        return self.typeBits
    def AddTypeBit(self, bit):
        self.typeBits |= bit
    def RemoveTypeBit(self, bit):
        self.typeBits &= ~bit
    def GetSystemBits(self):
        return self.systemBits
    def AddSystemBit(self, bit):
        self.systemBits |= bit
    def RemoveSystemBit(self, bit):
        self.systemBits &= ~bit
    def SetSystemBits(self, bits):
        self.systemBits = bits
    def SetTypeBits(self, bits):
        self.typeBits = bits
    def Reset(self):
        self.typeBits = self.systemBits = 0
    def __str__(self):
        return "Entity[{0}]".format(self.id)
    def AddComponent(self, component):
        if not isinstance(component, Component): raise TypeError
        self.entityManager.AddComponent(self, component)
    def RemoveComponent(self, component):
        if not isinstance(component, Component): raise TypeError
        self.entityManager.RemoveComponent(self, component)
    def IsActive(self):
        return self.entityManager.IsActive(self.id)
    def GetComponent(self, componentType):
        return self.entityManager.GetComponent(self, componentType)
    def GetComponents(self):
        self.entityManager.GetComponents(self)
    def Refresh(self):
        self.world.RefreshEntity(self)
    def Delete(self):
        self.world.DeleteEntity(self)
    def SetGroup(self, group):
        self.world.GetGroupManager().Set(group, self)
    def SetTag(self, tag):
        self.world.GetTagManager().Register(tag, self)
    def GetTag(self):
        return self.world.GetTagManager().GetTagOfEntity(self)
    
