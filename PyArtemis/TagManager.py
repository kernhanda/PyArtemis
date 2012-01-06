class TagManager(object):
    def __init__(self, world):
        self.world = world
        self.entityByTag = {}
    def Register(self, tag, entity):
        self.entityByTag[tag] = entity
    def Unregister(self, tag):
        del self.entityByTag[tag]
    def IsRgistered(self, tag):
        return tag in self.entityByTag
    def GetEntity(self, tag):
        e = self.entityByTag.get(tag)
        if e and not e.IsActive():
            self.Unregister(e)
            e = None
        return e
    def GetTagOfEntity(self, entity):
        tag = ''
        for k, v in self.entityByTag.iteritems():
            if v is entity:
                tag = k
                break
        return tag
