import PyArtemis.EntitySystem

class DelayedEntitySystem(PyArtemis.EntitySystem.EntitySystem):
    def __init__(self, *types):
        super(DelayedEntitySystem, self).__init__(*types)
        self.acc = self.delay = 0
        self.running = False
    def ProcessEntities(self, entities):
        self.ProcessEntities(entities, self.acc)
        self.Stop()
    def CheckProcessing(self):
        if self.running:
            self.acc += self.world.GetDelta()

            if self.acc >= self.delay:
                return self.enabled
        return False
    def ProcessEntities(self, entities, accumulatedDelta):
        raise NotImplementedError
    def StartDelayedRun(self, delay):
        self.delay = delay
        self.acc = 0
        self.running = True
    def GetInitialTimeDelay(self):
        return self.delay
    def GetRemainingTimeUntilProcessing(self):
        if self.running:
            return self.delay - self.acc
        return 0
    def IsRunning(self):
        return self.running
    def Stop(self):
        self.running = False
        self.acc = 0
