from PyArtemis.Component import Component

class Health(Component):
    """description of class"""
    def __init__(self, health = 0):
        self.maximumHealth = self.health = health
    def GetHealth(self):
        return self.health
    def AddHealth(self, health):
        self.health += health
    def GetMaximumHealth(self):
        return self.maximumHealth
    def GetHealthPercentage(self):
        return int(float(self.health) / self.maximumHealth * 100)
    def AddDamage(self, damage):
        self.health -= damage
        if self.health < 0: self.health = 0
    def IsAlive(self):
        return self.health > 0
