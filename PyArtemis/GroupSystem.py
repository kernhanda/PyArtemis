from PyArtemis.EntitySystem import EntitySystem

class GroupSystem(EntitySystem):
    def __init__(self, group):
        super(GroupSystem, self).__init__()
        self.group = group
    def Process(self, entity):
        raise NotImplementedError
    def ProcessEntities(self, entities):
        groupedEntities = self.world.GetGroupManager().GetEntities(self.group)
        for e in groupedEntities:
            self.Process(e)
