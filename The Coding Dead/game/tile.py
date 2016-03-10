class Tile(object):
    def __init__(self, x, y):
        self.position = (x, y)
        self.occupied = False
        self.occupier = ''

    def update(self):
        print "X:%r, Y:%r: " % self.position,
        if self.occupied: print "%s on Tile." % self.occupier
        else: print "Tile empty."

    def is_occupied(self):
        return self.occupied

    def get_occupier(self):
        return self.occupier

    def occupy(self, entity_type):
        self.occupied = True
        self.occupier = entity_type

    def print_pos(self):
        print self.position
