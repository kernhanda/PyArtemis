from PyArtemis.EntitySystem import EntitySystem

class IntervalEntitySystem(EntitySystem):
    def __init__(self, interval, *types):
        super(IntervalEntitySystem, self).__init__(*types)
        self.interval = interval
        self.acc = 0
    def CheckProcessing(self):
        self.acc += self.world.GetDelta()
        if self.acc >= self.interval:
            self.acc -= self.interval
            return self.enabled
        return False
