class GroupManager(object):
    def __init__(self, world):
        self.world = world
        self.entitiesByGroup = {}
        self.groupByEntity = {}
    def Set(self, group, e):
        self.Remove(e)

        entities = self.entitiesByGroup.get(group)
        if not entities:
            entities = []
            self.entitiesByGroup[group] = entities
        entities.append(e)

        self.groupByEntity[e.GetId()] = group
    def GetEntities(self, group):
        entities = self.entitiesByGroup.get(group)
        return entities
    def Remove(self, entity):
        eId = entity.GetId()
        if eId in self.groupByEntity:
            group = self.groupByEntity[eId]
            del self.groupByEntity[eId]

            entities = self.entitiesByGroup.get(group)
            if entities:
                entities.remove(entity)
    def GetGroupOf(self, entity):
        return self.groupByEntity.get(entity.GetId())
    def IsGrouped(self, entity):
        return self.GetGroupOf(entity) is not None

