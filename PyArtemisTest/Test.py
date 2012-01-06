from Components.Health import Health
from System.DummySystem import DummySystem
from System.DummySystem2 import DummySystem2
from System.DummySystem3 import DummySystem3
from System.SingleHealthBarRenderSystem import SingleHealthBarRenderSystem
from System.SingleHEAVYHealthBarRenderSystem import SingleHEAVYHealthBarRenderSystem
from PyArtemis.Component import Component
from PyArtemis.EntityWorld import EntityWorld
from PyArtemis.SystemManager import ExecutionType
from datetime import datetime

class Test(object):
    healthBag = []
    componentPool = {}

    @classmethod
    def RemovedComponent(cls, entity, component):
        typeComponent = type(component)
        print "This was the component removed:", typeComponent
        tempBag = cls.componentPool.get(typeComponent, [])
        print "Health Component Pool has", len(tempBag), "objects"
        tempBag.append(component)
        tempBag = cls.componentPool.get(typeComponent, [])
        print "Health Component Pool now has", len(tempBag), "objects"

    @classmethod
    def RemovedEntity(cls, entity):
        print "This was the entity removed:", entity.GetUniqueId()

    @classmethod
    def multi(cls):
        cls.healthBag.append(Health())
        cls.healthBag.append(Health())
        cls.componentPool[Health] = cls.healthBag

        tempBag = []
        world = EntityWorld()
        systemManager = world.GetSystemManager()
        world.GetEntityManager().RemovedComponentEvent.append(cls.RemovedComponent)
        world.GetEntityManager().RemovedEntityEvent.append(cls.RemovedEntity)

        hs = systemManager.SetSystem(SingleHEAVYHealthBarRenderSystem(), ExecutionType.UPDATE)
        systemManager.InitializeAll()

        l = []
        for i in range(1000):
            et = world.CreateEntity()
            et.AddComponent(Health())
            et.GetComponent(Health).AddHealth(100)
            et.Refresh()
            l.append(et)

        for i in range(100):
            dt = datetime.now()
            world.LoopStart()
            systemManager.UpdateSynchronous(ExecutionType.UPDATE)
            print (datetime.now() - dt).microseconds

        df = 0
        for i in l:
            i.GetComponent(Health).GetHealth() == 90
            df += 1

        raw_input()
    @classmethod
    def multisystem(cls):
        cls.healthBag.append(Health())
        cls.healthBag.append(Health())
        cls.componentPool[Health] = cls.healthBag

        tempBag = []
        world = EntityWorld()
        systemManager = world.GetSystemManager()
        world.GetEntityManager().RemovedComponentEvent.append(cls.RemovedComponent)
        world.GetEntityManager().RemovedEntityEvent.append(cls.RemovedEntity)
        hs = systemManager.SetSystem(SingleHealthBarRenderSystem(), ExecutionType.UPDATE)
        hs = systemManager.SetSystem(DummySystem(), ExecutionType.UPDATE)
        hs = systemManager.SetSystem(DummySystem2(), ExecutionType.UPDATE)
        hs = systemManager.SetSystem(DummySystem3(), ExecutionType.UPDATE)
        systemManager.InitializeAll()

        l = []
        for i in range(100000):
            et = world.CreateEntity()
            et.AddComponent(Health())
            et.GetComponent(Health).AddHealth(100)
            et.Refresh()
            l.append(et)

        for i in range(100):
            dt = datetime.now()
            world.LoopStart()
            systemManager.UpdateSynchronous(ExecutionType.UPDATE)
            print (datetime.now() - dt).microseconds
    @classmethod
    def Main(cls):
        #cls.multi()
        cls.multisystem()

if __name__ == '__main__':
    Test.Main()
