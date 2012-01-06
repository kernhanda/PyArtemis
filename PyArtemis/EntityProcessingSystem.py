from PyArtemis.EntitySystem import EntitySystem

class EntityProcessingSystem(EntitySystem):
    def __init__(self, requiredType, *otherTypes):
        super(EntityProcessingSystem, self).__init__(*self.GetMergedTypes(requiredType, *otherTypes))
    def Process(self, entity = None):
        if not entity:
            return super(EntityProcessingSystem, self).Process()
        raise NotImplementedError
    def ProcessEntities(self, entities):
        for e in entities.itervalues():
            self.Process(e)
