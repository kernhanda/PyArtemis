class ComponentType(object):
    _nextBit = 1
    _nextId = 0
    
    def __init__(self):
        self.bit = self._nextBit
        self._nextBit = self._nextBit << 1
        self.id = self._nextId
        self._nextId += 1
    def GetBit(self):
        return self.bit
    def GetId(self):
        return self.id
