from PyArtemis.TagSystem import TagSystem

class IntervalTagSystem(TagSystem):
    def __init__(self, interval, tag):
        super(IntervalTagSystem, self).__init__(tag)
        self.interval = interval
        self.acc = 0
    def CheckProcessing(self):
        self.acc += self.world.GetDelta()
        if self.acc >= self.interval:
            self.acc -= self.interval
            return self.enabled
        return False
