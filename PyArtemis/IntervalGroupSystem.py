from PyArtemis.GroupSystem import GroupSystem

class IntervalGroupSystem(GroupSystem):
    def __init__(self, interval, group):
        super(IntervalGroupSystem, self).__init__(group)
        self.interval = interval
        self.acc = 0
    def CheckProcessing(self):
        self.acc += self.world.GetDelta()
        if self.acc >= self.interval:
            self.acc -= self.interval
            return self.enabled
        return False
