import PyArtemis.EntitySystem

class TagSystem(PyArtemis.EntitySystem):
    def __init__(self, tag):
        super(TagSystem, self).__init__()
        self.tag = tag
    def Process(self, entity):
        raise NotImplementedError
    def ProcessEntities(self, entities):
        e = self.world.GetTagManager().GetEntity(tag)
        if e:
            self.Process(e)
