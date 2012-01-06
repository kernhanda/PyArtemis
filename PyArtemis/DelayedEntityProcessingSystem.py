from PyArtemis.DelayedEntitySystem import DelayedEntitySystem

class DelayedEntityProcessingSystem(DelayedEntitySystem):
    def __init__(self, requiredType, *otherTypes):
        super(DelayedEntityProcessingSystem, self).__init__(*self.GetMergedTypes(requiredType, *otherTypes))
    def Process(self, entity, accumulatedDelta):
        raise NotImplementedError
    def ProcessEntities(self, entities, accumulatedDelta):
        for e in entities:
            self.Process(e, accumulatedDelta)
