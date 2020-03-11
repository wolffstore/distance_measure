import random

class Sensor:

    def __init__(self,id,side,echo,trigger):
        self.id = id
        self.side = side
        self.echo = echo
        self.trigger = trigger

    def getDistance(self):
        return random.randrange(0,51)
