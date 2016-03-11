import random

class Tile(object):
    def __init__(self, x, y):
        self.position = (x, y)
        self.occupied = False
        self.occupier = ''
        self.entity = None

    def update(self):
        #print "X:%r, Y:%r: " % self.position,
        #if self.occupied: print "%s on Tile." % self.occupier
        #else: print "Tile empty."
        pass

    def is_occupied(self):
        return self.occupied

    def get_occupier(self):
        return self.occupier

    def occupy(self, entity_type):
        from hunter import Hunter
        from zombie import Zombie
        from victim import Victim

        self.occupied = True
        self.occupier = entity_type
        if self.occupier == "Zombie":
            self.entity = Zombie(self.position)
        elif self.occupier == "Victim":
            self.entity = Victim(self.position)
        elif self.occupier == "Hunter":
            self.entity = Hunter(self.position)
        
    def vacated(self):
        self.occupied = False
        self.occupier = ''
        self.entity = None

    def print_pos(self):
        print self.position

