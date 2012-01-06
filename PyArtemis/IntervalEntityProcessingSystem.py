from PyArtemis.IntervalEntitySystem import IntervalEntitySystem

class IntervalEntityProcessingSystem(IntervalEntitySystem):
    def __init__(self, interval, requiredType, *otherTypes):
        super(IntervalEntitySystem, self).__init__(interval, *self.GetMergedTypes(requiredType, *otherTypes))
    def Process(self):
        raise NotImplementedError
    def ProcessEntities(self, entities):
        for k in entities:
            self.Process(entities[k])
