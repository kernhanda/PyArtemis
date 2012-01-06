from PyArtemis.Utils import GetClass
from PyArtemis.Entity import Entity
from PyArtemis.Component import Component
from PyArtemis.ComponentType import ComponentType
from PyArtemis.ComponentTypeManager import ComponentTypeManager

class EntityManager(object):
    REMOVED_COMPONENT_EVENT = "RemovedComponent"
    REMOVED_ENTITY_EVENT    = "RemovedEntity"
    ADDED_COMPONENT_EVENT   = "AddedComponent"
    ADDED_ENTITY_EVENT      = "AddedEntity"
    def __init__(self, world):
        self.world = world
        self.activeEntities = {}
        self.removedAndAvailable = []
        self.componentsByType = {}
        self.entityComponents = [] # apparently for debug support; needed?
        self.nextAvailableId = self.count = self.uniqueEntityId = self.totalCreated = self.totalRemoved = 0
        self.events = { EntityManager.REMOVED_COMPONENT_EVENT : [],
                        EntityManager.REMOVED_ENTITY_EVENT : [],
                        EntityManager.ADDED_COMPONENT_EVENT : [],
                        EntityManager.ADDED_ENTITY_EVENT : [] }
        self.RemovedComponentEvent = self.events[EntityManager.REMOVED_COMPONENT_EVENT]
        self.RemovedEntityEvent = self.events[EntityManager.REMOVED_ENTITY_EVENT]
        self.AddedComponentEvent = self.events[EntityManager.ADDED_COMPONENT_EVENT]
        self.AddedEntityEvent = self.events[EntityManager.ADDED_ENTITY_EVENT]
    def Create(self):
        if self.removedAndAvailable:
            e = self.removedAndAvailable.pop()
        else:
            e = None
        if not e:
            e = Entity(self.world, self.nextAvailableId)
            self.nextAvailableId += 1
        else:
            e.Reset()
        e.SetUniqueId(self.uniqueEntityId)
        self.uniqueEntityId += 1
        self.activeEntities[e.GetId()] = e
        self.count += 1
        self.totalCreated += 1
        for event in self.events[EntityManager.ADDED_ENTITY_EVENT]:
            event(e)
        return e
    def Remove(self, entity):
        del self.activeEntities[entity.GetId()]
        entity.SetTypeBits(0)
        Refresh(entity)
        self.RemoveComponentsOfEntity(entity)
        self.count -= 1
        self.totalRemoved += 1
        self.removedAndAvailable.append(entity)
        for event in self.events[EntityManager.REMOVED_ENTITY_EVENT]:
            event(entity)
    def RemoveComponentsOfEntity(self, entity):
        id = entity.GetId()
        for componentTypes in self.componentsByType.itervalues():
            if id in componentTypes:
                for event in self.events[EntityManager.REMOVED_COMPONENT_EVENT]:
                    event(entity, componentTypes[id])
                del componentTypes[id]
    def IsActive(self, id):
        return id in self.activeEntities[id]
    def AddComponent(self, entity, component):
        componentType = ComponentTypeManager.GetTypeFor(GetClass(component))
        
        components = self.componentsByType.get(componentType.GetId())
        if not components:
            components = {}
            self.componentsByType[componentType.GetId()] = components

        components[entity.GetId()] = component
        entity.AddTypeBit(componentType.GetBit())
        for event in self.events[EntityManager.ADDED_COMPONENT_EVENT]:
            event(entity, component)
    def Refresh(self, entity):
        systemManager = self.world.GetSystemManager()
        for s in systemManager.GetSystems():
            s.Change(entity)
    def RemoveComponent(self, entity, componentType):
        eId = entity.GetId()
        components = self.componentsByType[componentType.GetId()]
        for event in self.events[EntityManager.REMOVED_COMPONENT_EVENT]:
            event(entity, components[eId])
        del  components[eId]
        entity.RemoveTypeBit(componentType.GetBit())
    def GetComponent(self, entity, componentType = None):
        _ct = GetClass(componentType)
        if issubclass(_ct, Component):
            componentType = ComponentTypeManager.GetTypeFor(_ct)
        eId = entity.GetId()
        components = self.componentsByType.get(componentType.GetId())
        if components and eId in components:
            return components[eId]
        return None
    def GetEntity(self, entityId):
        return self.activeEntities.get(entityId)
    def GetEntityCount(self):
        return self.count
    def GetTotalCreated(self):
        return self.totalCreated
    def GetTotalRemoved(self):
        return self.totalRemoved
    def GetComponents(self, entity):
        self.entityComponents = []
        eId = entity.GetId()
        for components in self.componentsByType.itervalues():
            if components: #TODO
                component = components.get(eId)
                if component: #TODO
                    self.entityComponents.append(component)
        return self.entityComponents
    def GetActiveEntities(self):
        return self.activeEntities
