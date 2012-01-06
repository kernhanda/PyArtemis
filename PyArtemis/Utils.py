from types import ClassType, TypeType

def GetClass(x):
    if type(x) in [ClassType, TypeType]:
        return x
    else:
        return x.__class__
