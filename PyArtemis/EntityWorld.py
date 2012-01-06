from PyArtemis.EntityManager import EntityManager
from PyArtemis.SystemManager import SystemManager
from PyArtemis.TagManager import TagManager
from PyArtemis.GroupManager import GroupManager
from PyArtemis.Utils import GetClass

class EntityWorld(object):
    def __init__(self):
        self.entityManager = EntityManager(self)
        self.systemManager = SystemManager(self)
        self.tagManager = TagManager(self)
        self.groupManager = GroupManager(self)

        self.pool = None

        self.refreshed = []
        self.deleted = []
        self.managers = {}
        self.delta = 0
    def SetManager(self, manager):
        self.managers[GetClass(manager)] = manager
    def GetManager(self, manager):
        return self.managers.get(GetClass(manager))
    def GetGroupManager(self):
        return self.groupManager
    def GetSystemManager(self):
        return self.systemManager
    def GetEntityManager(self):
        return self.entityManager
    def GetTagManager(self):
        return self.tagManager
    def GetDelta(self):
        return self.delta
    def SetDelta(self, delta):
        self.delta = delta
    def DeleteEntity(self, entity):
        self.groupManager.Remove(entity)
        if entity not in self.deleted:
            self.deleted.append(entity)
    def RefreshEntity(self, entity):
        self.refreshed.append(entity)
    def CreateEntity(self, tag = None):
        entity = self.entityManager.Create()
        self.tagManager.Register(tag, entity)
        return entity
    def GetEntity(self, entityId):
        return self.entityManager.GetEntity(entityId)
    def SetPool(self, artemisPool):
        self.pool = artemisPool
    def GetPool(self):
        return self.pool
    def LoopStart(self):
        for e in self.refreshed:
            self.entityManager.Refresh(e)
        self.refreshed = []
        for e in self.deleted:
            self.entityManager.Remove(e)
        self.deleted = []
    def GetCurrentState(self):
        entities = self.entityManager.GetActiveEntities()
        currentState = {}
        for e in entities.itervalues():
            components = e.GetComponents()
            currentState[e] = components
        return currentState
    def LoadEntityState(self, tag = None, groupName = None, *components):
        entity = self.CreateEntity(tag)
        if groupName:
            self.groupManager.Set(groupName, entity)
        for c in components:
            entity.AddComponent(c)
