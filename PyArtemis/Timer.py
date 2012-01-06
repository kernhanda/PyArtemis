class Timer(object):
    def __init__(self, delay, repeat):
        self.delay = delay
        self.repeat = repeat
        self.acc = 0
        self.done = self.stopped = False
    def Update(self, delta):
        if self.done or self.stopped:
            return
        self.acc += delta
        if self.acc >= self.delay:
            self.acc -= self.delay

            if self.repeat:
                self.Reset()
            else:
                self.done = True

            self.Execute()
    def Reset(self):
        self.stopped = self.done = False
        self.acc = 0
    def IsDone(self):
        return self.done
    def IsRunning(self):
        return not self.done and self.acc < self.delay and not self.stopped
    def Stop(self):
        self.stopped = True
    def SetDelay(self, delay):
        self.delay = delay
    def Execute(self):
        raise NotImplementedError
    def GetPercentageRemaining(self):
        if self.done: return 100
        if self.stopped: return 0
        return 1 - (self.delay - self.acc)/float(self.delay)
    def GetDelay(self):
        return self.delay
