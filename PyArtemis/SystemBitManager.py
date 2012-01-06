class SystemBitManager(object):
    _POS = 0
    _systemBits = {}
    
    @classmethod
    def GetBitFor(cls, entitySystem):
        bit = cls._systemBits.get(entitySystem)
        if bit is None:
            bit = 1 << cls._POS
            cls._POS += 1
            cls._systemBits[entitySystem] = bit

        return bit
