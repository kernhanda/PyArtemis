from PyArtemis.EntitySystem import EntitySystem
from PyArtemis.SystemBitManager import SystemBitManager
from PyArtemis.Utils import GetClass

class ExecutionType:
    DRAW = 0
    UPDATE = 1

class SystemManager(object):
    def __init__(self, world):
        self.world = world
        self.systems = {}

        self.layers = [{}, {}]
        self.mergedBag = []
    def SetSystem(self, system, execType, layer = 0):
        if not isinstance(system, EntitySystem): raise TypeError
        system.SetWorld(self.world)
        self.systems[GetClass(system)] = system

        if execType == ExecutionType.DRAW or execType == ExecutionType.UPDATE:
            bag = self.layers[execType].setdefault(layer, [])
            if system not in bag:
                bag.append(system)

        if system not in self.mergedBag:
            self.mergedBag.append(system)
        system.SetSystemBit(SystemBitManager.GetBitFor(system))

        return system
    def GetSystem(self, systemType):
        _t = Utils.GetClass(systemType)
        if not issubclass(_t, EntitySystem): raise TypeError
        return self.systems.get(_t)
    def GetSystems(self):
        return self.mergedBag
    def InitializeAll(self):
        map(lambda x: x.Initialize(), self.mergedBag)
    def UpdatebagSync(self, temp):
        for t in temp:
            t.Process()
    def UpdateSynchronous(self, execType):
        if execType == ExecutionType.DRAW or execType == ExecutionType.UPDATE:
            d = self.layers[execType]
            for k in d:
                self.UpdatebagSync(d[k])
    def UpdatebagASSync(self, temp): #needed?
        pass
    def UpdateAsynchronous(self, execType): #needed?
        pass
