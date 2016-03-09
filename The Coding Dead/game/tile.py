class Tile(object):
    def __init__(self, x, y):
        self.position = (x, y)
        self.occupied = False
        self.occupier = ''

    def update(self):
        print "%r updated." % self.position

    def isOccupied(self):
        return self.occupied

    def occupy(self, entity_type):
        self.occupied = True
        self.occupier = entity_type

    def printPos(self):
        print self.position
